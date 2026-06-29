"""DSA complexity guides — interview-sheet style time/space analysis for all 50 problems."""

from __future__ import annotations

import re

TOPIC_GUIDES: dict[str, dict] = {
    "arrays": {
        "phase_id": "arrays",
        "title": "Arrays, Hashing & Strings",
        "explanation": (
            "Arrays give **O(1) random access** but shifting or searching unsorted data is **O(n)**. "
            "Hash maps and sets trade **O(n) extra space** for **O(1) average** lookups — the default "
            "upgrade when brute force is O(n²).\n\n"
            "**Interview moves:** one-pass complement lookup (Two Sum), frequency/count buckets "
            "(Group Anagrams), prefix/suffix accumulation (Product Except Self), and sort-then-scan "
            "(Merge Intervals, Longest Consecutive).\n\n"
            "Always state whether you count **auxiliary space** separately from the required output array."
        ),
        "key_points": [
            "Hash map/set: O(1) avg lookup, O(n) space",
            "Sort unlocks two-pointer and greedy scans — O(n log n)",
            "Prefix/suffix passes achieve O(n) without division",
            "Clarify output array vs auxiliary space in analysis",
        ],
    },
    "pointers-window": {
        "phase_id": "pointers-window",
        "title": "Two Pointers & Sliding Window",
        "explanation": (
            "Two pointers shrink the search space on **sorted** or **monotonic** structures — "
            "typically **O(n)** with **O(1)** extra space. Sliding windows maintain a valid range "
            "[left, right] and expand/shrink based on constraints.\n\n"
            "**Fixed window:** add right, remove left when size exceeds k. "
            "**Variable window:** expand until invalid, then shrink until valid again. "
            "Each index enters and leaves the window at most once → **amortized O(n)**.\n\n"
            "Monotonic deques extend windows to track max/min in O(1) amortized per step."
        ),
        "key_points": [
            "Two pointers on sorted data: O(n) time, O(1) space",
            "Sliding window: each index visited ≤ twice → O(n)",
            "Monotonic deque for window max/min — amortized O(n)",
            "State the window invariant before coding",
        ],
    },
    "linked-list": {
        "phase_id": "linked-list",
        "title": "Linked Lists",
        "explanation": (
            "Linked lists have **O(1) insert/delete** at a known node but **O(n) access** by index. "
            "Most list problems use **two or three pointers** (prev/curr/next, fast/slow) in **O(n) time** "
            "and **O(1) auxiliary space**.\n\n"
            "**Dummy sentinel nodes** simplify edge cases (empty head, remove head). "
            "Floyd's cycle detection runs in O(n) time with two pointers moving at different speeds.\n\n"
            "Recursive solutions add **O(n) call-stack space** — mention this when comparing to iterative."
        ),
        "key_points": [
            "Dummy node eliminates head edge cases",
            "Fast/slow pointers: cycle detection in O(n), O(1) space",
            "Gap of n pointers → nth-from-end in one pass",
            "Iterative reversal: O(n) time, O(1) space vs O(n) stack",
        ],
    },
    "stack-queue": {
        "phase_id": "stack-queue",
        "title": "Stack, Queue & Monotonic Stack",
        "explanation": (
            "Stacks model **LIFO** nesting (parentheses) and **next-greater/smaller** relationships. "
            "Each element is pushed and popped at most once → **O(n) amortized** for monotonic stack problems.\n\n"
            "Monotonic stacks keep indices or values in sorted order so the top always answers "
            "the current query (next warmer day, histogram rectangle width).\n\n"
            "Queue + deque variants support BFS and sliding-window maximum. "
            "Auxiliary stack space is **O(n)** in the worst case."
        ),
        "key_points": [
            "Parentheses matching: single stack, O(n) time and space",
            "Monotonic stack: each index pushed/popped once → O(n)",
            "Store indices in stack to compute spans and widths",
            "Min Stack: O(1) ops via auxiliary min tracking — O(n) space",
        ],
    },
    "trees": {
        "phase_id": "trees",
        "title": "Trees & Binary Search Trees",
        "explanation": (
            "Tree traversal visits each node once → **O(n) time**. Recursion depth equals tree height "
            "**h**, giving **O(h) auxiliary stack space** (O(n) skewed, O(log n) balanced).\n\n"
            "BST problems exploit ordering: in-order is sorted, search/LCA run in **O(h)**. "
            "Validation needs **global bounds**, not just parent comparison.\n\n"
            "BFS level-order uses a queue sized up to the widest level — **O(n) space** worst case."
        ),
        "key_points": [
            "DFS visits n nodes → O(n) time; stack depth O(h)",
            "BST walk from root: O(h) time, O(1) space iterative",
            "Validate BST with min/max bounds, not parent-only check",
            "BFS queue holds up to O(n) nodes at bottom level",
        ],
    },
    "graphs": {
        "phase_id": "graphs",
        "title": "Graphs, BFS & DFS",
        "explanation": (
            "Graph algorithms typically cost **O(V + E)** for adjacency-list traversal. "
            "Grid problems treat each cell as a vertex with ≤4 edges → **O(rows × cols)**.\n\n"
            "**BFS** finds shortest unweighted paths; **multi-source BFS** seeds many nodes at once "
            "(rotting oranges). **Topological sort** detects cycles in directed graphs.\n\n"
            "Visited tracking (set, color array, or in-place grid mutation) prevents infinite loops "
            "and ensures each vertex is processed once."
        ),
        "key_points": [
            "Adjacency list BFS/DFS: O(V + E) time and space",
            "Grid flood fill: O(rows × cols) — each cell visited once",
            "Multi-source BFS for simultaneous propagation",
            "Topological sort (Kahn/DFS colors) detects cycles in O(V + E)",
        ],
    },
    "heap-search": {
        "phase_id": "heap-search",
        "title": "Heaps & Binary Search",
        "explanation": (
            "Binary search halves the search space each step → **O(log n)** on sorted or monotonic "
            "answer spaces. Watch for **overflow-safe mid**, inclusive/exclusive bounds, and "
            "rotated-array sorted-half logic.\n\n"
            "Heaps maintain top-k in **O(n log k)** vs **O(n log n)** full sort. "
            "Two-heap median structure balances halves in **O(log n)** per insert.\n\n"
            "**Binary search on answer:** monotonic feasibility (Koko Bananas) — "
            "O(n log M) where M is the answer range."
        ),
        "key_points": [
            "Binary search: O(log n) when half the space is eliminated each step",
            "Min-heap size k: O(n log k) for kth largest / top-k frequent",
            "Two heaps: O(log n) insert, O(1) median query",
            "Search on answer requires monotonic feasible/infeasible predicate",
        ],
    },
    "dp": {
        "phase_id": "dp",
        "title": "Dynamic Programming",
        "explanation": (
            "DP avoids exponential recomputation by storing subproblem results. "
            "Identify **state**, **transition**, and **base cases** before coding.\n\n"
            "1D DP (stairs, robber, coin change) often compresses to **O(1) or O(amount) space**. "
            "2D DP (LCS) costs **O(m × n) time and space**, optimizable to O(min(m, n)).\n\n"
            "Patience sorting / binary search on tails achieves **O(n log n)** for LIS — "
            "a common follow-up when O(n²) DP is too slow."
        ),
        "key_points": [
            "Define state and recurrence before writing loops",
            "1D rolling DP reduces space from O(n) to O(1) when only prior rows matter",
            "Unbounded knapsack: iterate amount outer, coins inner",
            "LIS: O(n²) DP easy; O(n log n) patience sorting for follow-ups",
        ],
    },
    "backtracking": {
        "phase_id": "backtracking",
        "title": "Backtracking & Greedy",
        "explanation": (
            "Backtracking explores a decision tree: choose → recurse → undo. "
            "Time is **O(output size × work per leaf)** — subsets **O(n × 2ⁿ)**, permutations **O(n × n!)**.\n\n"
            "**Pruning** (sort + break early, remain < 0) cuts branches without changing worst-case Big-O.\n\n"
            "Always **copy the path** when recording results; reuse one mutable path with pop after recurse."
        ),
        "key_points": [
            "Template: choose → explore → unchoose (backtrack)",
            "Subsets: 2ⁿ combinations; permutations: n! orderings",
            "Combination Sum: reuse candidate → recurse same index",
            "Sort + prune to skip dominated branches early",
        ],
    },
}


COMPLEXITY_META: dict[str, dict] = {
    "dsa-two-sum": {
        "leetcode": 1,
        "difficulty": "Easy",
        "pattern": "Hash map complement lookup",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Each element is processed once with O(1) average hash map lookup and insert. "
            "No nested loops — a single pass over n elements dominates the runtime."
        ),
        "space_auxiliary": "O(n)",
        "space_why": (
            "The hash map stores up to n value→index pairs in the worst case when no two elements match until the end. "
            "No other auxiliary structures are needed."
        ),
        "approach": (
            "One-pass hash map: for each nums[i], check if target - nums[i] exists in the map. "
            "If found, return both indices; otherwise store nums[i] → i and continue."
        ),
    },
    "dsa-contains-duplicate": {
        "leetcode": 217,
        "difficulty": "Easy",
        "pattern": "Hash set membership",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Single pass over n elements with O(1) average HashSet insert/lookup. "
            "Sorting alternative would be O(n log n) but hash set stays linear."
        ),
        "space_auxiliary": "O(n)",
        "space_why": (
            "HashSet may hold all n distinct values when no duplicate exists. "
            "In-place sort achieves O(1) extra space but sacrifices O(n log n) time."
        ),
        "approach": (
            "Add each number to a HashSet; if Add returns false, a duplicate exists. "
            "Return true on first collision, false if the loop completes."
        ),
    },
    "dsa-product-except-self": {
        "leetcode": 238,
        "difficulty": "Medium",
        "pattern": "Prefix / suffix accumulation",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Two linear passes over the array — one left-to-right for prefix products, "
            "one right-to-left for suffix products. Each pass is O(n), totaling O(n)."
        ),
        "space_auxiliary": "O(1)",
        "space_why": (
            "Only a running suffix variable is used beyond the output array, which does not count toward auxiliary space. "
            "No hash map or extra array of size n is required."
        ),
        "approach": (
            "First pass fills answer[i] with the product of all elements to the left. "
            "Second pass multiplies by a running suffix product of all elements to the right."
        ),
    },
    "dsa-max-subarray": {
        "leetcode": 53,
        "difficulty": "Medium",
        "pattern": "Kadane's algorithm (greedy DP)",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "One pass: at each index decide whether to extend the current subarray or restart. "
            "Constant work per element gives O(n) regardless of input values."
        ),
        "space_auxiliary": "O(1)",
        "space_why": (
            "Only two scalar variables (current sum and best sum) are tracked. "
            "No auxiliary array or recursion stack is needed."
        ),
        "approach": (
            "Kadane's algorithm: currentSum = max(nums[i], currentSum + nums[i]); "
            "best = max(best, currentSum). Handles all-negative arrays correctly."
        ),
    },
    "dsa-merge-intervals": {
        "leetcode": 56,
        "difficulty": "Medium",
        "pattern": "Sort + greedy merge",
        "time_best": "O(n log n)",
        "time_average": "O(n log n)",
        "time_worst": "O(n log n)",
        "time_why": (
            "Sorting intervals by start time dominates at O(n log n). "
            "The merge scan is a single O(n) pass after sorting."
        ),
        "space_auxiliary": "O(n)",
        "space_why": (
            "The merged result list can hold up to n intervals in the worst case (no overlaps). "
            "In-place sort uses O(log n) stack if merge output is excluded."
        ),
        "approach": (
            "Sort intervals by start. Iterate: if current overlaps the last merged interval, extend its end; "
            "otherwise append a new interval."
        ),
    },
    "dsa-group-anagrams": {
        "leetcode": 49,
        "difficulty": "Medium",
        "pattern": "Hash map with canonical key",
        "time_best": "O(n × k log k)",
        "time_average": "O(n × k log k)",
        "time_worst": "O(n × k log k)",
        "time_why": (
            "For n strings of average length k, sorting each string as a key costs O(k log k) per string. "
            "Char-count key alternative is O(n × k) with fixed alphabet."
        ),
        "space_auxiliary": "O(n × k)",
        "space_why": (
            "The dictionary stores every character of every string across all groups. "
            "Key storage (sorted string or 26-int count) adds overhead per group entry."
        ),
        "approach": (
            "Map each word to a canonical key (sorted string or char-frequency signature). "
            "Append the word to the dictionary list for that key; return all values."
        ),
    },
    "dsa-longest-consecutive": {
        "leetcode": 128,
        "difficulty": "Medium",
        "pattern": "Hash set streak expansion",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Each number is visited at most twice — once when checking if it starts a streak, "
            "once during streak expansion. HashSet lookups are O(1) average."
        ),
        "space_auxiliary": "O(n)",
        "space_why": (
            "All n elements are stored in a HashSet for O(1) existence checks. "
            "No additional structures grow beyond O(n)."
        ),
        "approach": (
            "Insert all nums into a HashSet. Only start counting when num-1 is absent (streak head). "
            "Walk num+1, num+2, … while present and track max length."
        ),
    },
    "dsa-valid-palindrome": {
        "leetcode": 125,
        "difficulty": "Easy",
        "pattern": "Two pointers converging",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Left and right pointers move inward at most once each across n characters. "
            "Skipping non-alphanumeric still visits each index a constant number of times."
        ),
        "space_auxiliary": "O(1)",
        "space_why": (
            "Comparison is in-place with two index variables. "
            "No substring allocation or auxiliary string is created."
        ),
        "approach": (
            "Two pointers at both ends. Skip non-alphanumeric characters, "
            "compare lowercased letters, move inward; return false on mismatch."
        ),
    },
    "dsa-two-sum-ii": {
        "leetcode": 167,
        "difficulty": "Medium",
        "pattern": "Two pointers on sorted array",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Each step moves either left or right pointer inward — at most n steps total. "
            "Sorted order guarantees no valid pair is skipped."
        ),
        "space_auxiliary": "O(1)",
        "space_why": (
            "Only two pointer indices are stored. "
            "The sorted input is given; no hash map is required."
        ),
        "approach": (
            "Left pointer at index 0, right at n-1. "
            "If sum < target, increment left; if sum > target, decrement right; if equal, return 1-based indices."
        ),
    },
    "dsa-container-water": {
        "leetcode": 11,
        "difficulty": "Medium",
        "pattern": "Greedy two pointers",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Pointers start at both ends and move inward once per iteration — at most n-1 iterations. "
            "Area calculation is O(1) per step."
        ),
        "space_auxiliary": "O(1)",
        "space_why": (
            "Only pointer indices and a running max area variable are used. "
            "No auxiliary arrays or stacks."
        ),
        "approach": (
            "Compute area = min(height[l], height[r]) × (r - l). "
            "Move the pointer at the shorter line inward — only a shorter line can potentially increase area."
        ),
    },
    "dsa-trapping-rain": {
        "leetcode": 42,
        "difficulty": "Hard",
        "pattern": "Two pointers with running max",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Each index is processed once as pointers move inward. "
            "Water at each step is computed in O(1) using leftMax or rightMax."
        ),
        "space_auxiliary": "O(1)",
        "space_why": (
            "Two-pointer approach tracks leftMax and rightMax scalars. "
            "Prefix-max arrays would use O(n) but are not needed here."
        ),
        "approach": (
            "Two pointers at both ends with leftMax and rightMax. "
            "Process the side with the smaller max; water += max(0, sideMax - height[pointer])."
        ),
    },
    "dsa-longest-substring": {
        "leetcode": 3,
        "difficulty": "Medium",
        "pattern": "Sliding window + last-seen map",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Right pointer advances n times; left pointer moves forward at most n times total. "
            "Amortized O(1) work per character with hash map updates."
        ),
        "space_auxiliary": "O(min(n, Σ))",
        "space_why": (
            "The last-seen map holds at most one entry per distinct character in the window. "
            "Σ is alphabet size (26 for lowercase ASCII, 128 for ASCII)."
        ),
        "approach": (
            "Expand window with right pointer; on duplicate, jump left past the previous occurrence. "
            "Track last index per character and update max window length."
        ),
    },
    "dsa-min-window-substring": {
        "leetcode": 76,
        "difficulty": "Hard",
        "pattern": "Sliding window with frequency map",
        "time_best": "O(|s| + |t|)",
        "time_average": "O(|s| + |t|)",
        "time_worst": "O(|s| + |t|)",
        "time_why": (
            "Right pointer scans s once; left pointer advances at most |s| times. "
            "Each character enters and leaves the window at most once — amortized O(1) per char."
        ),
        "space_auxiliary": "O(|s| + |t|)",
        "space_why": (
            "Frequency maps for need and window characters bounded by unique chars in t and s. "
            "At most O(Σ) or O(|t|) distinct keys in practice."
        ),
        "approach": (
            "Expand window until all required char counts are satisfied, then shrink from the left "
            "while still valid to minimize length. Track best window during shrink."
        ),
    },
    "dsa-sliding-window-max": {
        "leetcode": 239,
        "difficulty": "Hard",
        "pattern": "Monotonic deque",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Each index is pushed to the deque once and popped at most once. "
            "Amortized O(1) per element despite inner while loops."
        ),
        "space_auxiliary": "O(k)",
        "space_why": (
            "The monotonic deque stores at most k indices representing candidates for the window maximum. "
            "In the worst case all k indices fit before any are evicted."
        ),
        "approach": (
            "Maintain a deque of indices in decreasing value order. "
            "Front is always the current window max; evict out-of-window and dominated indices on each step."
        ),
    },
    "dsa-max-consecutive-ones": {
        "leetcode": 1004,
        "difficulty": "Medium",
        "pattern": "Variable sliding window (zero budget)",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Right pointer advances n times; left pointer moves forward at most n times when zero count exceeds k. "
            "Amortized linear total pointer movement."
        ),
        "space_auxiliary": "O(1)",
        "space_why": (
            "Only zero count, left/right pointers, and best length are tracked. "
            "No auxiliary array or deque is required."
        ),
        "approach": (
            "Expand window with right pointer, counting zeros. "
            "When zeros > k, shrink from left decrementing zero count until valid again; track max window size."
        ),
    },
    "dsa-reverse-linked-list": {
        "leetcode": 206,
        "difficulty": "Easy",
        "pattern": "Iterative three-pointer reversal",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Each of n nodes is visited exactly once with constant pointer rewiring. "
            "Recursive variant also touches each node once but adds stack cost."
        ),
        "space_auxiliary": "O(1)",
        "space_why": (
            "Iterative solution uses three pointer references (prev, curr, next). "
            "Recursive approach uses O(n) call stack — state O(1) for iterative."
        ),
        "approach": (
            "Iterate with prev=null, curr=head: save next, point curr.next to prev, advance prev and curr. "
            "Return prev as the new head."
        ),
    },
    "dsa-merge-two-lists": {
        "leetcode": 21,
        "difficulty": "Easy",
        "pattern": "Dummy head merge",
        "time_best": "O(n + m)",
        "time_average": "O(n + m)",
        "time_worst": "O(n + m)",
        "time_why": (
            "Each node from both lists is attached exactly once. "
            "Total pointer advances equal n + m."
        ),
        "space_auxiliary": "O(1)",
        "space_why": (
            "Nodes are rewired in place; only dummy head and tail pointer variables are extra. "
            "No new nodes are allocated beyond the existing lists."
        ),
        "approach": (
            "Dummy sentinel node; compare heads of l1 and l2, attach smaller to tail, advance. "
            "Append remaining non-null list when one exhausts."
        ),
    },
    "dsa-linked-list-cycle": {
        "leetcode": 141,
        "difficulty": "Easy",
        "pattern": "Floyd's tortoise and hare",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Slow pointer moves 1 step, fast moves 2; if cycle exists they meet within n slow steps. "
            "If no cycle, fast reaches null in O(n) steps."
        ),
        "space_auxiliary": "O(1)",
        "space_why": (
            "Only two pointer references regardless of list length. "
            "HashSet of visited nodes would use O(n) but is unnecessary."
        ),
        "approach": (
            "Initialize slow and fast at head. Move slow 1 step and fast 2 steps per iteration. "
            "If slow == fast, cycle exists; if fast reaches null, no cycle."
        ),
    },
    "dsa-remove-nth-node": {
        "leetcode": 19,
        "difficulty": "Medium",
        "pattern": "Two pointers n-gap apart",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Fast pointer advances at most n steps ahead, then both move until fast reaches end. "
            "Single pass over the list."
        ),
        "space_auxiliary": "O(1)",
        "space_why": (
            "Dummy node plus slow/fast pointers — constant extra space. "
            "No recursion or auxiliary list copy."
        ),
        "approach": (
            "Dummy before head; advance fast n+1 steps ahead of slow. "
            "Move both until fast is null; slow.next is the node to remove — skip it."
        ),
    },
    "dsa-valid-parentheses": {
        "leetcode": 20,
        "difficulty": "Easy",
        "pattern": "Stack matching pairs",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Each character is pushed or popped at most once. "
            "Single left-to-right scan of the string length n."
        ),
        "space_auxiliary": "O(n)",
        "space_why": (
            "Stack can hold all opening brackets in the worst case (e.g., '((((('). "
            "No other auxiliary storage grows with input."
        ),
        "approach": (
            "Push opening brackets onto a stack. On closing bracket, pop and verify matching pair. "
            "Valid iff stack is empty after processing entire string."
        ),
    },
    "dsa-min-stack": {
        "leetcode": 155,
        "difficulty": "Medium",
        "pattern": "Auxiliary min tracking",
        "time_best": "O(1) per op",
        "time_average": "O(1) per op",
        "time_worst": "O(1) per op",
        "time_why": (
            "Push, pop, top, and getMin each perform constant work — one stack operation plus min comparison on push. "
            "No loops over existing elements."
        ),
        "space_auxiliary": "O(n)",
        "space_why": (
            "Storing (value, currentMin) pairs doubles metadata per element vs a plain stack. "
            "Separate min-stack variant also uses O(n) worst-case space."
        ),
        "approach": (
            "Push (value, min(value, currentMin)) tuples. "
            "Top returns val; getMin returns stored min; pop removes both together."
        ),
    },
    "dsa-daily-temperatures": {
        "leetcode": 739,
        "difficulty": "Medium",
        "pattern": "Monotonic decreasing stack",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Each index is pushed once and popped at most once when a warmer day is found. "
            "Amortized O(1) per day despite inner while loop."
        ),
        "space_auxiliary": "O(n)",
        "space_why": (
            "Stack holds indices waiting for a warmer day — up to n in a decreasing temperature sequence. "
            "Answer array is required output, not auxiliary."
        ),
        "approach": (
            "Monotonic decreasing stack of indices. For each day, pop indices with lower temps "
            "and set answer[popped] = i - popped; push current index."
        ),
    },
    "dsa-largest-rectangle": {
        "leetcode": 84,
        "difficulty": "Hard",
        "pattern": "Monotonic increasing stack",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Each bar index is pushed once and popped once when a shorter bar arrives. "
            "Sentinel height 0 at end flushes remaining stack in the same pass."
        ),
        "space_auxiliary": "O(n)",
        "space_why": (
            "Stack can contain all n indices in a monotonically increasing histogram. "
            "No other structures scale with n."
        ),
        "approach": (
            "Monotonic increasing stack of indices. On pop, compute area = height × width "
            "where width extends from new stack top to current index."
        ),
    },
    "dsa-max-depth-tree": {
        "leetcode": 104,
        "difficulty": "Easy",
        "pattern": "Tree DFS / BFS",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Every node is visited exactly once whether via DFS or BFS. "
            "Work per node is O(1) — compute child depths or increment level."
        ),
        "space_auxiliary": "O(h)",
        "space_why": (
            "Recursion stack depth equals tree height h (O(n) skewed, O(log n) balanced). "
            "BFS queue also holds up to O(w) nodes at the widest level."
        ),
        "approach": (
            "DFS: return 1 + max(left depth, right depth) with base case null → 0. "
            "BFS alternative: count levels while dequeuing each level."
        ),
    },
    "dsa-invert-tree": {
        "leetcode": 226,
        "difficulty": "Easy",
        "pattern": "Tree DFS swap children",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Each node is visited once to swap its children and recurse. "
            "Exactly n nodes in the tree."
        ),
        "space_auxiliary": "O(h)",
        "space_why": (
            "Recursive DFS uses call stack proportional to height. "
            "BFS queue variant uses O(w) space for the widest level."
        ),
        "approach": (
            "At each node, swap left and right child pointers, then recursively invert both subtrees. "
            "Return root after full traversal."
        ),
    },
    "dsa-same-tree": {
        "leetcode": 100,
        "difficulty": "Easy",
        "pattern": "Parallel tree DFS",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Compares corresponding nodes once; stops early on first mismatch. "
            "Worst case visits all nodes when trees are identical."
        ),
        "space_auxiliary": "O(h)",
        "space_why": (
            "Recursive calls stack to depth h of the smaller tree path. "
            "Iterative BFS uses O(w) queue space."
        ),
        "approach": (
            "Both null → true; one null or value mismatch → false. "
            "Else recurse on left-left and right-right pairs."
        ),
    },
    "dsa-lca-bst": {
        "leetcode": 235,
        "difficulty": "Medium",
        "pattern": "BST ordered walk",
        "time_best": "O(h)",
        "time_average": "O(h)",
        "time_worst": "O(n)",
        "time_why": (
            "Descend one level per iteration using BST ordering — h steps for balanced tree. "
            "Skewed BST degrades to O(n) height."
        ),
        "space_auxiliary": "O(1)",
        "space_why": (
            "Iterative walk uses only a current node pointer. "
            "No hash map, path list, or recursion stack."
        ),
        "approach": (
            "Walk from root: if both p and q are smaller, go left; if both larger, go right; "
            "else current node is the split point — the LCA."
        ),
    },
    "dsa-validate-bst": {
        "leetcode": 98,
        "difficulty": "Medium",
        "pattern": "DFS with min/max bounds",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Each node is visited once with constant-time bound checks. "
            "In-order traversal alternative also touches each node once."
        ),
        "space_auxiliary": "O(h)",
        "space_why": (
            "Recursion stack depth is tree height h. "
            "Bounds are passed as scalar parameters — no extra array."
        ),
        "approach": (
            "DFS with (min, max) allowed range per node. "
            "Node value must be strictly between bounds; recurse left with updated max, right with updated min."
        ),
    },
    "dsa-level-order": {
        "leetcode": 102,
        "difficulty": "Medium",
        "pattern": "BFS level-by-level",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Each node is enqueued and dequeued exactly once. "
            "Level-size inner loop processes all n nodes total."
        ),
        "space_auxiliary": "O(n)",
        "space_why": (
            "Queue holds up to the widest level — O(n/2) ≈ O(n) nodes in a complete binary tree bottom row. "
            "Result list is required output."
        ),
        "approach": (
            "BFS with queue: record queue size as current level width, dequeue all, collect values, "
            "enqueue children, append level to result."
        ),
    },
    "dsa-number-of-islands": {
        "leetcode": 200,
        "difficulty": "Medium",
        "pattern": "Grid DFS/BFS flood fill",
        "time_best": "O(rows × cols)",
        "time_average": "O(rows × cols)",
        "time_worst": "O(rows × cols)",
        "time_why": (
            "Each cell is visited at most once across all flood-fill calls. "
            "4-directional DFS/BFS from each unvisited '1' marks the entire component."
        ),
        "space_auxiliary": "O(rows × cols)",
        "space_why": (
            "DFS recursion stack can reach O(rows × cols) in a snake-shaped island. "
            "BFS queue similarly bounded by component size; in-place marking avoids separate visited set."
        ),
        "approach": (
            "Scan grid; on '1', increment count and DFS/BFS to mark entire connected component as visited. "
            "4-directional connectivity only."
        ),
    },
    "dsa-clone-graph": {
        "leetcode": 133,
        "difficulty": "Medium",
        "pattern": "BFS/DFS with old→new map",
        "time_best": "O(V + E)",
        "time_average": "O(V + E)",
        "time_worst": "O(V + E)",
        "time_why": (
            "Each vertex and edge in the adjacency list is processed once during BFS/DFS. "
            "Neighbor cloning and map lookups are O(1) average per edge."
        ),
        "space_auxiliary": "O(V)",
        "space_why": (
            "Dictionary maps every original node to its clone — V entries. "
            "BFS queue holds at most O(V) nodes; edge references stored in clone adjacency lists."
        ),
        "approach": (
            "BFS from start: create clone on first visit, store in map, enqueue. "
            "Wire clone neighbors using map lookups to avoid duplicate creation and cycles."
        ),
    },
    "dsa-course-schedule": {
        "leetcode": 207,
        "difficulty": "Medium",
        "pattern": "Topological sort (Kahn's BFS)",
        "time_best": "O(V + E)",
        "time_average": "O(V + E)",
        "time_worst": "O(V + E)",
        "time_why": (
            "Build adjacency list and indegrees in O(E), then each vertex and edge processed once in Kahn's BFS. "
            "DFS coloring alternative is also O(V + E)."
        ),
        "space_auxiliary": "O(V + E)",
        "space_why": (
            "Adjacency list stores E edges across V lists; indegree array is O(V). "
            "Queue holds up to O(V) zero-indegree nodes."
        ),
        "approach": (
            "Build graph from prerequisites; enqueue courses with indegree 0. "
            "Process queue, decrement neighbor indegrees; cycle exists if processed count < numCourses."
        ),
    },
    "dsa-rotting-oranges": {
        "leetcode": 994,
        "difficulty": "Medium",
        "pattern": "Multi-source BFS",
        "time_best": "O(rows × cols)",
        "time_average": "O(rows × cols)",
        "time_worst": "O(rows × cols)",
        "time_why": (
            "Each cell is enqueued at most once when it rots. "
            "Level-by-level BFS processes all R×C cells in worst case."
        ),
        "space_auxiliary": "O(rows × cols)",
        "space_why": (
            "BFS queue can hold up to all cells in one level (e.g., entire grid rotten simultaneously). "
            "Fresh count is O(1) extra."
        ),
        "approach": (
            "Enqueue all initially rotten oranges at minute 0. "
            "BFS level-by-level, rotting adjacent fresh cells; track minutes and remaining fresh count."
        ),
    },
    "dsa-word-ladder": {
        "leetcode": 127,
        "difficulty": "Hard",
        "pattern": "BFS shortest path on implicit graph",
        "time_best": "O(N × L²)",
        "time_average": "O(N × L²)",
        "time_worst": "O(N × L²)",
        "time_why": (
            "BFS visits each word once; for word length L and N words, trying 26 letters at each of L positions "
            "costs O(26 × L) = O(L) per word with hash set lookup."
        ),
        "space_auxiliary": "O(N × L)",
        "space_why": (
            "HashSet stores up to N words of length L. "
            "BFS queue holds a frontier of words — O(N) in worst case."
        ),
        "approach": (
            "BFS from beginWord; for each word, try all single-char mutations. "
            "If next is in wordList, enqueue and remove from set to avoid revisiting."
        ),
    },
    "dsa-kth-largest": {
        "leetcode": 215,
        "difficulty": "Medium",
        "pattern": "Min-heap of size k",
        "time_best": "O(n log k)",
        "time_average": "O(n log k)",
        "time_worst": "O(n log k)",
        "time_why": (
            "Process n elements; each heap insert/delete is O(log k) with heap size capped at k. "
            "Quickselect achieves O(n) average but O(n²) worst case."
        ),
        "space_auxiliary": "O(k)",
        "space_why": (
            "Min-heap holds exactly k elements after processing all nums. "
            "Quickselect uses O(1) extra but mutates the array."
        ),
        "approach": (
            "Maintain min-heap of size k. For each num, enqueue; if size > k, pop smallest. "
            "Heap root is the kth largest element."
        ),
    },
    "dsa-top-k-frequent": {
        "leetcode": 347,
        "difficulty": "Medium",
        "pattern": "Frequency map + min-heap",
        "time_best": "O(n log k)",
        "time_average": "O(n log k)",
        "time_worst": "O(n log k)",
        "time_why": (
            "O(n) to count frequencies, then O(u log k) for u unique elements with heap size k. "
            "Bucket sort by frequency achieves O(n) when range is bounded."
        ),
        "space_auxiliary": "O(n)",
        "space_why": (
            "Frequency map stores up to n distinct elements. "
            "Heap holds k entries; bucket sort uses O(n) buckets."
        ),
        "approach": (
            "Count frequencies in a dictionary. "
            "Use min-heap of size k keyed by frequency; return heap elements after processing all unique nums."
        ),
    },
    "dsa-find-median-stream": {
        "leetcode": 295,
        "difficulty": "Hard",
        "pattern": "Two heaps (max-left, min-right)",
        "time_best": "O(log n) add",
        "time_average": "O(log n) add",
        "time_worst": "O(log n) add",
        "time_why": (
            "Each AddNum performs at most two heap insert/delete operations, each O(log n). "
            "FindMedian is O(1) by peeking at heap tops."
        ),
        "space_auxiliary": "O(n)",
        "space_why": (
            "Both heaps together store all n inserted numbers split across two halves. "
            "No other structures grow with stream length."
        ),
        "approach": (
            "Max-heap for lower half, min-heap for upper half. "
            "After each insert, rebalance so sizes differ by at most 1 and all lower ≤ all upper."
        ),
    },
    "dsa-binary-search": {
        "leetcode": 704,
        "difficulty": "Easy",
        "pattern": "Classic binary search",
        "time_best": "O(log n)",
        "time_average": "O(log n)",
        "time_worst": "O(log n)",
        "time_why": (
            "Search space halves each iteration: n → n/2 → n/4 → … → 1. "
            "At most ⌊log₂ n⌋ + 1 comparisons regardless of target position."
        ),
        "space_auxiliary": "O(1)",
        "space_why": (
            "Only left, right, and mid index variables are used. "
            "Iterative implementation — no recursion stack."
        ),
        "approach": (
            "left=0, right=n-1; while left <= right, compute mid, compare nums[mid] to target, "
            "narrow to left or right half. Return -1 if not found."
        ),
    },
    "dsa-search-rotated": {
        "leetcode": 33,
        "difficulty": "Medium",
        "pattern": "Binary search on rotated array",
        "time_best": "O(log n)",
        "time_average": "O(log n)",
        "time_worst": "O(log n)",
        "time_why": (
            "One half is always sorted after rotation; binary search eliminates half each step. "
            "Same logarithmic reduction as classic binary search."
        ),
        "space_auxiliary": "O(1)",
        "space_why": (
            "Constant pointer variables only. "
            "No auxiliary array needed to identify the sorted half."
        ),
        "approach": (
            "Binary search: determine which half [l..mid] or [mid..r] is sorted. "
            "Check if target lies in the sorted range; adjust l or r accordingly."
        ),
    },
    "dsa-min-rotated": {
        "leetcode": 153,
        "difficulty": "Medium",
        "pattern": "Binary search for pivot",
        "time_best": "O(log n)",
        "time_average": "O(log n)",
        "time_worst": "O(log n)",
        "time_why": (
            "Compare mid with right to decide which half contains the minimum; halve search space each step. "
            "Loop runs while l < r — logarithmic iterations."
        ),
        "space_auxiliary": "O(1)",
        "space_why": (
            "Only l, r, mid pointers — no extra storage. "
            "Iterative binary search template."
        ),
        "approach": (
            "Binary search comparing nums[mid] vs nums[r]. "
            "If nums[mid] > nums[r], min is in right half (l = mid+1); else min is in left including mid (r = mid)."
        ),
    },
    "dsa-koko-bananas": {
        "leetcode": 875,
        "difficulty": "Medium",
        "pattern": "Binary search on answer",
        "time_best": "O(n log M)",
        "time_average": "O(n log M)",
        "time_worst": "O(n log M)",
        "time_why": (
            "Binary search over speed range [1, max(piles)] — log M iterations where M = max pile. "
            "Each feasibility check scans all n piles with O(1) ceil division per pile."
        ),
        "space_auxiliary": "O(1)",
        "space_why": (
            "Feasibility check uses a running sum scalar. "
            "No auxiliary array beyond input; lo/hi/best pointers are O(1)."
        ),
        "approach": (
            "Binary search eating speed k from 1 to max(piles). "
            "Feasible if sum of ceil(pile/k) over all piles ≤ h hours; minimize feasible k."
        ),
    },
    "dsa-climbing-stairs": {
        "leetcode": 70,
        "difficulty": "Easy",
        "pattern": "1D DP (Fibonacci)",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "Single loop from 3 to n computing dp[i] = dp[i-1] + dp[i-2]. "
            "Constant work per step — linear in n."
        ),
        "space_auxiliary": "O(1)",
        "space_why": (
            "Rolling two variables (prev1, prev2) replace the full dp array. "
            "No recursion stack or O(n) table needed."
        ),
        "approach": (
            "Ways to reach step i = ways(i-1) + ways(i-2). "
            "Base: 1 way for n=1, 2 for n=2; iterate with two rolling variables."
        ),
    },
    "dsa-house-robber": {
        "leetcode": 198,
        "difficulty": "Medium",
        "pattern": "1D DP take-or-skip",
        "time_best": "O(n)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "time_why": (
            "One pass over n houses; at each house compute max(rob current + skip prev, skip current). "
            "Constant transition work per element."
        ),
        "space_auxiliary": "O(1)",
        "space_why": (
            "Two rolling variables track best if robbing vs skipping previous house. "
            "Full dp[n] array is not required."
        ),
        "approach": (
            "dp[i] = max(dp[i-1], dp[i-2] + nums[i]) — cannot rob adjacent houses. "
            "Track 'take' and 'skip' as two scalars updated each iteration."
        ),
    },
    "dsa-coin-change": {
        "leetcode": 322,
        "difficulty": "Medium",
        "pattern": "Unbounded knapsack DP",
        "time_best": "O(amount × coins)",
        "time_average": "O(amount × coins)",
        "time_worst": "O(amount × coins)",
        "time_why": (
            "Nested loops: for each amount 1..target, try each coin denomination. "
            "Total iterations = amount × number of coin types."
        ),
        "space_auxiliary": "O(amount)",
        "space_why": (
            "1D dp array of size amount+1 stores minimum coins for each sub-amount. "
            "Coin list is input, not auxiliary."
        ),
        "approach": (
            "dp[0]=0, dp[a]=min(dp[a-c]+1) for each coin c ≤ a. "
            "Initialize unreachable amounts to infinity; return dp[amount] or -1."
        ),
    },
    "dsa-lis": {
        "leetcode": 300,
        "difficulty": "Medium",
        "pattern": "Patience sorting + binary search",
        "time_best": "O(n log n)",
        "time_average": "O(n log n)",
        "time_worst": "O(n log n)",
        "time_why": (
            "For each of n elements, binary search on tails array of length ≤ n takes O(log n). "
            "DP O(n²) alternative is simpler but slower."
        ),
        "space_auxiliary": "O(n)",
        "space_why": (
            "tails array holds at most n elements — one per potential LIS length. "
            "Binary search uses O(1) extra beyond tails."
        ),
        "approach": (
            "Maintain tails[i] = smallest tail of an increasing subsequence of length i+1. "
            "Binary search position for each num; replace or append to tails."
        ),
    },
    "dsa-lcs": {
        "leetcode": 1143,
        "difficulty": "Medium",
        "pattern": "2D DP on two strings",
        "time_best": "O(m × n)",
        "time_average": "O(m × n)",
        "time_worst": "O(m × n)",
        "time_why": (
            "Fill (m+1) × (n+1) DP table — each cell computed in O(1) from neighbors. "
            "Both string lengths m and n contribute equally."
        ),
        "space_auxiliary": "O(m × n)",
        "space_why": (
            "Full 2D dp table of size (m+1)(n+1) in standard solution. "
            "Space-optimized 1D row reduces to O(min(m, n)) if needed."
        ),
        "approach": (
            "dp[i,j] = dp[i-1,j-1]+1 if chars match, else max(dp[i-1,j], dp[i,j-1]). "
            "Answer is dp[m,n]."
        ),
    },
    "dsa-word-break": {
        "leetcode": 139,
        "difficulty": "Medium",
        "pattern": "1D DP prefix segmentation",
        "time_best": "O(n² × L)",
        "time_average": "O(n² × L)",
        "time_worst": "O(n² × L)",
        "time_why": (
            "For each of n prefix positions, try up to n split points; "
            "dictionary lookup is O(L) per word length L with hash set."
        ),
        "space_auxiliary": "O(n + W)",
        "space_why": (
            "dp array of size n+1 plus HashSet of W dictionary words. "
            "Substring checks can be O(L) each without trie optimization."
        ),
        "approach": (
            "dp[i] = true if any prefix s[0..i) can be segmented. "
            "For each j < i, if dp[j] and s[j..i) is in dictionary, set dp[i] = true."
        ),
    },
    "dsa-subsets": {
        "leetcode": 78,
        "difficulty": "Medium",
        "pattern": "Backtracking include/exclude",
        "time_best": "O(n × 2ⁿ)",
        "time_average": "O(n × 2ⁿ)",
        "time_worst": "O(n × 2ⁿ)",
        "time_why": (
            "2ⁿ subsets exist; copying each subset of average size n/2 to the result dominates. "
            "Recursion tree has 2ⁿ leaves."
        ),
        "space_auxiliary": "O(n)",
        "space_why": (
            "Recursion depth is n with one mutable path list of size ≤ n. "
            "Output storage is required, not auxiliary."
        ),
        "approach": (
            "At each index, branch: include nums[i] and recurse, or exclude and recurse. "
            "Copy path to result when index reaches n."
        ),
    },
    "dsa-combination-sum": {
        "leetcode": 39,
        "difficulty": "Medium",
        "pattern": "Backtracking with reuse",
        "time_best": "O(2^target/min)",
        "time_average": "O(2^target/min)",
        "time_worst": "O(2^target/min)",
        "time_why": (
            "Worst case explores exponentially many combinations when candidates are small (e.g., many 1s). "
            "Sorting and pruning reduce practical runtime but not worst-case Big-O."
        ),
        "space_auxiliary": "O(target/min)",
        "space_why": (
            "Recursion depth bounded by target/min(candidate) when reusing smallest coin. "
            "Path list holds current combination being built."
        ),
        "approach": (
            "Sort candidates; backtrack from start index, add candidate, recurse same index (reuse allowed). "
            "Prune when remain < 0; copy path when remain == 0."
        ),
    },
    "dsa-permutations": {
        "leetcode": 46,
        "difficulty": "Medium",
        "pattern": "Backtracking with used array",
        "time_best": "O(n × n!)",
        "time_average": "O(n × n!)",
        "time_worst": "O(n × n!)",
        "time_why": (
            "n! permutations each of length n must be generated and copied to result. "
            "Recursion tree has n! leaves with n choices per level on average."
        ),
        "space_auxiliary": "O(n)",
        "space_why": (
            "used[] boolean array of size n plus path list of size n. "
            "Recursion stack depth is n."
        ),
        "approach": (
            "Backtrack: at each step pick an unused element, mark used, recurse, undo. "
            "When path length equals n, copy to result."
        ),
    },
}


def _extract_problem(existing_explanation: str, meta: dict) -> str:
    """Pull **Problem:** text from an existing explanation, or fall back to approach summary."""
    if existing_explanation:
        match = re.search(
            r"\*\*Problem:\*\*\s*(.+?)(?:\n\n|\*\*Approach|\*\*Complexity|\*\*Pattern|$)",
            existing_explanation,
            re.DOTALL,
        )
        if match:
            return re.sub(r"\s+", " ", match.group(1).strip())
    approach = meta.get("approach", "")
    if approach:
        first_sentence = approach.split(".")[0].strip()
        return first_sentence + "." if first_sentence else approach
    return "See approach below."


def _build_explanation(problem: str, meta: dict) -> str:
    """Build interview-sheet style explanation from complexity metadata."""
    difficulty = meta["difficulty"]
    leetcode = meta.get("leetcode")
    diff_line = f"**Difficulty:** {difficulty}"
    if leetcode is not None:
        diff_line += f" | LeetCode #{leetcode}"

    return (
        f"**Problem:** {problem}\n"
        f"**Pattern:** {meta['pattern']}\n"
        f"{diff_line}\n\n"
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


def _merge_key_points(existing: list[str], meta: dict) -> list[str]:
    """Keep existing key points; append complexity summaries if not already present."""
    merged = list(existing) if existing else []
    has_time = any("O(" in kp or "time" in kp.lower() for kp in merged)
    has_space = any("O(" in kp or "space" in kp.lower() for kp in merged)
    if not has_time:
        merged.append(f"Time: {meta['time_worst']} worst ({meta['time_best']} best)")
    if not has_space:
        merged.append(f"Space: {meta['space_auxiliary']} auxiliary")
    return merged


def apply_dsa_complexity(detailed: dict) -> None:
    """Merge enhanced complexity explanations into the DSA detailed dict for all 50 ids."""
    from data.dsa_detailed import DSA_DETAILED

    for problem_id, meta in COMPLEXITY_META.items():
        existing = detailed.get(problem_id) or DSA_DETAILED.get(problem_id, {})
        problem = _extract_problem(existing.get("explanation", ""), meta)
        enhanced = _build_explanation(problem, meta)
        key_points = _merge_key_points(existing.get("key_points", []), meta)

        updated = dict(existing)
        updated["explanation"] = enhanced
        updated["key_points"] = key_points
        detailed[problem_id] = updated
