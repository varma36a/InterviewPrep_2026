"""Dedicated DSA section — top 50 coding interview questions by topic."""

from data.interview_content import InterviewItem, Phase, Section


def _q(
    id: str,
    question: str,
    stub: str = "",
    points: list[str] | None = None,
) -> InterviewItem:
    return InterviewItem(
        id=id,
        question=question,
        explanation="See detailed explanation.",
        code=stub,
        language="csharp",
        key_points=points or [],
    )


DSA_SECTION = Section(
    id="dsa",
    title="DSA Coding",
    emoji="🧮",
    color="#059669",
    subtitle="Top 50 DSA problems — topic-wise with C# solutions and detailed time/space complexity",
    phases=[
        Phase("arrays", "Arrays, Hashing & Strings", [
            _q("dsa-two-sum", "Two Sum — find two indices that add to target",
               "// nums = [2,7,11,15], target = 9 → [0,1]",
               ["Hash map O(n)", "Store complement", "Classic warm-up"]),
            _q("dsa-contains-duplicate", "Contains Duplicate — detect any repeated value",
               "// [1,2,3,1] → true",
               ["HashSet O(n)", "Sort alternative O(n log n)"]),
            _q("dsa-product-except-self", "Product of Array Except Self — no division",
               "// [1,2,3,4] → [24,12,8,6]",
               ["Prefix + suffix", "O(n) time O(1) extra"]),
            _q("dsa-max-subarray", "Maximum Subarray — Kadane's algorithm",
               "// [-2,1,-3,4,-1,2,1,-5,4] → 6",
               ["Kadane O(n)", "DP / greedy"]),
            _q("dsa-merge-intervals", "Merge Intervals — overlapping ranges",
               "// [[1,3],[2,6],[8,10]] → [[1,6],[8,10]]",
               ["Sort by start", "Greedy merge"]),
            _q("dsa-group-anagrams", "Group Anagrams — bucket by signature",
               "// [\"eat\",\"tea\",\"tan\"] → groups",
               ["Sort key or char count", "Dictionary of lists"]),
            _q("dsa-longest-consecutive", "Longest Consecutive Sequence — O(n)",
               "// [100,4,200,1,3,2] → 4",
               ["HashSet lookup", "Only start of streak"]),
        ]),
        Phase("pointers-window", "Two Pointers & Sliding Window", [
            _q("dsa-valid-palindrome", "Valid Palindrome — alphanumeric, ignore case",
               "// \"A man, a plan...\" → true",
               ["Two pointers", "Skip non-alnum"]),
            _q("dsa-two-sum-ii", "Two Sum II — sorted array, one solution",
               "// [2,7,11,15], target=9 → [1,2]",
               ["Left/right pointers", "O(n) no hash map"]),
            _q("dsa-container-water", "Container With Most Water — max area",
               "// [1,8,6,2,5,4,8,3,7] → 49",
               ["Move shorter line", "Greedy two pointers"]),
            _q("dsa-trapping-rain", "Trapping Rain Water — elevation map",
               "// [0,1,0,2,1,0,1,3,2,1,2,1] → 6",
               ["Two pointers or prefix max", "Classic hard medium"]),
            _q("dsa-longest-substring", "Longest Substring Without Repeating Characters",
               "// \"abcabcbb\" → 3",
               ["Sliding window + HashSet", "Shrink on duplicate"]),
            _q("dsa-min-window-substring", "Minimum Window Substring — contain all chars of t",
               "// s=\"ADOBECODEBANC\", t=\"ABC\" → \"BANC\"",
               ["Expand/shrink window", "Frequency map"]),
            _q("dsa-sliding-window-max", "Sliding Window Maximum — deque monotonic",
               "// k=3 window max in array",
               ["Monotonic deque", "Amortized O(n)"]),
            _q("dsa-max-consecutive-ones", "Max Consecutive Ones III — flip at most k zeros",
               "// nums=[1,1,1,0,0,0,1,1,1,1,0], k=2 → 6",
               ["Sliding window on zeros", "Longest window with ≤k zeros"]),
        ]),
        Phase("linked-list", "Linked Lists", [
            _q("dsa-reverse-linked-list", "Reverse Linked List — iterative and recursive",
               "// 1→2→3→null → 3→2→1",
               ["Iterative three pointers", "Recursive base case"]),
            _q("dsa-merge-two-lists", "Merge Two Sorted Lists",
               "// 1→2→4 + 1→3→4 → 1→1→2→3→4→4",
               ["Dummy head", "Compare and advance"]),
            _q("dsa-linked-list-cycle", "Linked List Cycle — Floyd's tortoise & hare",
               "// detect cycle in O(1) space",
               ["Fast/slow pointers", "Find cycle start optional"]),
            _q("dsa-remove-nth-node", "Remove Nth Node From End of List",
               "// head=[1,2,3,4,5], n=2 → [1,2,3,5]",
               ["Two pointers n apart", "Dummy node edge case"]),
        ]),
        Phase("stack-queue", "Stack, Queue & Monotonic Stack", [
            _q("dsa-valid-parentheses", "Valid Parentheses — (), {}, []",
               "// \"()[]{}\" → true",
               ["Stack matching pairs", "O(n) time"]),
            _q("dsa-min-stack", "Min Stack — O(1) getMin",
               "// push/pop/top/getMin all O(1)",
               ["Auxiliary stack or pair store"]),
            _q("dsa-daily-temperatures", "Daily Temperatures — days until warmer",
               "// [73,74,75,71,69,72,76,73]",
               ["Monotonic decreasing stack", "Store indices"]),
            _q("dsa-largest-rectangle", "Largest Rectangle in Histogram",
               "// [2,1,5,6,2,3] → 10",
               ["Monotonic stack", "Expand width at pop"]),
        ]),
        Phase("trees", "Trees & Binary Search Trees", [
            _q("dsa-max-depth-tree", "Maximum Depth of Binary Tree",
               "// recursive or BFS level count",
               ["DFS O(n)", "Base: null → 0"]),
            _q("dsa-invert-tree", "Invert Binary Tree — mirror left/right",
               "// swap children recursively",
               ["Pre-order swap", "BFS level swap"]),
            _q("dsa-same-tree", "Same Tree — structural equality",
               "// compare nodes recursively",
               ["DFS pairwise", "Null handling"]),
            _q("dsa-lca-bst", "Lowest Common Ancestor of BST",
               "// use BST ordering property",
               ["O(h) walk from root", "Split when p and q diverge"]),
            _q("dsa-validate-bst", "Validate Binary Search Tree",
               "// strict range per node",
               ["In-order or min/max bounds", "long.MinValue trap"]),
            _q("dsa-level-order", "Binary Tree Level Order Traversal",
               "// BFS queue by level",
               ["Queue + level size", "Zigzag variant common follow-up"]),
        ]),
        Phase("graphs", "Graphs, BFS & DFS", [
            _q("dsa-number-of-islands", "Number of Islands — 2D grid '1' land",
               "// grid DFS/BFS count components",
               ["4-direction flood fill", "Mark visited in-place"]),
            _q("dsa-clone-graph", "Clone Graph — deep copy adjacency list",
               "// Dictionary old→new node",
               ["BFS/DFS + hash map", "Avoid infinite loop"]),
            _q("dsa-course-schedule", "Course Schedule — detect cycle (topological sort)",
               "// prerequisites → can finish all?",
               ["Kahn BFS or DFS colors", "Cycle = impossible"]),
            _q("dsa-rotting-oranges", "Rotting Oranges — multi-source BFS",
               "// minutes until all rotten",
               ["Queue all rotten at t=0", "Track fresh count"]),
            _q("dsa-word-ladder", "Word Ladder — shortest transformation sequence",
               "// beginWord → endWord one char at a time",
               ["BFS on word graph", "Wildcard bucket optimization"]),
        ]),
        Phase("heap-search", "Heaps & Binary Search", [
            _q("dsa-kth-largest", "Kth Largest Element in Array",
               "// quickselect or min-heap size k",
               ["Min-heap O(n log k)", "Quickselect average O(n)"]),
            _q("dsa-top-k-frequent", "Top K Frequent Elements",
               "// bucket sort or heap on frequency",
               ["Dictionary + heap", "O(n log k)"]),
            _q("dsa-find-median-stream", "Find Median from Data Stream",
               "// two heaps: max-left, min-right",
               ["Balance heap sizes", "O(log n) add"]),
            _q("dsa-binary-search", "Binary Search — classic sorted array",
               "// target in O(log n)",
               ["left/right inclusive", "mid = left + (right-left)/2"]),
            _q("dsa-search-rotated", "Search in Rotated Sorted Array",
               "// [4,5,6,7,0,1,2] find target",
               ["Which half sorted?", "Adjust bounds"]),
            _q("dsa-min-rotated", "Find Minimum in Rotated Sorted Array",
               "// compare mid with right",
               ["Binary search on pivot", "No duplicates variant"]),
            _q("dsa-koko-bananas", "Koko Eating Bananas — binary search on answer",
               "// min eating speed to finish in h hours",
               ["Search speed space", "Feasibility check"]),
        ]),
        Phase("dp", "Dynamic Programming", [
            _q("dsa-climbing-stairs", "Climbing Stairs — 1 or 2 steps to top",
               "// n=3 → 3 ways",
               ["Fibonacci DP", "O(1) space"]),
            _q("dsa-house-robber", "House Robber — no adjacent houses",
               "// max money linear street",
               ["dp[i] = max(skip, take)", "Two variable rolling"]),
            _q("dsa-coin-change", "Coin Change — minimum coins for amount",
               "// coins=[1,2,5], amount=11 → 3",
               ["Unbounded knapsack DP", "Initialize infinity"]),
            _q("dsa-lis", "Longest Increasing Subsequence",
               "// [10,9,2,5,3,7,101,18] → 4",
               ["DP O(n²) or patience O(n log n)", "Binary search tails"]),
            _q("dsa-lcs", "Longest Common Subsequence — two strings",
               "// \"abcde\", \"ace\" → 3",
               ["2D DP table", "Backtrack for string"]),
            _q("dsa-word-break", "Word Break — segment string with dictionary",
               "// \"leetcode\", dict → true",
               ["dp[i] = prefix breakable", "Try all word lengths"]),
        ]),
        Phase("backtracking", "Backtracking & Greedy", [
            _q("dsa-subsets", "Subsets — all subsets (power set)",
               "// [1,2,3] → 8 subsets",
               ["Include/exclude recursion", "Or iterative bitmask"]),
            _q("dsa-combination-sum", "Combination Sum — reuse candidates",
               "// candidates=[2,3,6,7], target=7",
               ["Backtrack + prune", "Sort to skip duplicates"]),
            _q("dsa-permutations", "Permutations — all orderings",
               "// [1,2,3] → 6 permutations",
               ["Swap or used[] array", "Backtracking classic"]),
        ]),
    ],
)


def apply_dsa_section(sections: dict, detailed: dict) -> None:
    """Register DSA section, topic complexity guides, and merge detailed solutions."""
    from dataclasses import replace

    from data.dsa_complexity import TOPIC_GUIDES, apply_dsa_complexity
    from data.dsa_detailed import DSA_DETAILED

    detailed.update(DSA_DETAILED)
    apply_dsa_complexity(detailed)

    phases_with_guides: list[Phase] = []
    for phase in DSA_SECTION.phases:
        guide = TOPIC_GUIDES.get(phase.id)
        items = list(phase.items)
        if guide:
            guide_id = f"dsa-guide-{phase.id}"
            detailed[guide_id] = {
                "explanation": guide["explanation"],
                "key_points": guide["key_points"],
            }
            guide_item = InterviewItem(
                id=guide_id,
                question=f"📊 {guide['title']} — Time & Space Complexity Guide",
                explanation=guide["explanation"],
                code="",
                language="text",
                key_points=guide["key_points"],
            )
            items = [guide_item, *items]
        phases_with_guides.append(Phase(phase.id, phase.label, items))

    sections["dsa"] = replace(DSA_SECTION, phases=phases_with_guides)
