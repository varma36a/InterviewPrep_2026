"""Infer time/space complexity for Love Babbar 450 DSA problems from title + topic."""

from __future__ import annotations

import re
from typing import Callable

Meta = dict[str, str]

# (pattern_regex, meta_override) — first match wins
_RULES: list[tuple[str, Meta]] = [
    (r"reverse.*array|reverse the array|rotate.*array|cyclically rotate", {
        "pattern": "In-place reversal / rotation",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Each element moved once during reverse or rotate.",
        "space_auxiliary": "O(1)", "space_why": "In-place two-pointer swap or triple-reversal trick.",
        "approach": "Two pointers swap from both ends, or reverse subarrays for rotation.",
    }),
    (r"two sum|pair.*sum|complement", {
        "pattern": "Hash map one-pass",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Single pass with O(1) average hash lookups for complement.",
        "space_auxiliary": "O(n)", "space_why": "Hash map stores up to n elements.",
        "approach": "Scan array; for each value check if (target - value) exists in map.",
    }),
    (r"three sum|3sum|four sum|4sum", {
        "pattern": "Sort + two pointers / nested loops",
        "time_best": "O(n²)", "time_average": "O(n²)", "time_worst": "O(n²)",
        "time_why": "Sort O(n log n) + two-pointer scan for each fixed element.",
        "space_auxiliary": "O(1) or O(n)", "space_why": "O(1) excluding output; O(n) if dedup set needed.",
        "approach": "Sort array; fix one index and use two pointers for remaining pair sum.",
    }),
    (r"kadane|largest sum contiguous|maximum subarray|max subarray", {
        "pattern": "Kadane's algorithm (DP/greedy)",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "One pass tracking running max ending here and global max.",
        "space_auxiliary": "O(1)", "space_why": "Only scalar variables for current/global max.",
        "approach": "Extend subarray or restart at current index when sum goes negative.",
    }),
    (r"binary search|search in.*sorted|find.*sorted array", {
        "pattern": "Binary search",
        "time_best": "O(log n)", "time_average": "O(log n)", "time_worst": "O(log n)",
        "time_why": "Halve search space each iteration on sorted/monotonic data.",
        "space_auxiliary": "O(1)", "space_why": "Iterative binary search uses constant pointers.",
        "approach": "Maintain left/right bounds; compare mid and discard half.",
    }),
    (r"merge sort|quick sort|heap sort|counting sort|radix sort|bucket sort", {
        "pattern": "Sorting algorithm",
        "time_best": "O(n log n)", "time_average": "O(n log n)", "time_worst": "O(n log n)",
        "time_why": "Comparison sorts are O(n log n); counting/radix can be O(n+k) on bounded keys.",
        "space_auxiliary": "O(n)", "space_why": "Merge sort needs O(n) auxiliary; in-place quicksort O(log n) stack.",
        "approach": "Apply standard sort; analyze stability and in-place requirements.",
    }),
    (r"sort.*without.*sort|dutch national|0.*1.*2|three color", {
        "pattern": "Dutch national flag / counting",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Three-way partition or count buckets in linear time.",
        "space_auxiliary": "O(1)", "space_why": "In-place three-pointer partition.",
        "approach": "Use low/mid/high pointers or count 0s/1s/2s then rewrite array.",
    }),
    (r"sliding window|subarray.*length|longest substring|minimum window|max consecutive", {
        "pattern": "Sliding window",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Each index enters and leaves window at most once.",
        "space_auxiliary": "O(k)", "space_why": "Frequency map sized by alphabet or distinct chars in window.",
        "approach": "Expand right until invalid, shrink left until valid; track best window.",
    }),
    (r"two pointer|container.*water|trapping rain|palindrome", {
        "pattern": "Two pointers",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Pointers move monotonically across array/string once.",
        "space_auxiliary": "O(1)", "space_why": "Only index pointers and scalar trackers.",
        "approach": "Place pointers at ends or both at start; move based on comparison/greedy rule.",
    }),
    (r"reverse linked list|reverse.*list", {
        "pattern": "Iterative/recursive reversal",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Visit each node exactly once to rewire next pointers.",
        "space_auxiliary": "O(1)", "space_why": "Iterative uses three pointers; recursive uses O(n) stack.",
        "approach": "prev/curr/next walk or recurse to end then reverse links on unwind.",
    }),
    (r"cycle.*linked|detect cycle|floyd|tortoise", {
        "pattern": "Floyd cycle detection",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Fast pointer traverses at most 2n nodes before cycle detected.",
        "space_auxiliary": "O(1)", "space_why": "Two pointer references only.",
        "approach": "Slow moves 1 step, fast 2 steps; meeting inside cycle proves loop.",
    }),
    (r"merge.*sorted.*list|merge k sorted|merge two", {
        "pattern": "Merge lists / heap",
        "time_best": "O(n + m)", "time_average": "O(n + m)", "time_worst": "O(n + m)",
        "time_why": "Each node compared and linked once across input lists.",
        "space_auxiliary": "O(1)", "space_why": "Iterative merge rewires pointers without extra list.",
        "approach": "Dummy head; compare heads, attach smaller, advance pointer.",
    }),
    (r"valid parenthes|parenthesis|balanced bracket", {
        "pattern": "Stack matching",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Each character pushed/popped at most once.",
        "space_auxiliary": "O(n)", "space_why": "Stack holds up to n opening brackets.",
        "approach": "Push opens; on close verify top matches and pop.",
    }),
    (r"monotonic stack|next greater|next smaller|daily temperature|histogram|stock span", {
        "pattern": "Monotonic stack",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Each index pushed and popped at most once — amortized O(n).",
        "space_auxiliary": "O(n)", "space_why": "Stack stores indices waiting for next greater/smaller.",
        "approach": "Maintain decreasing/increasing stack; pop when current resolves pending indices.",
    }),
    (r"min stack|getmin.*o\(1\)", {
        "pattern": "Auxiliary min tracking",
        "time_best": "O(1)", "time_average": "O(1)", "time_worst": "O(1)",
        "time_why": "Push/pop/top/getMin each O(1) with paired min stack or stored tuple.",
        "space_auxiliary": "O(n)", "space_why": "Second stack or pairs store running minimum per level.",
        "approach": "Push (value, currentMin); pop both together.",
    }),
    (r"level order|zigzag|vertical order|boundary", {
        "pattern": "BFS level-order traversal",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Each node enqueued and dequeued once.",
        "space_auxiliary": "O(n)", "space_why": "Queue holds up to widest level (~n/2 nodes).",
        "approach": "BFS with queue; process level size batches for level-wise output.",
    }),
    (r"lca|lowest common ancestor", {
        "pattern": "BST walk or post-order DFS",
        "time_best": "O(h)", "time_average": "O(h)", "time_worst": "O(n)",
        "time_why": "Descend from root; split point is LCA. Skewed tree height n.",
        "space_auxiliary": "O(h)", "space_why": "Recursive DFS stack depth equals tree height.",
        "approach": "If both nodes on different sides of root, root is LCA; else recurse into child side.",
    }),
    (r"validate bst|is bst|check bst", {
        "pattern": "In-order or min/max bounds",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Visit each node once with range validation.",
        "space_auxiliary": "O(h)", "space_why": "Recursion stack depth h; iterative uses O(h) explicit stack.",
        "approach": "Pass (min, max) bounds down; node must lie strictly inside.",
    }),
    (r"diameter|height|depth|max path|sum tree", {
        "pattern": "Tree DFS aggregation",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Single post-order pass computes answer at each node once.",
        "space_auxiliary": "O(h)", "space_why": "Recursion depth equals tree height.",
        "approach": "Recurse children; combine left/right results at parent for global optimum.",
    }),
    (r"serialize|deserialize.*tree", {
        "pattern": "Pre-order encoding",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Visit and encode/decode each node once.",
        "space_auxiliary": "O(n)", "space_why": "Output string/list length proportional to n nodes.",
        "approach": "Pre-order with null markers; rebuild recursively from stream.",
    }),
    (r"number of islands|flood fill|connected component|surrounded regions", {
        "pattern": "Grid DFS/BFS flood fill",
        "time_best": "O(rows × cols)", "time_average": "O(rows × cols)", "time_worst": "O(rows × cols)",
        "time_why": "Each cell visited once across all components.",
        "space_auxiliary": "O(rows × cols)", "space_why": "DFS stack or BFS queue in worst case full grid.",
        "approach": "Scan grid; on land start DFS/BFS, mark visited, increment count.",
    }),
    (r"topological|course schedule|detect cycle.*directed", {
        "pattern": "Topological sort (Kahn/DFS colors)",
        "time_best": "O(V + E)", "time_average": "O(V + E)", "time_worst": "O(V + E)",
        "time_why": "Each vertex and edge processed once.",
        "space_auxiliary": "O(V + E)", "space_why": "Adjacency list, indegree array, and queue/stack.",
        "approach": "Kahn BFS peel zero-indegree nodes or DFS 3-color cycle detection.",
    }),
    (r"dijkstra|shortest path|bellman|floyd", {
        "pattern": "Shortest path algorithm",
        "time_best": "O((V + E) log V)", "time_average": "O((V + E) log V)", "time_worst": "O((V + E) log V)",
        "time_why": "Dijkstra with min-heap relaxes each edge once. Bellman-Ford O(VE).",
        "space_auxiliary": "O(V + E)", "space_why": "Distance array O(V) plus graph/heap storage.",
        "approach": "Relax edges from settled nodes; use heap for non-negative weights.",
    }),
    (r"union.?find|disjoint set|kruskal", {
        "pattern": "Union-Find (DSU)",
        "time_best": "O(α(n))", "time_average": "O(α(n))", "time_worst": "O(α(n))",
        "time_why": "Inverse Ackermann α(n) amortized per union/find with path compression.",
        "space_auxiliary": "O(n)", "space_why": "Parent and rank arrays for n elements.",
        "approach": "Find with path compression; union by rank/size.",
    }),
    (r"word ladder|bfs.*word|transformation", {
        "pattern": "BFS on implicit graph",
        "time_best": "O(n × wordLen)", "time_average": "O(n × wordLen)", "time_worst": "O(n × wordLen)",
        "time_why": "Each word dequeued once; try wordLen character substitutions.",
        "space_auxiliary": "O(n)", "space_why": "Visited set and BFS queue of words.",
        "approach": "BFS from startWord; generate neighbors by one-char change.",
    }),
    (r"heap|priority queue|kth largest|kth smallest|top k|median.*stream", {
        "pattern": "Heap / priority queue",
        "time_best": "O(n log k)", "time_average": "O(n log k)", "time_worst": "O(n log k)",
        "time_why": "Maintain size-k heap: n inserts each O(log k).",
        "space_auxiliary": "O(k)", "space_why": "Heap stores k elements (or two heaps for median).",
        "approach": "Min-heap of size k for kth largest; balance two heaps for median.",
    }),
    (r"coin change|knapsack|unbounded|0/1 knapsack|subset sum|partition equal", {
        "pattern": "Dynamic programming — knapsack family",
        "time_best": "O(n × W)", "time_average": "O(n × W)", "time_worst": "O(n × W)",
        "time_why": "Fill DP table over n items and capacity/target W.",
        "space_auxiliary": "O(W)", "space_why": "1D rolling DP over target/capacity dimension.",
        "approach": "dp[w] = min/max ways to reach sum w using processed items.",
    }),
    (r"longest increasing subsequence|lis", {
        "pattern": "Patience sorting / DP",
        "time_best": "O(n log n)", "time_average": "O(n log n)", "time_worst": "O(n log n)",
        "time_why": "Binary search on tails array for each element.",
        "space_auxiliary": "O(n)", "space_why": "Tails array length at most n.",
        "approach": "Replace first tail ≥ current with binary search; length = LIS.",
    }),
    (r"longest common subsequence|lcs|edit distance|levenshtein", {
        "pattern": "2D DP on strings",
        "time_best": "O(m × n)", "time_average": "O(m × n)", "time_worst": "O(m × n)",
        "time_why": "Fill (m+1)×(n+1) table comparing each char pair.",
        "space_auxiliary": "O(min(m, n))", "space_why": "Rolling two-row optimization over longer dimension.",
        "approach": "dp[i][j] from dp[i-1][j], dp[i][j-1], dp[i-1][j-1] based on match.",
    }),
    (r"matrix chain|optimal binary search|palindrome partitioning.*min", {
        "pattern": "Interval DP",
        "time_best": "O(n³)", "time_average": "O(n³)", "time_worst": "O(n³)",
        "time_why": "Try all split points for every interval length.",
        "space_auxiliary": "O(n²)", "space_why": "2D DP table over interval start/end.",
        "approach": "dp[i][j] = min cost for subproblem [i,j]; iterate by length.",
    }),
    (r"climbing stair|fibonacci|count.*ways.*step", {
        "pattern": "Linear DP / Fibonacci",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Each state computed once from prior two states.",
        "space_auxiliary": "O(1)", "space_why": "Rolling two variables suffice.",
        "approach": "dp[i] = dp[i-1] + dp[i-2]; answer at dp[n].",
    }),
    (r"house robber|max sum.*non.?adjacent", {
        "pattern": "Linear DP — take/skip",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Single pass with take/skip recurrence.",
        "space_auxiliary": "O(1)", "space_why": "Track prev_max and curr_max only.",
        "approach": "At each house: max(skip, take + prev_prev).",
    }),
    (r"backtrack|subset|permutation|combination|n.?queens|sudoku|rat in a maze|word search", {
        "pattern": "Backtracking",
        "time_best": "O(2^n)", "time_average": "O(2^n)", "time_worst": "O(n!)",
        "time_why": "Exponential search tree; permutations n!, subsets 2^n.",
        "space_auxiliary": "O(n)", "space_why": "Recursion depth n plus path/used array.",
        "approach": "Choose/explore/unchoose; prune invalid branches early.",
    }),
    (r"greedy|activity selection|fractional knapsack|huffman|job sequencing", {
        "pattern": "Greedy choice",
        "time_best": "O(n log n)", "time_average": "O(n log n)", "time_worst": "O(n log n)",
        "time_why": "Sort by greedy key then linear scan.",
        "space_auxiliary": "O(1)", "space_why": "In-place after sort except output list.",
        "approach": "Prove greedy choice property; sort and pick locally optimal.",
    }),
    (r"trie|prefix tree|word dictionary|autocomplete", {
        "pattern": "Trie traversal",
        "time_best": "O(m)", "time_average": "O(m)", "time_worst": "O(m)",
        "time_why": "m = key length; traverse/create one node per character.",
        "space_auxiliary": "O(n × m)", "space_why": "Trie stores up to n keys of average length m.",
        "approach": "Walk trie per character; mark end-of-word at terminal node.",
    }),
    (r"bit manip|xor|single number|power of two|count set bit|power set", {
        "pattern": "Bit manipulation",
        "time_best": "O(1)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Single ops O(1); scanning all bits/elements O(n) or O(log n).",
        "space_auxiliary": "O(1)", "space_why": "Bit tricks use constant extra variables.",
        "approach": "Use AND/OR/XOR/shifts; Brian Kernighan for set bits.",
    }),
    (r"rotate.*matrix|spiral|search.*matrix|set matrix zero", {
        "pattern": "Matrix traversal / in-place transform",
        "time_best": "O(rows × cols)", "time_average": "O(rows × cols)", "time_worst": "O(rows × cols)",
        "time_why": "Each cell read/written constant times.",
        "space_auxiliary": "O(1)", "space_why": "In-place layer rotation or marker row/col.",
        "approach": "Traverse layers or use first row/col as zero flags.",
    }),
    (r"kmp|rabin.?karp|pattern match|strstr|anagram|palindrome.*string", {
        "pattern": "String matching / frequency",
        "time_best": "O(n + m)", "time_average": "O(n + m)", "time_worst": "O(n + m)",
        "time_why": "KMP/Rabin-Karp linear in text n plus pattern m.",
        "space_auxiliary": "O(m)", "space_why": "LPS array or rolling hash window size m.",
        "approach": "Build LPS for KMP or sliding window char counts for anagram.",
    }),
    (r"hash|frequency|anagram|duplicate|count.*element", {
        "pattern": "Hash map / frequency count",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Single pass with O(1) average map operations.",
        "space_auxiliary": "O(n)", "space_why": "Map stores up to n distinct keys.",
        "approach": "Count occurrences in dictionary; answer from frequencies.",
    }),
    (r"prefix sum|subarray sum|cumulative", {
        "pattern": "Prefix sum",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Build prefix array O(n); each range query O(1).",
        "space_auxiliary": "O(n)", "space_why": "Prefix array length n+1.",
        "approach": "prefix[j] - prefix[i] = sum(i..j-1); combine with hash map for target sum.",
    }),
]

_TOPIC_DEFAULTS: dict[str, Meta] = {
    "Array": {
        "pattern": "Array scan / hash / two pointers",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n²)",
        "time_why": "Typical array problems: one pass O(n) or nested loops O(n²) for pairs.",
        "space_auxiliary": "O(1)", "space_why": "Often in-place; hash-based solutions use O(n) extra.",
        "approach": "Clarify constraints; prefer one-pass hash or two-pointer over O(n²) brute force.",
    },
    "Matrix": {
        "pattern": "Matrix traversal",
        "time_best": "O(rows × cols)", "time_average": "O(rows × cols)", "time_worst": "O(rows × cols)",
        "time_why": "Visit each cell at least once.",
        "space_auxiliary": "O(1)", "space_why": "In-place row/col marking when possible.",
        "approach": "Row/column-wise scan or layer-by-layer boundary traversal.",
    },
    "String": {
        "pattern": "String processing",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n × m)",
        "time_why": "Linear scan O(n); pattern matching may add pattern length m.",
        "space_auxiliary": "O(n)", "space_why": "Output or frequency map proportional to input.",
        "approach": "Two pointers, sliding window, or KMP for pattern search.",
    },
    "Searching & Sorting": {
        "pattern": "Search or sort",
        "time_best": "O(log n)", "time_average": "O(n log n)", "time_worst": "O(n log n)",
        "time_why": "Binary search O(log n) on sorted data; comparison sort O(n log n).",
        "space_auxiliary": "O(1)", "space_why": "In-place sort or iterative binary search.",
        "approach": "Pick algorithm matching stability and space constraints.",
    },
    "LinkedList": {
        "pattern": "Linked list pointers",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Single pass over n nodes typical.",
        "space_auxiliary": "O(1)", "space_why": "Pointer manipulation without extra list.",
        "approach": "Dummy head for edge cases; fast/slow for cycle and midpoint.",
    },
    "Binary Trees": {
        "pattern": "Tree DFS/BFS",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Each of n nodes visited once.",
        "space_auxiliary": "O(h)", "space_why": "Recursion/stack depth equals tree height h.",
        "approach": "Pre/in/post-order DFS or level BFS depending on problem.",
    },
    "Binary Search Trees": {
        "pattern": "BST property exploitation",
        "time_best": "O(h)", "time_average": "O(log n)", "time_worst": "O(n)",
        "time_why": "Balanced BST height log n; skewed degrades to n.",
        "space_auxiliary": "O(h)", "space_why": "Recursive calls or explicit stack depth h.",
        "approach": "Use ordering: left < root < right for search/insert/delete.",
    },
    "Greedy": {
        "pattern": "Greedy selection",
        "time_best": "O(n log n)", "time_average": "O(n log n)", "time_worst": "O(n log n)",
        "time_why": "Sort by greedy key then linear pass.",
        "space_auxiliary": "O(1)", "space_why": "Constant extra after sorting in-place.",
        "approach": "Prove local optimal leads to global optimal; sort then scan.",
    },
    "BackTracking": {
        "pattern": "Backtracking",
        "time_best": "O(2^n)", "time_average": "O(2^n)", "time_worst": "O(n!)",
        "time_why": "Explore decision tree; permutations factorial, subsets exponential.",
        "space_auxiliary": "O(n)", "space_why": "Recursion depth and current path storage.",
        "approach": "Add choice, recurse, undo; prune invalid partial solutions.",
    },
    "Stacks & Queues": {
        "pattern": "Stack/queue simulation",
        "time_best": "O(n)", "time_average": "O(n)", "time_worst": "O(n)",
        "time_why": "Each element pushed/popped once.",
        "space_auxiliary": "O(n)", "space_why": "Stack/queue holds up to n elements.",
        "approach": "Use monotonic stack for next-greater or queue for BFS-like order.",
    },
    "Heap": {
        "pattern": "Heap operations",
        "time_best": "O(n log n)", "time_average": "O(n log n)", "time_worst": "O(n log n)",
        "time_why": "Build heap O(n) or n extract-min operations O(n log n).",
        "space_auxiliary": "O(n)", "space_why": "Heap stores all n elements.",
        "approach": "Use min/max heap for kth element, merge k lists, or scheduling.",
    },
    "Graph": {
        "pattern": "Graph BFS/DFS",
        "time_best": "O(V + E)", "time_average": "O(V + E)", "time_worst": "O(V + E)",
        "time_why": "Each vertex and edge processed once in adjacency list representation.",
        "space_auxiliary": "O(V + E)", "space_why": "Visited set, queue/stack, and adjacency storage.",
        "approach": "BFS for shortest unweighted paths; DFS for connectivity and cycles.",
    },
    "Trie": {
        "pattern": "Trie",
        "time_best": "O(m)", "time_average": "O(m)", "time_worst": "O(m)",
        "time_why": "m = key length; one step per character.",
        "space_auxiliary": "O(n × m)", "space_why": "Trie nodes for n strings average length m.",
        "approach": "Insert/search by walking children per character.",
    },
    "Dynamic Programming": {
        "pattern": "Dynamic programming",
        "time_best": "O(n × W)", "time_average": "O(n × W)", "time_worst": "O(n²)",
        "time_why": "Depends on state dimensions: 1D O(n), 2D O(n²), knapsack O(n×W).",
        "space_auxiliary": "O(W)", "space_why": "Often optimized to 1D rolling array over target/capacity.",
        "approach": "Define state, recurrence, base cases; bottom-up tabulation preferred in interviews.",
    },
    "Bit Manipulation": {
        "pattern": "Bit tricks",
        "time_best": "O(1)", "time_average": "O(log n)", "time_worst": "O(n)",
        "time_why": "Word-level ops O(1); bit iteration O(log n) or O(n) bits.",
        "space_auxiliary": "O(1)", "space_why": "Constant extra variables for XOR/AND/shift patterns.",
        "approach": "Isolate bits with masks; XOR cancels pairs; Brian Kernighan counts set bits.",
    },
}

_TOPIC_GUIDES: dict[str, dict] = {
    "array": {
        "title": "Array",
        "explanation": (
            "Array problems dominate interviews. **Random access is O(1)** but insert/delete in middle is **O(n)**. "
            "Most optimal solutions use **hash maps** (O(n) time, O(n) space), **two pointers** (O(n), O(1)), "
            "or **prefix sums** for range queries.\n\n"
            "**Key patterns:** complement lookup, frequency counting, Kadane for subarrays, Dutch flag for 3-way partition, "
            "and sort-then-scan when order unlocks greedy or two-pointer moves."
        ),
        "key_points": ["Hash map: O(n) time average", "Two pointers: O(n) time O(1) space", "Kadane: O(n) max subarray", "Sort: O(n log n) unlocks many patterns"],
    },
    "matrix": {
        "title": "Matrix",
        "explanation": (
            "Matrix problems reduce to **O(rows × cols)** traversal unless binary search on sorted matrix (**O(log(rows×cols))**). "
            "Use **layer-by-layer spiral**, **in-place row/col markers** for zero matrix, or **transpose + reverse** for rotation.\n\n"
            "Space is usually **O(1)** when transforming in-place; BFS on matrix uses **O(rows×cols)** queue worst case."
        ),
        "key_points": ["Full scan: O(rows × cols)", "Sorted matrix search: O(log n)", "In-place rotation: O(1) extra", "BFS flood: queue up to all cells"],
    },
    "string": {
        "title": "String",
        "explanation": (
            "String problems often use **sliding window** (O(n)) or **two pointers** for palindrome/substring tasks. "
            "Pattern matching: **KMP/Rabin-Karp** in O(n+m). Anagram problems use **frequency maps** of size alphabet.\n\n"
            "Clarify whether input is Unicode or ASCII — alphabet size affects space in frequency arrays."
        ),
        "key_points": ["Sliding window: O(n) amortized", "KMP: O(n + m) pattern search", "Anagram: O(n) with freq map", "Palindrome two-pointer: O(n)"],
    },
    "searching-sorting": {
        "title": "Searching & Sorting",
        "explanation": (
            "**Binary search** requires sorted or monotonic predicate — **O(log n)**. "
            "Comparison sorts are **O(n log n)** lower bound. Linear search **O(n)** when unsorted.\n\n"
            "Know merge sort (stable, O(n) extra), quicksort (in-place, O(log n) stack), counting/radix for bounded keys."
        ),
        "key_points": ["Binary search: O(log n)", "Merge/quick sort: O(n log n)", "Counting sort: O(n + k) for range k", "Search rotated array: modified BS"],
    },
    "linked-list": {
        "title": "Linked List",
        "explanation": (
            "Lists lack O(1) random access — expect **O(n)** scans. **Dummy nodes** simplify head deletion. "
            "**Fast/slow pointers** detect cycles and find mid in O(n) O(1). Reversal is **O(n)** iterative or recursive.\n\n"
            "Recursive solutions add **O(n) stack** — mention when comparing to iterative O(1) space."
        ),
        "key_points": ["Dummy head for edge cases", "Floyd cycle: O(n) O(1)", "Reverse in-place: O(n) O(1)", "Merge sorted lists: O(n+m)"],
    },
    "binary-trees": {
        "title": "Binary Trees",
        "explanation": (
            "Tree traversals visit each node once → **O(n)**. Stack/queue space **O(h)** where h is height "
            "(O(n) skewed, O(log n) balanced).\n\n"
            "**Post-order** aggregates from children (height, diameter, max path). **BFS** gives level-order and shortest path in unweighted tree."
        ),
        "key_points": ["DFS/BFS: O(n) time", "Recursion depth O(h)", "Diameter/max-path: post-order combine", "Serialize: O(n) pre-order"],
    },
    "bst": {
        "title": "Binary Search Trees",
        "explanation": (
            "BST operations are **O(h)** — O(log n) balanced, O(n) skewed. **In-order traversal** yields sorted order. "
            "Validate with **global min/max bounds**, not parent-only check.\n\n"
            "Deletion has three cases: leaf, one child, two children (in-order successor)."
        ),
        "key_points": ["Search/insert/delete: O(h)", "In-order = sorted", "Validate with bounds", "Self-balancing AVL/RB: O(log n) guaranteed"],
    },
    "greedy": {
        "title": "Greedy",
        "explanation": (
            "Greedy picks locally optimal choice if **greedy choice property** and **optimal substructure** hold. "
            "Usually **O(n log n)** from sorting by key (intervals, activities).\n\n"
            "Prove greediness or cite exchange argument — interviewers expect justification, not just code."
        ),
        "key_points": ["Sort + scan: O(n log n)", "Interval scheduling classic", "Huffman: heap O(n log n)", "Prove greedy choice property"],
    },
    "backtracking": {
        "title": "BackTracking",
        "explanation": (
            "Backtracking explores decision trees: subsets **O(2^n)**, permutations **O(n!)**. "
            "Prune early when partial solution cannot succeed (N-Queens, Sudoku).\n\n"
            "Auxiliary space **O(n)** for recursion depth and current path; output may dominate."
        ),
        "key_points": ["Subsets: O(2^n)", "Permutations: O(n!)", "Prune invalid branches", "Undo choice after recursion"],
    },
    "stack-queue": {
        "title": "Stacks & Queues",
        "explanation": (
            "Stacks solve **LIFO** nesting and **monotonic next-greater/smaller** in **O(n) amortized**. "
            "Queues model BFS and sliding-window max with deque.\n\n"
            "Min-stack uses auxiliary structure for O(1) getMin at O(n) space cost."
        ),
        "key_points": ["Monotonic stack: O(n) amortized", "Valid parentheses: O(n)", "Queue BFS: O(n) per level", "Deque window max: O(n)"],
    },
    "heap": {
        "title": "Heap",
        "explanation": (
            "Heaps give **O(log n)** insert/extract and **O(1)** peek. **Top-k** problems: min-heap size k → **O(n log k)**. "
            "Merge k sorted lists: heap of k heads → **O(n log k)**.\n\n"
            "Two-heap median trick balances halves in O(log n) per add."
        ),
        "key_points": ["Insert/extract: O(log n)", "Top-k: O(n log k)", "Build heap: O(n)", "Two heaps for streaming median"],
    },
    "graph": {
        "title": "Graph",
        "explanation": (
            "Adjacency-list BFS/DFS: **O(V + E)**. Grid graphs: **O(rows × cols)**. "
            "**Topological sort** for dependencies; **Dijkstra** for non-negative shortest paths.\n\n"
            "Union-Find for dynamic connectivity in near **O(α(n))** per operation."
        ),
        "key_points": ["BFS/DFS: O(V + E)", "Dijkstra: O((V+E) log V)", "Topo sort detects DAG cycle", "Union-Find: O(α(n)) amortized"],
    },
    "trie": {
        "title": "Trie",
        "explanation": (
            "Trie supports insert/search in **O(m)** per key of length m. Space **O(n × m)** for n strings. "
            "Beats hash maps when **prefix queries** matter (autocomplete, word search).\n\n"
            "Compress paths (radix tree) if memory is tight."
        ),
        "key_points": ["Insert/search: O(m) per key", "Prefix search natural fit", "Space: O(n × m) nodes", "vs hash: prefix wins"],
    },
    "dp": {
        "title": "Dynamic Programming",
        "explanation": (
            "DP = optimal substructure + overlapping subproblems. "
            "1D linear DP often **O(n) time O(1) space** (Fibonacci, house robber). "
            "2D string DP **O(m × n)**. Knapsack **O(n × W)**.\n\n"
            "Always state state definition, transition, base case, and iteration order."
        ),
        "key_points": ["Define state before coding", "1D rolling: O(n) O(1)", "2D LCS: O(m × n)", "Knapsack: O(n × W)"],
    },
    "bit-manipulation": {
        "title": "Bit Manipulation",
        "explanation": (
            "Bit tricks run in **O(1)** or **O(log n)** word operations. "
            "**XOR** finds single unique; **n & (n-1)** clears lowest set bit (Brian Kernighan).\n\n"
            "Power set via bits: **O(2^n × n)** to enumerate all subsets."
        ),
        "key_points": ["XOR cancels pairs", "n & (n-1) clears lowest bit", "Check power of 2: n & (n-1) == 0", "Subset bitmask: O(2^n)"],
    },
}

_TOPIC_TO_PHASE: dict[str, str] = {
    "Array": "array",
    "Matrix": "matrix",
    "String": "string",
    "Searching & Sorting": "searching-sorting",
    "LinkedList": "linked-list",
    "Binary Trees": "binary-trees",
    "Binary Search Trees": "bst",
    "Greedy": "greedy",
    "BackTracking": "backtracking",
    "Stacks & Queues": "stack-queue",
    "Heap": "heap",
    "Graph": "graph",
    "Trie": "trie",
    "Dynamic Programming": "dp",
    "Bit Manipulation": "bit-manipulation",
}

_PHASE_ORDER = [
    "array", "matrix", "string", "searching-sorting", "linked-list",
    "binary-trees", "bst", "greedy", "backtracking", "stack-queue",
    "heap", "graph", "trie", "dp", "bit-manipulation",
]


def _difficulty(problem: str) -> str:
    p = problem.lower()
    if any(k in p for k in ("hard", "v.imp", "v. imp", "imp]", "[imp")):
        return "Hard"
    if any(k in p for k in ("medium", "optimal", "o(1)", "o(log")):
        return "Medium"
    return "Medium"


def infer_complexity(problem: str, topic: str) -> Meta:
    """Return complexity metadata for a problem title and topic."""
    text = problem.lower()
    for pattern, meta in _RULES:
        if re.search(pattern, text, re.I):
            result = dict(_TOPIC_DEFAULTS.get(topic, _TOPIC_DEFAULTS["Array"]))
            result.update(meta)
            result["difficulty"] = _difficulty(problem)
            result["pattern"] = meta.get("pattern", result["pattern"])
            return result

    base = dict(_TOPIC_DEFAULTS.get(topic, _TOPIC_DEFAULTS["Array"]))
    base["difficulty"] = _difficulty(problem)
    base["approach"] = (
        f"Standard {topic} approach: identify brute force, then optimize using "
        f"{base['pattern'].lower()} typical for this category."
    )
    return base


def build_explanation(problem: str, meta: Meta) -> str:
    """Interview-sheet style markdown explanation."""
    diff = meta.get("difficulty", "Medium")
    return (
        f"**Problem:** {problem}\n"
        f"**Pattern:** {meta['pattern']}\n"
        f"**Difficulty:** {diff}\n\n"
        f"**Approach:** {meta['approach']}\n\n"
        f"### Time Complexity\n"
        f"| Case | Complexity |\n"
        f"| Best | {meta['time_best']} |\n"
        f"| Average | {meta['time_average']} |\n"
        f"| Worst | {meta['time_worst']} |\n\n"
        f"**Why:** {meta['time_why']}\n\n"
        f"### Space Complexity\n"
        f"| Type | Complexity |\n"
        f"| Auxiliary | {meta['space_auxiliary']} |\n\n"
        f"**Why:** {meta['space_why']}"
    )


def key_points_from_meta(meta: Meta) -> list[str]:
    return [
        f"Pattern: {meta['pattern']}",
        f"Time: {meta['time_worst']} worst ({meta['time_best']} best)",
        f"Space: {meta['space_auxiliary']} auxiliary",
    ]


def slugify(text: str, max_len: int = 36) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:max_len].rstrip("-") or "problem"


def get_topic_guides() -> dict[str, dict]:
    return _TOPIC_GUIDES


def get_phase_order() -> list[str]:
    return _PHASE_ORDER


def topic_to_phase(topic: str) -> str:
    return _TOPIC_TO_PHASE.get(topic, slugify(topic))
