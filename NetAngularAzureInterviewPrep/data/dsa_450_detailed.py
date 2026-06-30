"""Love Babbar 450 detailed explanations — auto-generated."""

DSA_450_DETAILED: dict[str, dict] = {
    "dsa-guide-array": {
        'explanation': "Array problems dominate interviews. **Random access is O(1)** but insert/delete in middle is **O(n)**. Most optimal solutions use **hash maps** (O(n) time, O(n) space), **two pointers** (O(n), O(1)), or **prefix sums** for range queries.\n\n**Key patterns:** complement lookup, frequency counting, Kadane for subarrays, Dutch flag for 3-way partition, and sort-then-scan when order unlocks greedy or two-pointer moves.",
        'key_points': ['Hash map: O(n) time average', 'Two pointers: O(n) time O(1) space', 'Kadane: O(n) max subarray', 'Sort: O(n log n) unlocks many patterns'],
    },
    "dsa-450-array-001-reverse-the-array": {
        'explanation': "**Problem:** Reverse the array\n**Pattern:** In-place reversal / rotation\n**Difficulty:** Medium\n\n**Approach:** Two pointers swap from both ends, or reverse subarrays for rotation.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element moved once during reverse or rotate.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place two-pointer swap or triple-reversal trick.",
        'key_points': ['Pattern: In-place reversal / rotation', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-002-find-the-maximum-and-minimum-element": {
        'explanation': "**Problem:** Find the maximum and minimum element in an array\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-003-find-the-kth-max-and-min-element-of": {
        'explanation': "**Problem:** Find the \"Kth\" max and min element of an array\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-004-given-an-array-which-consists-of-onl": {
        'explanation': "**Problem:** Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo\n**Pattern:** Dutch national flag / counting\n**Difficulty:** Medium\n\n**Approach:** Use low/mid/high pointers or count 0s/1s/2s then rewrite array.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Three-way partition or count buckets in linear time.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place three-pointer partition.",
        'key_points': ['Pattern: Dutch national flag / counting', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-005-move-all-the-negative-elements-to-on": {
        'explanation': "**Problem:** Move all the negative elements to one side of the array\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-006-find-the-union-and-intersection-of-t": {
        'explanation': "**Problem:** Find the Union and Intersection of the two sorted arrays.\n**Pattern:** Binary search\n**Difficulty:** Medium\n\n**Approach:** Maintain left/right bounds; compare mid and discard half.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(log n) |\n| Worst | O(log n) |\n\n**Why:** Halve search space each iteration on sorted/monotonic data.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Iterative binary search uses constant pointers.",
        'key_points': ['Pattern: Binary search', 'Time: O(log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-007-write-a-program-to-cyclically-rotate": {
        'explanation': "**Problem:** Write a program to cyclically rotate an array by one.\n**Pattern:** In-place reversal / rotation\n**Difficulty:** Medium\n\n**Approach:** Two pointers swap from both ends, or reverse subarrays for rotation.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element moved once during reverse or rotate.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place two-pointer swap or triple-reversal trick.",
        'key_points': ['Pattern: In-place reversal / rotation', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-008-find-largest-sum-contiguous-subarray": {
        'explanation': "**Problem:** find Largest sum contiguous Subarray [V. IMP]\n**Pattern:** Kadane's algorithm (DP/greedy)\n**Difficulty:** Hard\n\n**Approach:** Extend subarray or restart at current index when sum goes negative.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** One pass tracking running max ending here and global max.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Only scalar variables for current/global max.",
        'key_points': ["Pattern: Kadane's algorithm (DP/greedy)", 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-009-minimise-the-maximum-difference-betw": {
        'explanation': "**Problem:** Minimise the maximum difference between heights [V.IMP]\n**Pattern:** Tree DFS aggregation\n**Difficulty:** Hard\n\n**Approach:** Recurse children; combine left/right results at parent for global optimum.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single post-order pass computes answer at each node once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion depth equals tree height.",
        'key_points': ['Pattern: Tree DFS aggregation', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-array-010-minimum-no-of-jumps-to-reach-end-of": {
        'explanation': "**Problem:** Minimum no. of Jumps to reach end of an array\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-011-find-duplicate-in-an-array-of-n-1-in": {
        'explanation': "**Problem:** find duplicate in an array of N+1 Integers\n**Pattern:** Hash map / frequency count\n**Difficulty:** Medium\n\n**Approach:** Count occurrences in dictionary; answer from frequencies.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single pass with O(1) average map operations.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Map stores up to n distinct keys.",
        'key_points': ['Pattern: Hash map / frequency count', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-array-012-merge-2-sorted-arrays-without-using": {
        'explanation': "**Problem:** Merge 2 sorted arrays without using Extra space.\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-013-kadane-s-algo-v-v-v-v-v-imp": {
        'explanation': "**Problem:** Kadane's Algo [V.V.V.V.V IMP]\n**Pattern:** Kadane's algorithm (DP/greedy)\n**Difficulty:** Hard\n\n**Approach:** Extend subarray or restart at current index when sum goes negative.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** One pass tracking running max ending here and global max.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Only scalar variables for current/global max.",
        'key_points': ["Pattern: Kadane's algorithm (DP/greedy)", 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-014-merge-intervals": {
        'explanation': "**Problem:** Merge Intervals\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-015-next-permutation": {
        'explanation': "**Problem:** Next Permutation\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Choose/explore/unchoose; prune invalid branches early.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Exponential search tree; permutations n!, subsets 2^n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth n plus path/used array.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-array-016-count-inversion": {
        'explanation': "**Problem:** Count Inversion\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-017-best-time-to-buy-and-sell-stock": {
        'explanation': "**Problem:** Best time to buy and Sell stock\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-018-find-all-pairs-on-integer-array-whos": {
        'explanation': "**Problem:** find all pairs on integer array whose sum is equal to given number\n**Pattern:** Hash map one-pass\n**Difficulty:** Medium\n\n**Approach:** Scan array; for each value check if (target - value) exists in map.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single pass with O(1) average hash lookups for complement.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Hash map stores up to n elements.",
        'key_points': ['Pattern: Hash map one-pass', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-array-019-find-common-elements-in-3-sorted-arr": {
        'explanation': "**Problem:** find common elements In 3 sorted arrays\n**Pattern:** Binary search\n**Difficulty:** Medium\n\n**Approach:** Maintain left/right bounds; compare mid and discard half.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(log n) |\n| Worst | O(log n) |\n\n**Why:** Halve search space each iteration on sorted/monotonic data.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Iterative binary search uses constant pointers.",
        'key_points': ['Pattern: Binary search', 'Time: O(log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-020-rearrange-the-array-in-alternating-p": {
        'explanation': "**Problem:** Rearrange the array in alternating positive and negative items with O(1) extra space\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-021-find-if-there-is-any-subarray-with-s": {
        'explanation': "**Problem:** Find if there is any subarray with sum equal to 0\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-022-find-factorial-of-a-large-number": {
        'explanation': "**Problem:** Find factorial of a large number\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-023-find-maximum-product-subarray": {
        'explanation': "**Problem:** find maximum product subarray\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-024-find-longest-coinsecutive-subsequenc": {
        'explanation': "**Problem:** Find longest coinsecutive subsequence\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-025-given-an-array-of-size-n-and-a-numbe": {
        'explanation': "**Problem:** Given an array of size n and a number k, fin all elements that appear more than \" n/k \" times.\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-026-maximum-profit-by-buying-and-selling": {
        'explanation': "**Problem:** Maximum profit by buying and selling a share atmost twice\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-027-find-whether-an-array-is-a-subset-of": {
        'explanation': "**Problem:** Find whether an array is a subset of another array\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Choose/explore/unchoose; prune invalid branches early.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Exponential search tree; permutations n!, subsets 2^n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth n plus path/used array.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-array-028-find-the-triplet-that-sum-to-a-given": {
        'explanation': "**Problem:** Find the triplet that sum to a given value\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-029-trapping-rain-water-problem": {
        'explanation': "**Problem:** Trapping Rain water problem\n**Pattern:** Two pointers\n**Difficulty:** Medium\n\n**Approach:** Place pointers at ends or both at start; move based on comparison/greedy rule.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Pointers move monotonically across array/string once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Only index pointers and scalar trackers.",
        'key_points': ['Pattern: Two pointers', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-030-chocolate-distribution-problem": {
        'explanation': "**Problem:** Chocolate Distribution problem\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-031-smallest-subarray-with-sum-greater-t": {
        'explanation': "**Problem:** Smallest Subarray with sum greater than a given value\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-032-three-way-partitioning-of-an-array-a": {
        'explanation': "**Problem:** Three way partitioning of an array around a given value\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-033-minimum-swaps-required-bring-element": {
        'explanation': "**Problem:** Minimum swaps required bring elements less equal K together\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-034-minimum-no-of-operations-required-to": {
        'explanation': "**Problem:** Minimum no. of operations required to make an array palindrome\n**Pattern:** Two pointers\n**Difficulty:** Medium\n\n**Approach:** Place pointers at ends or both at start; move based on comparison/greedy rule.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Pointers move monotonically across array/string once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Only index pointers and scalar trackers.",
        'key_points': ['Pattern: Two pointers', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-035-median-of-2-sorted-arrays-of-equal-s": {
        'explanation': "**Problem:** Median of 2 sorted arrays of equal size\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-array-036-median-of-2-sorted-arrays-of-differe": {
        'explanation': "**Problem:** Median of 2 sorted arrays of different size\n**Pattern:** Array scan / hash / two pointers\n**Difficulty:** Medium\n\n**Approach:** Standard Array approach: identify brute force, then optimize using array scan / hash / two pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n\u00b2) |\n\n**Why:** Typical array problems: one pass O(n) or nested loops O(n\u00b2) for pairs.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Often in-place; hash-based solutions use O(n) extra.",
        'key_points': ['Pattern: Array scan / hash / two pointers', 'Time: O(n²) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-guide-matrix": {
        'explanation': "Matrix problems reduce to **O(rows \u00d7 cols)** traversal unless binary search on sorted matrix (**O(log(rows\u00d7cols))**). Use **layer-by-layer spiral**, **in-place row/col markers** for zero matrix, or **transpose + reverse** for rotation.\n\nSpace is usually **O(1)** when transforming in-place; BFS on matrix uses **O(rows\u00d7cols)** queue worst case.",
        'key_points': ['Full scan: O(rows × cols)', 'Sorted matrix search: O(log n)', 'In-place rotation: O(1) extra', 'BFS flood: queue up to all cells'],
    },
    "dsa-450-matrix-001-spiral-traversal-on-a-matrix": {
        'explanation': "**Problem:** Spiral traversal on a Matrix\n**Pattern:** Matrix traversal / in-place transform\n**Difficulty:** Medium\n\n**Approach:** Traverse layers or use first row/col as zero flags.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(rows \u00d7 cols) |\n| Average | O(rows \u00d7 cols) |\n| Worst | O(rows \u00d7 cols) |\n\n**Why:** Each cell read/written constant times.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place layer rotation or marker row/col.",
        'key_points': ['Pattern: Matrix traversal / in-place transform', 'Time: O(rows × cols) worst (O(rows × cols) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-matrix-002-search-an-element-in-a-matriix": {
        'explanation': "**Problem:** Search an element in a matriix\n**Pattern:** Matrix traversal\n**Difficulty:** Medium\n\n**Approach:** Standard Matrix approach: identify brute force, then optimize using matrix traversal typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(rows \u00d7 cols) |\n| Average | O(rows \u00d7 cols) |\n| Worst | O(rows \u00d7 cols) |\n\n**Why:** Visit each cell at least once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place row/col marking when possible.",
        'key_points': ['Pattern: Matrix traversal', 'Time: O(rows × cols) worst (O(rows × cols) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-matrix-003-find-median-in-a-row-wise-sorted-mat": {
        'explanation': "**Problem:** Find median in a row wise sorted matrix\n**Pattern:** Matrix traversal\n**Difficulty:** Medium\n\n**Approach:** Standard Matrix approach: identify brute force, then optimize using matrix traversal typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(rows \u00d7 cols) |\n| Average | O(rows \u00d7 cols) |\n| Worst | O(rows \u00d7 cols) |\n\n**Why:** Visit each cell at least once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place row/col marking when possible.",
        'key_points': ['Pattern: Matrix traversal', 'Time: O(rows × cols) worst (O(rows × cols) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-matrix-004-find-row-with-maximum-no-of-1-s": {
        'explanation': "**Problem:** Find row with maximum no. of 1's\n**Pattern:** Matrix traversal\n**Difficulty:** Medium\n\n**Approach:** Standard Matrix approach: identify brute force, then optimize using matrix traversal typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(rows \u00d7 cols) |\n| Average | O(rows \u00d7 cols) |\n| Worst | O(rows \u00d7 cols) |\n\n**Why:** Visit each cell at least once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place row/col marking when possible.",
        'key_points': ['Pattern: Matrix traversal', 'Time: O(rows × cols) worst (O(rows × cols) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-matrix-005-print-elements-in-sorted-order-using": {
        'explanation': "**Problem:** Print elements in sorted order using row-column wise sorted matrix\n**Pattern:** Matrix traversal\n**Difficulty:** Medium\n\n**Approach:** Standard Matrix approach: identify brute force, then optimize using matrix traversal typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(rows \u00d7 cols) |\n| Average | O(rows \u00d7 cols) |\n| Worst | O(rows \u00d7 cols) |\n\n**Why:** Visit each cell at least once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place row/col marking when possible.",
        'key_points': ['Pattern: Matrix traversal', 'Time: O(rows × cols) worst (O(rows × cols) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-matrix-006-maximum-size-rectangle": {
        'explanation': "**Problem:** Maximum size rectangle\n**Pattern:** Matrix traversal\n**Difficulty:** Medium\n\n**Approach:** Standard Matrix approach: identify brute force, then optimize using matrix traversal typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(rows \u00d7 cols) |\n| Average | O(rows \u00d7 cols) |\n| Worst | O(rows \u00d7 cols) |\n\n**Why:** Visit each cell at least once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place row/col marking when possible.",
        'key_points': ['Pattern: Matrix traversal', 'Time: O(rows × cols) worst (O(rows × cols) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-matrix-007-find-a-specific-pair-in-matrix": {
        'explanation': "**Problem:** Find a specific pair in matrix\n**Pattern:** Matrix traversal\n**Difficulty:** Medium\n\n**Approach:** Standard Matrix approach: identify brute force, then optimize using matrix traversal typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(rows \u00d7 cols) |\n| Average | O(rows \u00d7 cols) |\n| Worst | O(rows \u00d7 cols) |\n\n**Why:** Visit each cell at least once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place row/col marking when possible.",
        'key_points': ['Pattern: Matrix traversal', 'Time: O(rows × cols) worst (O(rows × cols) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-matrix-008-rotate-matrix-by-90-degrees": {
        'explanation': "**Problem:** Rotate matrix by 90 degrees\n**Pattern:** Matrix traversal / in-place transform\n**Difficulty:** Medium\n\n**Approach:** Traverse layers or use first row/col as zero flags.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(rows \u00d7 cols) |\n| Average | O(rows \u00d7 cols) |\n| Worst | O(rows \u00d7 cols) |\n\n**Why:** Each cell read/written constant times.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place layer rotation or marker row/col.",
        'key_points': ['Pattern: Matrix traversal / in-place transform', 'Time: O(rows × cols) worst (O(rows × cols) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-matrix-009-kth-smallest-element-in-a-row-cpumn": {
        'explanation': "**Problem:** Kth smallest element in a row-cpumn wise sorted matrix\n**Pattern:** Heap / priority queue\n**Difficulty:** Medium\n\n**Approach:** Min-heap of size k for kth largest; balance two heaps for median.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log k) |\n| Average | O(n log k) |\n| Worst | O(n log k) |\n\n**Why:** Maintain size-k heap: n inserts each O(log k).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(k) |\n\n**Why:** Heap stores k elements (or two heaps for median).",
        'key_points': ['Pattern: Heap / priority queue', 'Time: O(n log k) worst (O(n log k) best)', 'Space: O(k) auxiliary'],
    },
    "dsa-450-matrix-010-common-elements-in-all-rows-of-a-giv": {
        'explanation': "**Problem:** Common elements in all rows of a given matrix\n**Pattern:** Matrix traversal\n**Difficulty:** Medium\n\n**Approach:** Standard Matrix approach: identify brute force, then optimize using matrix traversal typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(rows \u00d7 cols) |\n| Average | O(rows \u00d7 cols) |\n| Worst | O(rows \u00d7 cols) |\n\n**Why:** Visit each cell at least once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place row/col marking when possible.",
        'key_points': ['Pattern: Matrix traversal', 'Time: O(rows × cols) worst (O(rows × cols) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-guide-string": {
        'explanation': "String problems often use **sliding window** (O(n)) or **two pointers** for palindrome/substring tasks. Pattern matching: **KMP/Rabin-Karp** in O(n+m). Anagram problems use **frequency maps** of size alphabet.\n\nClarify whether input is Unicode or ASCII \u2014 alphabet size affects space in frequency arrays.",
        'key_points': ['Sliding window: O(n) amortized', 'KMP: O(n + m) pattern search', 'Anagram: O(n) with freq map', 'Palindrome two-pointer: O(n)'],
    },
    "dsa-450-string-001-reverse-a-string": {
        'explanation': "**Problem:** Reverse a String\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-002-check-whether-a-string-is-palindrome": {
        'explanation': "**Problem:** Check whether a String is Palindrome or not\n**Pattern:** Two pointers\n**Difficulty:** Medium\n\n**Approach:** Place pointers at ends or both at start; move based on comparison/greedy rule.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Pointers move monotonically across array/string once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Only index pointers and scalar trackers.",
        'key_points': ['Pattern: Two pointers', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-string-003-find-duplicate-characters-in-a-strin": {
        'explanation': "**Problem:** Find Duplicate characters in a string\n**Pattern:** Hash map / frequency count\n**Difficulty:** Medium\n\n**Approach:** Count occurrences in dictionary; answer from frequencies.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single pass with O(1) average map operations.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Map stores up to n distinct keys.",
        'key_points': ['Pattern: Hash map / frequency count', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-004-why-strings-are-immutable-in-java": {
        'explanation': "**Problem:** Why strings are immutable in Java?\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-005-write-a-code-to-check-whether-one-st": {
        'explanation': "**Problem:** Write a Code to check whether one string is a rotation of another\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-006-write-a-program-to-check-whether-a-s": {
        'explanation': "**Problem:** Write a Program to check whether a string is a valid shuffle of two strings or not\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-007-count-and-say-problem": {
        'explanation': "**Problem:** Count and Say problem\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-008-write-a-program-to-find-the-longest": {
        'explanation': "**Problem:** Write a program to find the longest Palindrome in a string.[ Longest palindromic Substring]\n**Pattern:** Two pointers\n**Difficulty:** Medium\n\n**Approach:** Place pointers at ends or both at start; move based on comparison/greedy rule.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Pointers move monotonically across array/string once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Only index pointers and scalar trackers.",
        'key_points': ['Pattern: Two pointers', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-string-009-find-longest-recurring-subsequence-i": {
        'explanation': "**Problem:** Find Longest Recurring Subsequence in String\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-010-print-all-subsequences-of-a-string": {
        'explanation': "**Problem:** Print all Subsequences of a string.\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-011-print-all-the-permutations-of-the-gi": {
        'explanation': "**Problem:** Print all the permutations of the given string\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Choose/explore/unchoose; prune invalid branches early.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Exponential search tree; permutations n!, subsets 2^n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth n plus path/used array.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-012-split-the-binary-string-into-two-sub": {
        'explanation': "**Problem:** Split the Binary string into two substring with equal 0\u2019s and 1\u2019s\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-013-word-wrap-problem-very-imp": {
        'explanation': "**Problem:** Word Wrap Problem [VERY IMP].\n**Pattern:** String processing\n**Difficulty:** Hard\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-014-edit-distance-very-imp": {
        'explanation': "**Problem:** EDIT Distance [Very Imp]\n**Pattern:** 2D DP on strings\n**Difficulty:** Hard\n\n**Approach:** dp[i][j] from dp[i-1][j], dp[i][j-1], dp[i-1][j-1] based on match.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(m \u00d7 n) |\n| Average | O(m \u00d7 n) |\n| Worst | O(m \u00d7 n) |\n\n**Why:** Fill (m+1)\u00d7(n+1) table comparing each char pair.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(min(m, n)) |\n\n**Why:** Rolling two-row optimization over longer dimension.",
        'key_points': ['Pattern: 2D DP on strings', 'Time: O(m × n) worst (O(m × n) best)', 'Space: O(min(m, n)) auxiliary'],
    },
    "dsa-450-string-015-find-next-greater-number-with-same-s": {
        'explanation': "**Problem:** Find next greater number with same set of digits. [Very Very IMP]\n**Pattern:** Monotonic stack\n**Difficulty:** Hard\n\n**Approach:** Maintain decreasing/increasing stack; pop when current resolves pending indices.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each index pushed and popped at most once \u2014 amortized O(n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack stores indices waiting for next greater/smaller.",
        'key_points': ['Pattern: Monotonic stack', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-016-balanced-parenthesis-problem-imp": {
        'explanation': "**Problem:** Balanced Parenthesis problem.[Imp]\n**Pattern:** Stack matching\n**Difficulty:** Hard\n\n**Approach:** Push opens; on close verify top matches and pop.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each character pushed/popped at most once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack holds up to n opening brackets.",
        'key_points': ['Pattern: Stack matching', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-017-word-break-problem-very-imp": {
        'explanation': "**Problem:** Word break Problem[ Very Imp]\n**Pattern:** String processing\n**Difficulty:** Hard\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-018-rabin-karp-algo": {
        'explanation': "**Problem:** Rabin Karp Algo\n**Pattern:** String matching / frequency\n**Difficulty:** Medium\n\n**Approach:** Build LPS for KMP or sliding window char counts for anagram.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n + m) |\n| Average | O(n + m) |\n| Worst | O(n + m) |\n\n**Why:** KMP/Rabin-Karp linear in text n plus pattern m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(m) |\n\n**Why:** LPS array or rolling hash window size m.",
        'key_points': ['Pattern: String matching / frequency', 'Time: O(n + m) worst (O(n + m) best)', 'Space: O(m) auxiliary'],
    },
    "dsa-450-string-019-kmp-algo": {
        'explanation': "**Problem:** KMP Algo\n**Pattern:** String matching / frequency\n**Difficulty:** Medium\n\n**Approach:** Build LPS for KMP or sliding window char counts for anagram.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n + m) |\n| Average | O(n + m) |\n| Worst | O(n + m) |\n\n**Why:** KMP/Rabin-Karp linear in text n plus pattern m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(m) |\n\n**Why:** LPS array or rolling hash window size m.",
        'key_points': ['Pattern: String matching / frequency', 'Time: O(n + m) worst (O(n + m) best)', 'Space: O(m) auxiliary'],
    },
    "dsa-450-string-020-convert-a-sentence-into-its-equivale": {
        'explanation': "**Problem:** Convert a Sentence into its equivalent mobile numeric keypad sequence.\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-021-minimum-number-of-bracket-reversals": {
        'explanation': "**Problem:** Minimum number of bracket reversals needed to make an expression balanced.\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-022-count-all-palindromic-subsequence-in": {
        'explanation': "**Problem:** Count All Palindromic Subsequence in a given String.\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-023-count-of-number-of-given-string-in-2": {
        'explanation': "**Problem:** Count of number of given string in 2D character array\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-024-search-a-word-in-a-2d-grid-of-charac": {
        'explanation': "**Problem:** Search a Word in a 2D Grid of characters.\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-025-boyer-moore-algorithm-for-pattern-se": {
        'explanation': "**Problem:** Boyer Moore Algorithm for Pattern Searching.\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-026-converting-roman-numerals-to-decimal": {
        'explanation': "**Problem:** Converting Roman Numerals to Decimal\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-027-longest-common-prefix": {
        'explanation': "**Problem:** Longest Common Prefix\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-028-number-of-flips-to-make-binary-strin": {
        'explanation': "**Problem:** Number of flips to make binary string alternate\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-029-find-the-first-repeated-word-in-stri": {
        'explanation': "**Problem:** Find the first repeated word in string.\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-030-minimum-number-of-swaps-for-bracket": {
        'explanation': "**Problem:** Minimum number of swaps for bracket balancing.\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-031-find-the-longest-common-subsequence": {
        'explanation': "**Problem:** Find the longest common subsequence between two strings.\n**Pattern:** 2D DP on strings\n**Difficulty:** Medium\n\n**Approach:** dp[i][j] from dp[i-1][j], dp[i][j-1], dp[i-1][j-1] based on match.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(m \u00d7 n) |\n| Average | O(m \u00d7 n) |\n| Worst | O(m \u00d7 n) |\n\n**Why:** Fill (m+1)\u00d7(n+1) table comparing each char pair.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(min(m, n)) |\n\n**Why:** Rolling two-row optimization over longer dimension.",
        'key_points': ['Pattern: 2D DP on strings', 'Time: O(m × n) worst (O(m × n) best)', 'Space: O(min(m, n)) auxiliary'],
    },
    "dsa-450-string-032-program-to-generate-all-possible-val": {
        'explanation': "**Problem:** Program to generate all possible valid IP addresses from given string.\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-033-write-a-program-tofind-the-smallest": {
        'explanation': "**Problem:** Write a program tofind the smallest window that contains all characters of string itself.\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-034-rearrange-characters-in-a-string-suc": {
        'explanation': "**Problem:** Rearrange characters in a string such that no two adjacent are same\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-035-minimum-characters-to-be-added-at-fr": {
        'explanation': "**Problem:** Minimum characters to be added at front to make string palindrome\n**Pattern:** Two pointers\n**Difficulty:** Medium\n\n**Approach:** Place pointers at ends or both at start; move based on comparison/greedy rule.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Pointers move monotonically across array/string once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Only index pointers and scalar trackers.",
        'key_points': ['Pattern: Two pointers', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-string-036-given-a-sequence-of-words-print-all": {
        'explanation': "**Problem:** Given a sequence of words, print all anagrams together\n**Pattern:** String matching / frequency\n**Difficulty:** Medium\n\n**Approach:** Build LPS for KMP or sliding window char counts for anagram.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n + m) |\n| Average | O(n + m) |\n| Worst | O(n + m) |\n\n**Why:** KMP/Rabin-Karp linear in text n plus pattern m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(m) |\n\n**Why:** LPS array or rolling hash window size m.",
        'key_points': ['Pattern: String matching / frequency', 'Time: O(n + m) worst (O(n + m) best)', 'Space: O(m) auxiliary'],
    },
    "dsa-450-string-037-find-the-smallest-window-in-a-string": {
        'explanation': "**Problem:** Find the smallest window in a string containing all characters of another string\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-038-recursively-remove-all-adjacent-dupl": {
        'explanation': "**Problem:** Recursively remove all adjacent duplicates\n**Pattern:** Hash map / frequency count\n**Difficulty:** Medium\n\n**Approach:** Count occurrences in dictionary; answer from frequencies.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single pass with O(1) average map operations.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Map stores up to n distinct keys.",
        'key_points': ['Pattern: Hash map / frequency count', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-039-string-matching-where-one-string-con": {
        'explanation': "**Problem:** String matching where one string contains wildcard characters\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-040-function-to-find-number-of-customers": {
        'explanation': "**Problem:** Function to find Number of customers who could not get a computer\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-041-transform-one-string-to-another-usin": {
        'explanation': "**Problem:** Transform One String to Another using Minimum Number of Given Operation\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-042-check-if-two-given-strings-are-isomo": {
        'explanation': "**Problem:** Check if two given strings are isomorphic to each other\n**Pattern:** String processing\n**Difficulty:** Medium\n\n**Approach:** Standard String approach: identify brute force, then optimize using string processing typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n \u00d7 m) |\n\n**Why:** Linear scan O(n); pattern matching may add pattern length m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Output or frequency map proportional to input.",
        'key_points': ['Pattern: String processing', 'Time: O(n × m) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-string-043-recursively-print-all-sentences-that": {
        'explanation': "**Problem:** Recursively print all sentences that can be formed from list of word lists\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-guide-searching-sorting": {
        'explanation': "**Binary search** requires sorted or monotonic predicate \u2014 **O(log n)**. Comparison sorts are **O(n log n)** lower bound. Linear search **O(n)** when unsorted.\n\nKnow merge sort (stable, O(n) extra), quicksort (in-place, O(log n) stack), counting/radix for bounded keys.",
        'key_points': ['Binary search: O(log n)', 'Merge/quick sort: O(n log n)', 'Counting sort: O(n + k) for range k', 'Search rotated array: modified BS'],
    },
    "dsa-450-searching-sorting-001-find-first-and-last-positions-of-an": {
        'explanation': "**Problem:** Find first and last positions of an element in a sorted array\n**Pattern:** Binary search\n**Difficulty:** Medium\n\n**Approach:** Maintain left/right bounds; compare mid and discard half.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(log n) |\n| Worst | O(log n) |\n\n**Why:** Halve search space each iteration on sorted/monotonic data.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Iterative binary search uses constant pointers.",
        'key_points': ['Pattern: Binary search', 'Time: O(log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-002-find-a-fixed-point-value-equal-to-in": {
        'explanation': "**Problem:** Find a Fixed Point (Value equal to index) in a given array\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-003-search-in-a-rotated-sorted-array": {
        'explanation': "**Problem:** Search in a rotated sorted array\n**Pattern:** In-place reversal / rotation\n**Difficulty:** Medium\n\n**Approach:** Two pointers swap from both ends, or reverse subarrays for rotation.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element moved once during reverse or rotate.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place two-pointer swap or triple-reversal trick.",
        'key_points': ['Pattern: In-place reversal / rotation', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-004-square-root-of-an-integer": {
        'explanation': "**Problem:** square root of an integer\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-005-maximum-and-minimum-of-an-array-usin": {
        'explanation': "**Problem:** Maximum and minimum of an array using minimum number of comparisons\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-006-optimum-location-of-point-to-minimiz": {
        'explanation': "**Problem:** Optimum location of point to minimize total distance\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-007-find-the-repeating-and-the-missing": {
        'explanation': "**Problem:** Find the repeating and the missing\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-008-find-majority-element": {
        'explanation': "**Problem:** find majority element\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-009-searching-in-an-array-where-adjacent": {
        'explanation': "**Problem:** Searching in an array where adjacent differ by at most k\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-010-find-a-pair-with-a-given-difference": {
        'explanation': "**Problem:** find a pair with a given difference\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-011-find-four-elements-that-sum-to-a-giv": {
        'explanation': "**Problem:** find four elements that sum to a given value\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-012-maximum-sum-such-that-no-2-elements": {
        'explanation': "**Problem:** maximum sum such that no 2 elements are adjacent\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-013-count-triplet-with-sum-smaller-than": {
        'explanation': "**Problem:** Count triplet with sum smaller than a given value\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-014-merge-2-sorted-arrays": {
        'explanation': "**Problem:** merge 2 sorted arrays\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-015-print-all-subarrays-with-0-sum": {
        'explanation': "**Problem:** print all subarrays with 0 sum\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-016-product-array-puzzle": {
        'explanation': "**Problem:** Product array Puzzle\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-017-sort-array-according-to-count-of-set": {
        'explanation': "**Problem:** Sort array according to count of set bits\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-018-minimum-no-of-swaps-required-to-sort": {
        'explanation': "**Problem:** minimum no. of swaps required to sort the array\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-019-bishu-and-soldiers": {
        'explanation': "**Problem:** Bishu and Soldiers\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-020-rasta-and-kheshtak": {
        'explanation': "**Problem:** Rasta and Kheshtak\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-021-kth-smallest-number-again": {
        'explanation': "**Problem:** Kth smallest number again\n**Pattern:** Heap / priority queue\n**Difficulty:** Medium\n\n**Approach:** Min-heap of size k for kth largest; balance two heaps for median.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log k) |\n| Average | O(n log k) |\n| Worst | O(n log k) |\n\n**Why:** Maintain size-k heap: n inserts each O(log k).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(k) |\n\n**Why:** Heap stores k elements (or two heaps for median).",
        'key_points': ['Pattern: Heap / priority queue', 'Time: O(n log k) worst (O(n log k) best)', 'Space: O(k) auxiliary'],
    },
    "dsa-450-searching-sorting-022-find-pivot-element-in-a-sorted-array": {
        'explanation': "**Problem:** Find pivot element in a sorted array\n**Pattern:** Binary search\n**Difficulty:** Medium\n\n**Approach:** Maintain left/right bounds; compare mid and discard half.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(log n) |\n| Worst | O(log n) |\n\n**Why:** Halve search space each iteration on sorted/monotonic data.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Iterative binary search uses constant pointers.",
        'key_points': ['Pattern: Binary search', 'Time: O(log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-023-k-th-element-of-two-sorted-arrays": {
        'explanation': "**Problem:** K-th Element of Two Sorted Arrays\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-024-aggressive-cows": {
        'explanation': "**Problem:** Aggressive cows\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-025-book-allocation-problem": {
        'explanation': "**Problem:** Book Allocation Problem\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-026-ekospoj": {
        'explanation': "**Problem:** EKOSPOJ:\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-027-job-scheduling-algo": {
        'explanation': "**Problem:** Job Scheduling Algo\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-028-missing-number-in-ap": {
        'explanation': "**Problem:** Missing Number in AP\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-029-smallest-number-with-atleastn-traili": {
        'explanation': "**Problem:** Smallest number with atleastn trailing zeroes infactorial\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-030-painters-partition-problem": {
        'explanation': "**Problem:** Painters Partition Problem:\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-031-roti-prata-spoj": {
        'explanation': "**Problem:** ROTI-Prata SPOJ\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-032-doublehelix-spoj": {
        'explanation': "**Problem:** DoubleHelix SPOJ\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-033-subset-sums": {
        'explanation': "**Problem:** Subset Sums\n**Pattern:** Dynamic programming \u2014 knapsack family\n**Difficulty:** Medium\n\n**Approach:** dp[w] = min/max ways to reach sum w using processed items.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n \u00d7 W) |\n\n**Why:** Fill DP table over n items and capacity/target W.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** 1D rolling DP over target/capacity dimension.",
        'key_points': ['Pattern: Dynamic programming — knapsack family', 'Time: O(n × W) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-searching-sorting-034-findthe-inversion-count": {
        'explanation': "**Problem:** Findthe inversion count\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-035-implement-merge-sort-in-place": {
        'explanation': "**Problem:** Implement Merge-sort in-place\n**Pattern:** Search or sort\n**Difficulty:** Medium\n\n**Approach:** Standard Searching & Sorting approach: identify brute force, then optimize using search or sort typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search O(log n) on sorted data; comparison sort O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place sort or iterative binary search.",
        'key_points': ['Pattern: Search or sort', 'Time: O(n log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-searching-sorting-036-partitioning-and-sorting-arrays-with": {
        'explanation': "**Problem:** Partitioning and Sorting Arrays with Many Repeated Entries\n**Pattern:** Trie traversal\n**Difficulty:** Medium\n\n**Approach:** Walk trie per character; mark end-of-word at terminal node.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(m) |\n| Average | O(m) |\n| Worst | O(m) |\n\n**Why:** m = key length; traverse/create one node per character.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n \u00d7 m) |\n\n**Why:** Trie stores up to n keys of average length m.",
        'key_points': ['Pattern: Trie traversal', 'Time: O(m) worst (O(m) best)', 'Space: O(n × m) auxiliary'],
    },
    "dsa-guide-linked-list": {
        'explanation': "Lists lack O(1) random access \u2014 expect **O(n)** scans. **Dummy nodes** simplify head deletion. **Fast/slow pointers** detect cycles and find mid in O(n) O(1). Reversal is **O(n)** iterative or recursive.\n\nRecursive solutions add **O(n) stack** \u2014 mention when comparing to iterative O(1) space.",
        'key_points': ['Dummy head for edge cases', 'Floyd cycle: O(n) O(1)', 'Reverse in-place: O(n) O(1)', 'Merge sorted lists: O(n+m)'],
    },
    "dsa-450-linked-list-001-write-a-program-to-reverse-the-linke": {
        'explanation': "**Problem:** Write a Program to reverse the Linked List. (Both Iterative and recursive)\n**Pattern:** Iterative/recursive reversal\n**Difficulty:** Medium\n\n**Approach:** prev/curr/next walk or recurse to end then reverse links on unwind.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Visit each node exactly once to rewire next pointers.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Iterative uses three pointers; recursive uses O(n) stack.",
        'key_points': ['Pattern: Iterative/recursive reversal', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-linked-list-002-reverse-a-linked-list-in-group-of-gi": {
        'explanation': "**Problem:** Reverse a Linked List in group of Given Size. [Very Imp]\n**Pattern:** Iterative/recursive reversal\n**Difficulty:** Hard\n\n**Approach:** prev/curr/next walk or recurse to end then reverse links on unwind.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Visit each node exactly once to rewire next pointers.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Iterative uses three pointers; recursive uses O(n) stack.",
        'key_points': ['Pattern: Iterative/recursive reversal', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-linked-list-003-write-a-program-to-detect-loop-in-a": {
        'explanation': "**Problem:** Write a program to Detect loop in a linked list.\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-004-write-a-program-to-delete-loop-in-a": {
        'explanation': "**Problem:** Write a program to Delete loop in a linked list.\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-005-find-the-starting-point-of-the-loop": {
        'explanation': "**Problem:** Find the starting point of the loop.\n**Pattern:** Linked list pointers\n**Difficulty:** Medium\n\n**Approach:** Standard LinkedList approach: identify brute force, then optimize using linked list pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single pass over n nodes typical.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Pointer manipulation without extra list.",
        'key_points': ['Pattern: Linked list pointers', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-linked-list-006-remove-duplicates-in-a-sorted-linked": {
        'explanation': "**Problem:** Remove Duplicates in a sorted Linked List.\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-007-remove-duplicates-in-a-un-sorted-lin": {
        'explanation': "**Problem:** Remove Duplicates in a Un-sorted Linked List.\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-008-write-a-program-to-move-the-last-ele": {
        'explanation': "**Problem:** Write a Program to Move the last element to Front in a Linked List.\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-009-add-1-to-a-number-represented-as-a-l": {
        'explanation': "**Problem:** Add \u201c1\u201d to a number represented as a Linked List.\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-010-add-two-numbers-represented-by-linke": {
        'explanation': "**Problem:** Add two numbers represented by linked lists.\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-011-intersection-of-two-sorted-linked-li": {
        'explanation': "**Problem:** Intersection of two Sorted Linked List.\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-012-intersection-point-of-two-linked-lis": {
        'explanation': "**Problem:** Intersection Point of two Linked Lists.\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-013-merge-sort-for-linked-lists-very-imp": {
        'explanation': "**Problem:** Merge Sort For Linked lists.[Very Important]\n**Pattern:** Sorting algorithm\n**Difficulty:** Medium\n\n**Approach:** Apply standard sort; analyze stability and in-place requirements.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Comparison sorts are O(n log n); counting/radix can be O(n+k) on bounded keys.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Merge sort needs O(n) auxiliary; in-place quicksort O(log n) stack.",
        'key_points': ['Pattern: Sorting algorithm', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-014-quicksort-for-linked-lists-very-impo": {
        'explanation': "**Problem:** Quicksort for Linked Lists.[Very Important]\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-015-find-the-middle-element-of-a-linked": {
        'explanation': "**Problem:** Find the middle Element of a linked list.\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-016-check-if-a-linked-list-is-a-circular": {
        'explanation': "**Problem:** Check if a linked list is a circular linked list.\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-017-split-a-circular-linked-list-into-tw": {
        'explanation': "**Problem:** Split a Circular linked list into two halves.\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-018-write-a-program-to-check-whether-the": {
        'explanation': "**Problem:** Write a Program to check whether the Singly Linked list is a palindrome or not.\n**Pattern:** Two pointers\n**Difficulty:** Medium\n\n**Approach:** Place pointers at ends or both at start; move based on comparison/greedy rule.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Pointers move monotonically across array/string once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Only index pointers and scalar trackers.",
        'key_points': ['Pattern: Two pointers', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-linked-list-019-deletion-from-a-circular-linked-list": {
        'explanation': "**Problem:** Deletion from a Circular Linked List.\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-020-reverse-a-doubly-linked-list": {
        'explanation': "**Problem:** Reverse a Doubly Linked list.\n**Pattern:** Iterative/recursive reversal\n**Difficulty:** Medium\n\n**Approach:** prev/curr/next walk or recurse to end then reverse links on unwind.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Visit each node exactly once to rewire next pointers.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Iterative uses three pointers; recursive uses O(n) stack.",
        'key_points': ['Pattern: Iterative/recursive reversal', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-linked-list-021-find-pairs-with-a-given-sum-in-a-dll": {
        'explanation': "**Problem:** Find pairs with a given sum in a DLL.\n**Pattern:** Hash map one-pass\n**Difficulty:** Medium\n\n**Approach:** Scan array; for each value check if (target - value) exists in map.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single pass with O(1) average hash lookups for complement.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Hash map stores up to n elements.",
        'key_points': ['Pattern: Hash map one-pass', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-022-count-triplets-in-a-sorted-dll-whose": {
        'explanation': "**Problem:** Count triplets in a sorted DLL whose sum is equal to given value \u201cX\u201d.\n**Pattern:** Linked list pointers\n**Difficulty:** Medium\n\n**Approach:** Standard LinkedList approach: identify brute force, then optimize using linked list pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single pass over n nodes typical.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Pointer manipulation without extra list.",
        'key_points': ['Pattern: Linked list pointers', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-linked-list-023-sort-a-k-sorted-doubly-linked-list-v": {
        'explanation': "**Problem:** Sort a \u201ck\u201dsorted Doubly Linked list.[Very IMP]\n**Pattern:** Patience sorting / DP\n**Difficulty:** Hard\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-024-rotate-doublylinked-list-by-n-nodes": {
        'explanation': "**Problem:** Rotate DoublyLinked list by N nodes.\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-025-rotate-a-doubly-linked-list-in-group": {
        'explanation': "**Problem:** Rotate a Doubly Linked list in group of Given Size.[Very IMP]\n**Pattern:** Patience sorting / DP\n**Difficulty:** Hard\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-026-can-we-reverse-a-linked-list-in-less": {
        'explanation': "**Problem:** Can we reverse a linked list in less than O(n) ?\n**Pattern:** Iterative/recursive reversal\n**Difficulty:** Medium\n\n**Approach:** prev/curr/next walk or recurse to end then reverse links on unwind.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Visit each node exactly once to rewire next pointers.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Iterative uses three pointers; recursive uses O(n) stack.",
        'key_points': ['Pattern: Iterative/recursive reversal', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-linked-list-027-why-quicksort-is-preferred-for-array": {
        'explanation': "**Problem:** Why Quicksort is preferred for. Arrays and Merge Sort for LinkedLists ?\n**Pattern:** Sorting algorithm\n**Difficulty:** Medium\n\n**Approach:** Apply standard sort; analyze stability and in-place requirements.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Comparison sorts are O(n log n); counting/radix can be O(n+k) on bounded keys.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Merge sort needs O(n) auxiliary; in-place quicksort O(log n) stack.",
        'key_points': ['Pattern: Sorting algorithm', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-028-flatten-a-linked-list": {
        'explanation': "**Problem:** Flatten a Linked List\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-029-sort-a-ll-of-0-s-1-s-and-2-s": {
        'explanation': "**Problem:** Sort a LL of 0's, 1's and 2's\n**Pattern:** Dutch national flag / counting\n**Difficulty:** Medium\n\n**Approach:** Use low/mid/high pointers or count 0s/1s/2s then rewrite array.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Three-way partition or count buckets in linear time.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place three-pointer partition.",
        'key_points': ['Pattern: Dutch national flag / counting', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-linked-list-030-clone-a-linked-list-with-next-and-ra": {
        'explanation': "**Problem:** Clone a linked list with next and random pointer\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-031-merge-k-sorted-linked-list": {
        'explanation': "**Problem:** Merge K sorted Linked list\n**Pattern:** Merge lists / heap\n**Difficulty:** Medium\n\n**Approach:** Dummy head; compare heads, attach smaller, advance pointer.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n + m) |\n| Average | O(n + m) |\n| Worst | O(n + m) |\n\n**Why:** Each node compared and linked once across input lists.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Iterative merge rewires pointers without extra list.",
        'key_points': ['Pattern: Merge lists / heap', 'Time: O(n + m) worst (O(n + m) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-linked-list-032-multiply-2-no-represented-by-ll": {
        'explanation': "**Problem:** Multiply 2 no. represented by LL\n**Pattern:** Linked list pointers\n**Difficulty:** Medium\n\n**Approach:** Standard LinkedList approach: identify brute force, then optimize using linked list pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single pass over n nodes typical.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Pointer manipulation without extra list.",
        'key_points': ['Pattern: Linked list pointers', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-linked-list-033-delete-nodes-which-have-a-greater-va": {
        'explanation': "**Problem:** Delete nodes which have a greater value on right side\n**Pattern:** Linked list pointers\n**Difficulty:** Medium\n\n**Approach:** Standard LinkedList approach: identify brute force, then optimize using linked list pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single pass over n nodes typical.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Pointer manipulation without extra list.",
        'key_points': ['Pattern: Linked list pointers', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-linked-list-034-segregate-even-and-odd-nodes-in-a-li": {
        'explanation': "**Problem:** Segregate even and odd nodes in a Linked List\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-035-program-for-n-th-node-from-the-end-o": {
        'explanation': "**Problem:** Program for n\u2019th node from the end of a Linked List\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-linked-list-036-find-the-first-non-repeating-charact": {
        'explanation': "**Problem:** Find the first non-repeating character from a stream of characters\n**Pattern:** Linked list pointers\n**Difficulty:** Medium\n\n**Approach:** Standard LinkedList approach: identify brute force, then optimize using linked list pointers typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single pass over n nodes typical.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Pointer manipulation without extra list.",
        'key_points': ['Pattern: Linked list pointers', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-guide-binary-trees": {
        'explanation': "Tree traversals visit each node once \u2192 **O(n)**. Stack/queue space **O(h)** where h is height (O(n) skewed, O(log n) balanced).\n\n**Post-order** aggregates from children (height, diameter, max path). **BFS** gives level-order and shortest path in unweighted tree.",
        'key_points': ['DFS/BFS: O(n) time', 'Recursion depth O(h)', 'Diameter/max-path: post-order combine', 'Serialize: O(n) pre-order'],
    },
    "dsa-450-binary-trees-001-level-order-traversal": {
        'explanation': "**Problem:** level order traversal\n**Pattern:** BFS level-order traversal\n**Difficulty:** Medium\n\n**Approach:** BFS with queue; process level size batches for level-wise output.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each node enqueued and dequeued once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Queue holds up to widest level (~n/2 nodes).",
        'key_points': ['Pattern: BFS level-order traversal', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-binary-trees-002-reverse-level-order-traversal": {
        'explanation': "**Problem:** Reverse Level Order traversal\n**Pattern:** BFS level-order traversal\n**Difficulty:** Medium\n\n**Approach:** BFS with queue; process level size batches for level-wise output.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each node enqueued and dequeued once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Queue holds up to widest level (~n/2 nodes).",
        'key_points': ['Pattern: BFS level-order traversal', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-binary-trees-003-height-of-a-tree": {
        'explanation': "**Problem:** Height of a tree\n**Pattern:** Tree DFS aggregation\n**Difficulty:** Medium\n\n**Approach:** Recurse children; combine left/right results at parent for global optimum.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single post-order pass computes answer at each node once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion depth equals tree height.",
        'key_points': ['Pattern: Tree DFS aggregation', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-004-diameter-of-a-tree": {
        'explanation': "**Problem:** Diameter of a tree\n**Pattern:** Tree DFS aggregation\n**Difficulty:** Medium\n\n**Approach:** Recurse children; combine left/right results at parent for global optimum.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single post-order pass computes answer at each node once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion depth equals tree height.",
        'key_points': ['Pattern: Tree DFS aggregation', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-005-mirror-of-a-tree": {
        'explanation': "**Problem:** Mirror of a tree\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-006-inorder-traversal-of-a-tree-both-usi": {
        'explanation': "**Problem:** Inorder Traversal of a tree both using recursion and Iteration\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-007-preorder-traversal-of-a-tree-both-us": {
        'explanation': "**Problem:** Preorder Traversal of a tree both using recursion and Iteration\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-008-postorder-traversal-of-a-tree-both-u": {
        'explanation': "**Problem:** Postorder Traversal of a tree both using recursion and Iteration\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-009-left-view-of-a-tree": {
        'explanation': "**Problem:** Left View of a tree\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-010-right-view-of-tree": {
        'explanation': "**Problem:** Right View of Tree\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-011-top-view-of-a-tree": {
        'explanation': "**Problem:** Top View of a tree\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-012-bottom-view-of-a-tree": {
        'explanation': "**Problem:** Bottom View of a tree\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-013-zig-zag-traversal-of-a-binary-tree": {
        'explanation': "**Problem:** Zig-Zag traversal of a binary tree\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-014-check-if-a-tree-is-balanced-or-not": {
        'explanation': "**Problem:** Check if a tree is balanced or not\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-015-diagnol-traversal-of-a-binary-tree": {
        'explanation': "**Problem:** Diagnol Traversal of a Binary tree\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-016-boundary-traversal-of-a-binary-tree": {
        'explanation': "**Problem:** Boundary traversal of a Binary tree\n**Pattern:** BFS level-order traversal\n**Difficulty:** Medium\n\n**Approach:** BFS with queue; process level size batches for level-wise output.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each node enqueued and dequeued once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Queue holds up to widest level (~n/2 nodes).",
        'key_points': ['Pattern: BFS level-order traversal', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-binary-trees-017-construct-binary-tree-from-string-wi": {
        'explanation': "**Problem:** Construct Binary Tree from String with Bracket Representation\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-018-convert-binary-tree-into-doubly-link": {
        'explanation': "**Problem:** Convert Binary tree into Doubly Linked List\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-binary-trees-019-convert-binary-tree-into-sum-tree": {
        'explanation': "**Problem:** Convert Binary tree into Sum tree\n**Pattern:** Tree DFS aggregation\n**Difficulty:** Medium\n\n**Approach:** Recurse children; combine left/right results at parent for global optimum.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single post-order pass computes answer at each node once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion depth equals tree height.",
        'key_points': ['Pattern: Tree DFS aggregation', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-020-construct-binary-tree-from-inorder-a": {
        'explanation': "**Problem:** Construct Binary tree from Inorder and preorder traversal\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-021-find-minimum-swaps-required-to-conve": {
        'explanation': "**Problem:** Find minimum swaps required to convert a Binary tree into BST\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-022-check-if-binary-tree-is-sum-tree-or": {
        'explanation': "**Problem:** Check if Binary tree is Sum tree or not\n**Pattern:** Tree DFS aggregation\n**Difficulty:** Medium\n\n**Approach:** Recurse children; combine left/right results at parent for global optimum.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single post-order pass computes answer at each node once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion depth equals tree height.",
        'key_points': ['Pattern: Tree DFS aggregation', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-023-check-if-all-leaf-nodes-are-at-same": {
        'explanation': "**Problem:** Check if all leaf nodes are at same level or not\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-024-check-if-a-binary-tree-contains-dupl": {
        'explanation': "**Problem:** Check if a Binary Tree contains duplicate subtrees of size 2 or more [ IMP ]\n**Pattern:** Hash map / frequency count\n**Difficulty:** Medium\n\n**Approach:** Count occurrences in dictionary; answer from frequencies.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single pass with O(1) average map operations.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Map stores up to n distinct keys.",
        'key_points': ['Pattern: Hash map / frequency count', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-binary-trees-025-check-if-2-trees-are-mirror-or-not": {
        'explanation': "**Problem:** Check if 2 trees are mirror or not\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-026-sum-of-nodes-on-the-longest-path-fro": {
        'explanation': "**Problem:** Sum of Nodes on the Longest path from root to leaf node\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-027-check-if-given-graph-is-tree-or-not": {
        'explanation': "**Problem:** Check if given graph is tree or not. [ IMP ]\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-028-find-largest-subtree-sum-in-a-tree": {
        'explanation': "**Problem:** Find Largest subtree sum in a tree\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-029-maximum-sum-of-nodes-in-binary-tree": {
        'explanation': "**Problem:** Maximum Sum of nodes in Binary tree such that no two are adjacent\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-030-print-all-k-sum-paths-in-a-binary-tr": {
        'explanation': "**Problem:** Print all \"K\" Sum paths in a Binary tree\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-031-find-lca-in-a-binary-tree": {
        'explanation': "**Problem:** Find LCA in a Binary tree\n**Pattern:** BST walk or post-order DFS\n**Difficulty:** Medium\n\n**Approach:** If both nodes on different sides of root, root is LCA; else recurse into child side.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(h) |\n| Average | O(h) |\n| Worst | O(n) |\n\n**Why:** Descend from root; split point is LCA. Skewed tree height n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursive DFS stack depth equals tree height.",
        'key_points': ['Pattern: BST walk or post-order DFS', 'Time: O(n) worst (O(h) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-032-find-distance-between-2-nodes-in-a-b": {
        'explanation': "**Problem:** Find distance between 2 nodes in a Binary tree\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-033-kth-ancestor-of-node-in-a-binary-tre": {
        'explanation': "**Problem:** Kth Ancestor of node in a Binary tree\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-binary-trees-034-find-all-duplicate-subtrees-in-a-bin": {
        'explanation': "**Problem:** Find all Duplicate subtrees in a Binary tree [ IMP ]\n**Pattern:** Hash map / frequency count\n**Difficulty:** Medium\n\n**Approach:** Count occurrences in dictionary; answer from frequencies.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single pass with O(1) average map operations.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Map stores up to n distinct keys.",
        'key_points': ['Pattern: Hash map / frequency count', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-binary-trees-035-tree-isomorphism-problem": {
        'explanation': "**Problem:** Tree Isomorphism Problem\n**Pattern:** Tree DFS/BFS\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Trees approach: identify brute force, then optimize using tree dfs/bfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each of n nodes visited once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion/stack depth equals tree height h.",
        'key_points': ['Pattern: Tree DFS/BFS', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-guide-bst": {
        'explanation': "BST operations are **O(h)** \u2014 O(log n) balanced, O(n) skewed. **In-order traversal** yields sorted order. Validate with **global min/max bounds**, not parent-only check.\n\nDeletion has three cases: leaf, one child, two children (in-order successor).",
        'key_points': ['Search/insert/delete: O(h)', 'In-order = sorted', 'Validate with bounds', 'Self-balancing AVL/RB: O(log n) guaranteed'],
    },
    "dsa-450-bst-001-fina-a-value-in-a-bst": {
        'explanation': "**Problem:** Fina a value in a BST\n**Pattern:** BST property exploitation\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Search Trees approach: identify brute force, then optimize using bst property exploitation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(h) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Balanced BST height log n; skewed degrades to n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursive calls or explicit stack depth h.",
        'key_points': ['Pattern: BST property exploitation', 'Time: O(n) worst (O(h) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-bst-002-deletion-of-a-node-in-a-bst": {
        'explanation': "**Problem:** Deletion of a node in a BST\n**Pattern:** BST property exploitation\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Search Trees approach: identify brute force, then optimize using bst property exploitation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(h) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Balanced BST height log n; skewed degrades to n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursive calls or explicit stack depth h.",
        'key_points': ['Pattern: BST property exploitation', 'Time: O(n) worst (O(h) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-bst-003-find-min-and-max-value-in-a-bst": {
        'explanation': "**Problem:** Find min and max value in a BST\n**Pattern:** BST property exploitation\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Search Trees approach: identify brute force, then optimize using bst property exploitation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(h) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Balanced BST height log n; skewed degrades to n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursive calls or explicit stack depth h.",
        'key_points': ['Pattern: BST property exploitation', 'Time: O(n) worst (O(h) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-bst-004-find-inorder-successor-and-inorder-p": {
        'explanation': "**Problem:** Find inorder successor and inorder predecessor in a BST\n**Pattern:** BST property exploitation\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Search Trees approach: identify brute force, then optimize using bst property exploitation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(h) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Balanced BST height log n; skewed degrades to n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursive calls or explicit stack depth h.",
        'key_points': ['Pattern: BST property exploitation', 'Time: O(n) worst (O(h) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-bst-005-check-if-a-tree-is-a-bst-or-not": {
        'explanation': "**Problem:** Check if a tree is a BST or not\n**Pattern:** BST property exploitation\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Search Trees approach: identify brute force, then optimize using bst property exploitation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(h) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Balanced BST height log n; skewed degrades to n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursive calls or explicit stack depth h.",
        'key_points': ['Pattern: BST property exploitation', 'Time: O(n) worst (O(h) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-bst-006-populate-inorder-successor-of-all-no": {
        'explanation': "**Problem:** Populate Inorder successor of all nodes\n**Pattern:** BST property exploitation\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Search Trees approach: identify brute force, then optimize using bst property exploitation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(h) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Balanced BST height log n; skewed degrades to n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursive calls or explicit stack depth h.",
        'key_points': ['Pattern: BST property exploitation', 'Time: O(n) worst (O(h) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-bst-007-find-lca-of-2-nodes-in-a-bst": {
        'explanation': "**Problem:** Find LCA of 2 nodes in a BST\n**Pattern:** BST walk or post-order DFS\n**Difficulty:** Medium\n\n**Approach:** If both nodes on different sides of root, root is LCA; else recurse into child side.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(h) |\n| Average | O(h) |\n| Worst | O(n) |\n\n**Why:** Descend from root; split point is LCA. Skewed tree height n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursive DFS stack depth equals tree height.",
        'key_points': ['Pattern: BST walk or post-order DFS', 'Time: O(n) worst (O(h) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-bst-008-construct-bst-from-preorder-traversa": {
        'explanation': "**Problem:** Construct BST from preorder traversal\n**Pattern:** BST property exploitation\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Search Trees approach: identify brute force, then optimize using bst property exploitation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(h) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Balanced BST height log n; skewed degrades to n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursive calls or explicit stack depth h.",
        'key_points': ['Pattern: BST property exploitation', 'Time: O(n) worst (O(h) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-bst-009-convert-binary-tree-into-bst": {
        'explanation': "**Problem:** Convert Binary tree into BST\n**Pattern:** BST property exploitation\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Search Trees approach: identify brute force, then optimize using bst property exploitation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(h) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Balanced BST height log n; skewed degrades to n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursive calls or explicit stack depth h.",
        'key_points': ['Pattern: BST property exploitation', 'Time: O(n) worst (O(h) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-bst-010-convert-a-normal-bst-into-a-balanced": {
        'explanation': "**Problem:** Convert a normal BST into a Balanced BST\n**Pattern:** BST property exploitation\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Search Trees approach: identify brute force, then optimize using bst property exploitation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(h) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Balanced BST height log n; skewed degrades to n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursive calls or explicit stack depth h.",
        'key_points': ['Pattern: BST property exploitation', 'Time: O(n) worst (O(h) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-bst-011-merge-two-bst-v-v-v-imp": {
        'explanation': "**Problem:** Merge two BST [ V.V.V>IMP ]\n**Pattern:** Merge lists / heap\n**Difficulty:** Medium\n\n**Approach:** Dummy head; compare heads, attach smaller, advance pointer.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n + m) |\n| Average | O(n + m) |\n| Worst | O(n + m) |\n\n**Why:** Each node compared and linked once across input lists.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Iterative merge rewires pointers without extra list.",
        'key_points': ['Pattern: Merge lists / heap', 'Time: O(n + m) worst (O(n + m) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-bst-012-find-kth-largest-element-in-a-bst": {
        'explanation': "**Problem:** Find Kth largest element in a BST\n**Pattern:** Heap / priority queue\n**Difficulty:** Medium\n\n**Approach:** Min-heap of size k for kth largest; balance two heaps for median.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log k) |\n| Average | O(n log k) |\n| Worst | O(n log k) |\n\n**Why:** Maintain size-k heap: n inserts each O(log k).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(k) |\n\n**Why:** Heap stores k elements (or two heaps for median).",
        'key_points': ['Pattern: Heap / priority queue', 'Time: O(n log k) worst (O(n log k) best)', 'Space: O(k) auxiliary'],
    },
    "dsa-450-bst-013-find-kth-smallest-element-in-a-bst": {
        'explanation': "**Problem:** Find Kth smallest element in a BST\n**Pattern:** Heap / priority queue\n**Difficulty:** Medium\n\n**Approach:** Min-heap of size k for kth largest; balance two heaps for median.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log k) |\n| Average | O(n log k) |\n| Worst | O(n log k) |\n\n**Why:** Maintain size-k heap: n inserts each O(log k).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(k) |\n\n**Why:** Heap stores k elements (or two heaps for median).",
        'key_points': ['Pattern: Heap / priority queue', 'Time: O(n log k) worst (O(n log k) best)', 'Space: O(k) auxiliary'],
    },
    "dsa-450-bst-014-count-pairs-from-2-bst-whose-sum-is": {
        'explanation': "**Problem:** Count pairs from 2 BST whose sum is equal to given value \"X\"\n**Pattern:** Hash map one-pass\n**Difficulty:** Medium\n\n**Approach:** Scan array; for each value check if (target - value) exists in map.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single pass with O(1) average hash lookups for complement.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Hash map stores up to n elements.",
        'key_points': ['Pattern: Hash map one-pass', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-bst-015-find-the-median-of-bst-in-o-n-time-a": {
        'explanation': "**Problem:** Find the median of BST in O(n) time and O(1) space\n**Pattern:** BST property exploitation\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Search Trees approach: identify brute force, then optimize using bst property exploitation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(h) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Balanced BST height log n; skewed degrades to n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursive calls or explicit stack depth h.",
        'key_points': ['Pattern: BST property exploitation', 'Time: O(n) worst (O(h) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-bst-016-count-bst-ndoes-that-lie-in-a-given": {
        'explanation': "**Problem:** Count BST ndoes that lie in a given range\n**Pattern:** BST property exploitation\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Search Trees approach: identify brute force, then optimize using bst property exploitation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(h) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Balanced BST height log n; skewed degrades to n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursive calls or explicit stack depth h.",
        'key_points': ['Pattern: BST property exploitation', 'Time: O(n) worst (O(h) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-bst-017-replace-every-element-with-the-least": {
        'explanation': "**Problem:** Replace every element with the least greater element on its right\n**Pattern:** BST property exploitation\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Search Trees approach: identify brute force, then optimize using bst property exploitation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(h) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Balanced BST height log n; skewed degrades to n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursive calls or explicit stack depth h.",
        'key_points': ['Pattern: BST property exploitation', 'Time: O(n) worst (O(h) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-bst-018-given-n-appointments-find-the-confli": {
        'explanation': "**Problem:** Given \"n\" appointments, find the conflicting appointments\n**Pattern:** BST property exploitation\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Search Trees approach: identify brute force, then optimize using bst property exploitation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(h) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Balanced BST height log n; skewed degrades to n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursive calls or explicit stack depth h.",
        'key_points': ['Pattern: BST property exploitation', 'Time: O(n) worst (O(h) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-bst-019-check-preorder-is-valid-or-not": {
        'explanation': "**Problem:** Check preorder is valid or not\n**Pattern:** BST property exploitation\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Search Trees approach: identify brute force, then optimize using bst property exploitation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(h) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Balanced BST height log n; skewed degrades to n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursive calls or explicit stack depth h.",
        'key_points': ['Pattern: BST property exploitation', 'Time: O(n) worst (O(h) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-bst-020-check-whether-bst-contains-dead-end": {
        'explanation': "**Problem:** Check whether BST contains Dead end\n**Pattern:** BST property exploitation\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Search Trees approach: identify brute force, then optimize using bst property exploitation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(h) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Balanced BST height log n; skewed degrades to n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursive calls or explicit stack depth h.",
        'key_points': ['Pattern: BST property exploitation', 'Time: O(n) worst (O(h) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-bst-021-largest-bst-in-a-binary-tree-v-v-v-v": {
        'explanation': "**Problem:** Largest BST in a Binary Tree [ V.V.V.V.V IMP ]\n**Pattern:** BST property exploitation\n**Difficulty:** Medium\n\n**Approach:** Standard Binary Search Trees approach: identify brute force, then optimize using bst property exploitation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(h) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Balanced BST height log n; skewed degrades to n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursive calls or explicit stack depth h.",
        'key_points': ['Pattern: BST property exploitation', 'Time: O(n) worst (O(h) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-bst-022-flatten-bst-to-sorted-list": {
        'explanation': "**Problem:** Flatten BST to sorted list\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-guide-greedy": {
        'explanation': "Greedy picks locally optimal choice if **greedy choice property** and **optimal substructure** hold. Usually **O(n log n)** from sorting by key (intervals, activities).\n\nProve greediness or cite exchange argument \u2014 interviewers expect justification, not just code.",
        'key_points': ['Sort + scan: O(n log n)', 'Interval scheduling classic', 'Huffman: heap O(n log n)', 'Prove greedy choice property'],
    },
    "dsa-450-greedy-001-activity-selection-problem": {
        'explanation': "**Problem:** Activity Selection Problem\n**Pattern:** Greedy choice\n**Difficulty:** Medium\n\n**Approach:** Prove greedy choice property; sort and pick locally optimal.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear scan.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place after sort except output list.",
        'key_points': ['Pattern: Greedy choice', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-002-job-sequencingproblem": {
        'explanation': "**Problem:** Job SequencingProblem\n**Pattern:** Greedy choice\n**Difficulty:** Medium\n\n**Approach:** Prove greedy choice property; sort and pick locally optimal.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear scan.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place after sort except output list.",
        'key_points': ['Pattern: Greedy choice', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-003-huffman-coding": {
        'explanation': "**Problem:** Huffman Coding\n**Pattern:** Greedy choice\n**Difficulty:** Medium\n\n**Approach:** Prove greedy choice property; sort and pick locally optimal.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear scan.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place after sort except output list.",
        'key_points': ['Pattern: Greedy choice', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-004-water-connection-problem": {
        'explanation': "**Problem:** Water Connection Problem\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-005-fractional-knapsack-problem": {
        'explanation': "**Problem:** Fractional Knapsack Problem\n**Pattern:** Dynamic programming \u2014 knapsack family\n**Difficulty:** Medium\n\n**Approach:** dp[w] = min/max ways to reach sum w using processed items.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n \u00d7 W) |\n\n**Why:** Fill DP table over n items and capacity/target W.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** 1D rolling DP over target/capacity dimension.",
        'key_points': ['Pattern: Dynamic programming — knapsack family', 'Time: O(n × W) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-greedy-006-greedy-algorithm-to-find-minimum-num": {
        'explanation': "**Problem:** Greedy Algorithm to find Minimum number of Coins\n**Pattern:** Greedy choice\n**Difficulty:** Medium\n\n**Approach:** Prove greedy choice property; sort and pick locally optimal.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear scan.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** In-place after sort except output list.",
        'key_points': ['Pattern: Greedy choice', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-007-maximum-trains-for-which-stoppage-ca": {
        'explanation': "**Problem:** Maximum trains for which stoppage can be provided\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-008-minimum-platforms-problem": {
        'explanation': "**Problem:** Minimum Platforms Problem\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-009-buy-maximum-stocks-if-i-stocks-can-b": {
        'explanation': "**Problem:** Buy Maximum Stocks if i stocks can be bought on i-th day\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-010-find-the-minimum-and-maximum-amount": {
        'explanation': "**Problem:** Find the minimum and maximum amount to buy all N candies\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-011-minimize-cash-flow-among-a-given-set": {
        'explanation': "**Problem:** Minimize Cash Flow among a given set of friends who have borrowed money from each other\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-012-minimum-cost-to-cut-a-board-into-squ": {
        'explanation': "**Problem:** Minimum Cost to cut a board into squares\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-013-check-if-it-is-possible-to-survive-o": {
        'explanation': "**Problem:** Check if it is possible to survive on Island\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-014-find-maximum-meetings-in-one-room": {
        'explanation': "**Problem:** Find maximum meetings in one room\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-015-maximum-product-subset-of-an-array": {
        'explanation': "**Problem:** Maximum product subset of an array\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Choose/explore/unchoose; prune invalid branches early.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Exponential search tree; permutations n!, subsets 2^n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth n plus path/used array.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-greedy-016-maximize-array-sum-after-k-negations": {
        'explanation': "**Problem:** Maximize array sum after K negations\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-017-maximize-the-sum-of-arr-i-i": {
        'explanation': "**Problem:** Maximize the sum of arr[i]*i\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-018-maximum-sum-of-absolute-difference-o": {
        'explanation': "**Problem:** Maximum sum of absolute difference of an array\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-019-maximize-sum-of-consecutive-differen": {
        'explanation': "**Problem:** Maximize sum of consecutive differences in a circular array\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-020-minimum-sum-of-absolute-difference-o": {
        'explanation': "**Problem:** Minimum sum of absolute difference of pairs of two arrays\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-021-program-for-shortest-job-first-or-sj": {
        'explanation': "**Problem:** Program for Shortest Job First (or SJF) CPU Scheduling\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-022-program-for-least-recently-used-lru": {
        'explanation': "**Problem:** Program for Least Recently Used (LRU) Page Replacement algorithm\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-023-smallest-subset-with-sum-greater-tha": {
        'explanation': "**Problem:** Smallest subset with sum greater than all other elements\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Choose/explore/unchoose; prune invalid branches early.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Exponential search tree; permutations n!, subsets 2^n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth n plus path/used array.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-greedy-024-chocolate-distribution-problem": {
        'explanation': "**Problem:** Chocolate Distribution Problem\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-025-defkin-defense-of-a-kingdom": {
        'explanation': "**Problem:** DEFKIN -Defense of a Kingdom\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-026-diehard-die-hard": {
        'explanation': "**Problem:** DIEHARD -DIE HARD\n**Pattern:** Greedy selection\n**Difficulty:** Hard\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-027-gergovia-wine-trading-in-gergovia": {
        'explanation': "**Problem:** GERGOVIA -Wine trading in Gergovia\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-028-picking-up-chicks": {
        'explanation': "**Problem:** Picking Up Chicks\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-029-chocola-chocolate": {
        'explanation': "**Problem:** CHOCOLA \u2013Chocolate\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-030-arrange-arranging-amplifiers": {
        'explanation': "**Problem:** ARRANGE -Arranging Amplifiers\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-031-k-centers-problem": {
        'explanation': "**Problem:** K Centers Problem\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-032-minimum-cost-of-ropes": {
        'explanation': "**Problem:** Minimum Cost of ropes\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-033-find-smallest-number-with-given-numb": {
        'explanation': "**Problem:** Find smallest number with given number of digits and sum of digits\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-034-rearrange-characters-in-a-string-suc": {
        'explanation': "**Problem:** Rearrange characters in a string such that no two adjacent are same\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-greedy-035-find-maximum-sum-possible-equal-sum": {
        'explanation': "**Problem:** Find maximum sum possible equal sum of three stacks\n**Pattern:** Greedy selection\n**Difficulty:** Medium\n\n**Approach:** Standard Greedy approach: identify brute force, then optimize using greedy selection typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Sort by greedy key then linear pass.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra after sorting in-place.",
        'key_points': ['Pattern: Greedy selection', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-guide-backtracking": {
        'explanation': "Backtracking explores decision trees: subsets **O(2^n)**, permutations **O(n!)**. Prune early when partial solution cannot succeed (N-Queens, Sudoku).\n\nAuxiliary space **O(n)** for recursion depth and current path; output may dominate.",
        'key_points': ['Subsets: O(2^n)', 'Permutations: O(n!)', 'Prune invalid branches', 'Undo choice after recursion'],
    },
    "dsa-450-backtracking-001-rat-in-a-maze-problem": {
        'explanation': "**Problem:** Rat in a maze Problem\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Choose/explore/unchoose; prune invalid branches early.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Exponential search tree; permutations n!, subsets 2^n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth n plus path/used array.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-backtracking-002-printing-all-solutions-in-n-queen-pr": {
        'explanation': "**Problem:** Printing all solutions in N-Queen Problem\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Standard BackTracking approach: identify brute force, then optimize using backtracking typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Explore decision tree; permutations factorial, subsets exponential.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth and current path storage.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-backtracking-003-word-break-problem-using-backtrackin": {
        'explanation': "**Problem:** Word Break Problem using Backtracking\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Choose/explore/unchoose; prune invalid branches early.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Exponential search tree; permutations n!, subsets 2^n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth n plus path/used array.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-backtracking-004-remove-invalid-parentheses": {
        'explanation': "**Problem:** Remove Invalid Parentheses\n**Pattern:** Stack matching\n**Difficulty:** Medium\n\n**Approach:** Push opens; on close verify top matches and pop.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each character pushed/popped at most once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack holds up to n opening brackets.",
        'key_points': ['Pattern: Stack matching', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-backtracking-005-sudoku-solver": {
        'explanation': "**Problem:** Sudoku Solver\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Choose/explore/unchoose; prune invalid branches early.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Exponential search tree; permutations n!, subsets 2^n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth n plus path/used array.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-backtracking-006-m-coloring-problem": {
        'explanation': "**Problem:** m Coloring Problem\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Standard BackTracking approach: identify brute force, then optimize using backtracking typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Explore decision tree; permutations factorial, subsets exponential.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth and current path storage.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-backtracking-007-print-all-palindromic-partitions-of": {
        'explanation': "**Problem:** Print all palindromic partitions of a string\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Standard BackTracking approach: identify brute force, then optimize using backtracking typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Explore decision tree; permutations factorial, subsets exponential.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth and current path storage.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-backtracking-008-subset-sum-problem": {
        'explanation': "**Problem:** Subset Sum Problem\n**Pattern:** Dynamic programming \u2014 knapsack family\n**Difficulty:** Medium\n\n**Approach:** dp[w] = min/max ways to reach sum w using processed items.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n \u00d7 W) |\n\n**Why:** Fill DP table over n items and capacity/target W.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** 1D rolling DP over target/capacity dimension.",
        'key_points': ['Pattern: Dynamic programming — knapsack family', 'Time: O(n × W) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-backtracking-009-the-knight-s-tour-problem": {
        'explanation': "**Problem:** The Knight\u2019s tour problem\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Standard BackTracking approach: identify brute force, then optimize using backtracking typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Explore decision tree; permutations factorial, subsets exponential.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth and current path storage.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-backtracking-010-tug-of-war": {
        'explanation': "**Problem:** Tug of War\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Standard BackTracking approach: identify brute force, then optimize using backtracking typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Explore decision tree; permutations factorial, subsets exponential.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth and current path storage.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-backtracking-011-find-shortest-safe-route-in-a-path-w": {
        'explanation': "**Problem:** Find shortest safe route in a path with landmines\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Standard BackTracking approach: identify brute force, then optimize using backtracking typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Explore decision tree; permutations factorial, subsets exponential.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth and current path storage.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-backtracking-012-combinational-sum": {
        'explanation': "**Problem:** Combinational Sum\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Choose/explore/unchoose; prune invalid branches early.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Exponential search tree; permutations n!, subsets 2^n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth n plus path/used array.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-backtracking-013-find-maximum-number-possible-by-doin": {
        'explanation': "**Problem:** Find Maximum number possible by doing at-most K swaps\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Standard BackTracking approach: identify brute force, then optimize using backtracking typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Explore decision tree; permutations factorial, subsets exponential.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth and current path storage.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-backtracking-014-print-all-permutations-of-a-string": {
        'explanation': "**Problem:** Print all permutations of a string\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Choose/explore/unchoose; prune invalid branches early.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Exponential search tree; permutations n!, subsets 2^n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth n plus path/used array.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-backtracking-015-find-if-there-is-a-path-of-more-than": {
        'explanation': "**Problem:** Find if there is a path of more than k length from a source\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Standard BackTracking approach: identify brute force, then optimize using backtracking typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Explore decision tree; permutations factorial, subsets exponential.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth and current path storage.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-backtracking-016-longest-possible-route-in-a-matrix-w": {
        'explanation': "**Problem:** Longest Possible Route in a Matrix with Hurdles\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Standard BackTracking approach: identify brute force, then optimize using backtracking typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Explore decision tree; permutations factorial, subsets exponential.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth and current path storage.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-backtracking-017-print-all-possible-paths-from-top-le": {
        'explanation': "**Problem:** Print all possible paths from top left to bottom right of a mXn matrix\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Standard BackTracking approach: identify brute force, then optimize using backtracking typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Explore decision tree; permutations factorial, subsets exponential.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth and current path storage.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-backtracking-018-partition-of-a-set-intok-subsets-wit": {
        'explanation': "**Problem:** Partition of a set intoK subsets with equal sum\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Choose/explore/unchoose; prune invalid branches early.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Exponential search tree; permutations n!, subsets 2^n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth n plus path/used array.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-backtracking-019-find-the-k-th-permutation-sequence-o": {
        'explanation': "**Problem:** Find the K-th Permutation Sequence of first N natural numbers\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Choose/explore/unchoose; prune invalid branches early.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Exponential search tree; permutations n!, subsets 2^n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth n plus path/used array.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-guide-stack-queue": {
        'explanation': "Stacks solve **LIFO** nesting and **monotonic next-greater/smaller** in **O(n) amortized**. Queues model BFS and sliding-window max with deque.\n\nMin-stack uses auxiliary structure for O(1) getMin at O(n) space cost.",
        'key_points': ['Monotonic stack: O(n) amortized', 'Valid parentheses: O(n)', 'Queue BFS: O(n) per level', 'Deque window max: O(n)'],
    },
    "dsa-450-stack-queue-001-implement-stack-from-scratch": {
        'explanation': "**Problem:** Implement Stack from Scratch\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-002-implement-queue-from-scratch": {
        'explanation': "**Problem:** Implement Queue from Scratch\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-003-implement-2-stack-in-an-array": {
        'explanation': "**Problem:** Implement 2 stack in an array\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-004-find-the-middle-element-of-a-stack": {
        'explanation': "**Problem:** find the middle element of a stack\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-005-implement-n-stacks-in-an-array": {
        'explanation': "**Problem:** Implement \"N\" stacks in an Array\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-006-check-the-expression-has-valid-or-ba": {
        'explanation': "**Problem:** Check the expression has valid or Balanced parenthesis or not.\n**Pattern:** Stack matching\n**Difficulty:** Medium\n\n**Approach:** Push opens; on close verify top matches and pop.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each character pushed/popped at most once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack holds up to n opening brackets.",
        'key_points': ['Pattern: Stack matching', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-007-reverse-a-string-using-stack": {
        'explanation': "**Problem:** Reverse a String using Stack\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-008-design-a-stack-that-supports-getmin": {
        'explanation': "**Problem:** Design a Stack that supports getMin() in O(1) time and O(1) extra space.\n**Pattern:** Auxiliary min tracking\n**Difficulty:** Medium\n\n**Approach:** Push (value, currentMin); pop both together.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(1) |\n| Average | O(1) |\n| Worst | O(1) |\n\n**Why:** Push/pop/top/getMin each O(1) with paired min stack or stored tuple.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Second stack or pairs store running minimum per level.",
        'key_points': ['Pattern: Auxiliary min tracking', 'Time: O(1) worst (O(1) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-009-find-the-next-greater-element": {
        'explanation': "**Problem:** Find the next Greater element\n**Pattern:** Monotonic stack\n**Difficulty:** Medium\n\n**Approach:** Maintain decreasing/increasing stack; pop when current resolves pending indices.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each index pushed and popped at most once \u2014 amortized O(n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack stores indices waiting for next greater/smaller.",
        'key_points': ['Pattern: Monotonic stack', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-010-the-celebrity-problem": {
        'explanation': "**Problem:** The celebrity Problem\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-011-arithmetic-expression-evaluation": {
        'explanation': "**Problem:** Arithmetic Expression evaluation\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-012-evaluation-of-postfix-expression": {
        'explanation': "**Problem:** Evaluation of Postfix expression\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-013-implement-a-method-to-insert-an-elem": {
        'explanation': "**Problem:** Implement a method to insert an element at its bottom without using any other data structure.\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-014-reverse-a-stack-using-recursion": {
        'explanation': "**Problem:** Reverse a stack using recursion\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-015-sort-a-stack-using-recursion": {
        'explanation': "**Problem:** Sort a Stack using recursion\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-016-merge-overlapping-intervals": {
        'explanation': "**Problem:** Merge Overlapping Intervals\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-017-largest-rectangular-area-in-histogra": {
        'explanation': "**Problem:** Largest rectangular Area in Histogram\n**Pattern:** Monotonic stack\n**Difficulty:** Medium\n\n**Approach:** Maintain decreasing/increasing stack; pop when current resolves pending indices.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each index pushed and popped at most once \u2014 amortized O(n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack stores indices waiting for next greater/smaller.",
        'key_points': ['Pattern: Monotonic stack', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-018-length-of-the-longest-valid-substrin": {
        'explanation': "**Problem:** Length of the Longest Valid Substring\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-019-expression-contains-redundant-bracke": {
        'explanation': "**Problem:** Expression contains redundant bracket or not\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-020-implement-stack-using-queue": {
        'explanation': "**Problem:** Implement Stack using Queue\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-021-implement-stack-using-deque": {
        'explanation': "**Problem:** Implement Stack using Deque\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-022-stack-permutations-check-if-an-array": {
        'explanation': "**Problem:** Stack Permutations (Check if an array is stack permutation of other)\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Choose/explore/unchoose; prune invalid branches early.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Exponential search tree; permutations n!, subsets 2^n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth n plus path/used array.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-023-implement-queue-using-stack": {
        'explanation': "**Problem:** Implement Queue using Stack\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-024-implement-n-queue-in-an-array": {
        'explanation': "**Problem:** Implement \"n\" queue in an array\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-025-implement-a-circular-queue": {
        'explanation': "**Problem:** Implement a Circular queue\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-026-lru-cache-implementationa": {
        'explanation': "**Problem:** LRU Cache Implementationa\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-027-reverse-a-queue-using-recursion": {
        'explanation': "**Problem:** Reverse a Queue using recursion\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-028-reverse-the-first-k-elements-of-a-qu": {
        'explanation': "**Problem:** Reverse the first \u201cK\u201d elements of a queue\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-029-interleave-the-first-half-of-the-que": {
        'explanation': "**Problem:** Interleave the first half of the queue with second half\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-030-find-the-first-circular-tour-that-vi": {
        'explanation': "**Problem:** Find the first circular tour that visits all Petrol Pumps\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-031-minimum-time-required-to-rot-all-ora": {
        'explanation': "**Problem:** Minimum time required to rot all oranges\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-032-distance-of-nearest-cell-having-1-in": {
        'explanation': "**Problem:** Distance of nearest cell having 1 in a binary matrix\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-033-first-negative-integer-in-every-wind": {
        'explanation': "**Problem:** First negative integer in every window of size \u201ck\u201d\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-034-check-if-all-levels-of-two-trees-are": {
        'explanation': "**Problem:** Check if all levels of two trees are anagrams or not.\n**Pattern:** String matching / frequency\n**Difficulty:** Medium\n\n**Approach:** Build LPS for KMP or sliding window char counts for anagram.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n + m) |\n| Average | O(n + m) |\n| Worst | O(n + m) |\n\n**Why:** KMP/Rabin-Karp linear in text n plus pattern m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(m) |\n\n**Why:** LPS array or rolling hash window size m.",
        'key_points': ['Pattern: String matching / frequency', 'Time: O(n + m) worst (O(n + m) best)', 'Space: O(m) auxiliary'],
    },
    "dsa-450-stack-queue-035-sum-of-minimum-and-maximum-elements": {
        'explanation': "**Problem:** Sum of minimum and maximum elements of all subarrays of size \u201ck\u201d.\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-036-minimum-sum-of-squares-of-character": {
        'explanation': "**Problem:** Minimum sum of squares of character counts in a given string after removing \u201ck\u201d characters.\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-037-queue-based-approach-or-first-non-re": {
        'explanation': "**Problem:** Queue based approach or first non-repeating character in a stream.\n**Pattern:** Stack/queue simulation\n**Difficulty:** Medium\n\n**Approach:** Standard Stacks & Queues approach: identify brute force, then optimize using stack/queue simulation typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each element pushed/popped once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack/queue holds up to n elements.",
        'key_points': ['Pattern: Stack/queue simulation', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-stack-queue-038-next-smaller-element": {
        'explanation': "**Problem:** Next Smaller Element\n**Pattern:** Monotonic stack\n**Difficulty:** Medium\n\n**Approach:** Maintain decreasing/increasing stack; pop when current resolves pending indices.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Each index pushed and popped at most once \u2014 amortized O(n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Stack stores indices waiting for next greater/smaller.",
        'key_points': ['Pattern: Monotonic stack', 'Time: O(n) worst (O(n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-guide-heap": {
        'explanation': "Heaps give **O(log n)** insert/extract and **O(1)** peek. **Top-k** problems: min-heap size k \u2192 **O(n log k)**. Merge k sorted lists: heap of k heads \u2192 **O(n log k)**.\n\nTwo-heap median trick balances halves in O(log n) per add.",
        'key_points': ['Insert/extract: O(log n)', 'Top-k: O(n log k)', 'Build heap: O(n)', 'Two heaps for streaming median'],
    },
    "dsa-450-heap-001-implement-a-maxheap-minheap-using-ar": {
        'explanation': "**Problem:** Implement a Maxheap/MinHeap using arrays and recursion.\n**Pattern:** Heap / priority queue\n**Difficulty:** Medium\n\n**Approach:** Min-heap of size k for kth largest; balance two heaps for median.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log k) |\n| Average | O(n log k) |\n| Worst | O(n log k) |\n\n**Why:** Maintain size-k heap: n inserts each O(log k).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(k) |\n\n**Why:** Heap stores k elements (or two heaps for median).",
        'key_points': ['Pattern: Heap / priority queue', 'Time: O(n log k) worst (O(n log k) best)', 'Space: O(k) auxiliary'],
    },
    "dsa-450-heap-002-sort-an-array-using-heap-heapsort": {
        'explanation': "**Problem:** Sort an Array using heap. (HeapSort)\n**Pattern:** Heap / priority queue\n**Difficulty:** Medium\n\n**Approach:** Min-heap of size k for kth largest; balance two heaps for median.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log k) |\n| Average | O(n log k) |\n| Worst | O(n log k) |\n\n**Why:** Maintain size-k heap: n inserts each O(log k).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(k) |\n\n**Why:** Heap stores k elements (or two heaps for median).",
        'key_points': ['Pattern: Heap / priority queue', 'Time: O(n log k) worst (O(n log k) best)', 'Space: O(k) auxiliary'],
    },
    "dsa-450-heap-003-maximum-of-all-subarrays-of-size-k": {
        'explanation': "**Problem:** Maximum of all subarrays of size k.\n**Pattern:** Heap operations\n**Difficulty:** Medium\n\n**Approach:** Standard Heap approach: identify brute force, then optimize using heap operations typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Build heap O(n) or n extract-min operations O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Heap stores all n elements.",
        'key_points': ['Pattern: Heap operations', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-heap-004-k-largest-element-in-an-array": {
        'explanation': "**Problem:** \u201ck\u201d largest element in an array\n**Pattern:** Heap operations\n**Difficulty:** Medium\n\n**Approach:** Standard Heap approach: identify brute force, then optimize using heap operations typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Build heap O(n) or n extract-min operations O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Heap stores all n elements.",
        'key_points': ['Pattern: Heap operations', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-heap-005-kth-smallest-and-largest-element-in": {
        'explanation': "**Problem:** Kth smallest and largest element in an unsorted array\n**Pattern:** Heap / priority queue\n**Difficulty:** Medium\n\n**Approach:** Min-heap of size k for kth largest; balance two heaps for median.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log k) |\n| Average | O(n log k) |\n| Worst | O(n log k) |\n\n**Why:** Maintain size-k heap: n inserts each O(log k).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(k) |\n\n**Why:** Heap stores k elements (or two heaps for median).",
        'key_points': ['Pattern: Heap / priority queue', 'Time: O(n log k) worst (O(n log k) best)', 'Space: O(k) auxiliary'],
    },
    "dsa-450-heap-006-merge-k-sorted-arrays-imp": {
        'explanation': "**Problem:** Merge \u201cK\u201d sorted arrays. [ IMP ]\n**Pattern:** Heap operations\n**Difficulty:** Medium\n\n**Approach:** Standard Heap approach: identify brute force, then optimize using heap operations typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Build heap O(n) or n extract-min operations O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Heap stores all n elements.",
        'key_points': ['Pattern: Heap operations', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-heap-007-merge-2-binary-max-heaps": {
        'explanation': "**Problem:** Merge 2 Binary Max Heaps\n**Pattern:** Heap / priority queue\n**Difficulty:** Medium\n\n**Approach:** Min-heap of size k for kth largest; balance two heaps for median.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log k) |\n| Average | O(n log k) |\n| Worst | O(n log k) |\n\n**Why:** Maintain size-k heap: n inserts each O(log k).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(k) |\n\n**Why:** Heap stores k elements (or two heaps for median).",
        'key_points': ['Pattern: Heap / priority queue', 'Time: O(n log k) worst (O(n log k) best)', 'Space: O(k) auxiliary'],
    },
    "dsa-450-heap-008-kth-largest-sum-continuous-subarrays": {
        'explanation': "**Problem:** Kth largest sum continuous subarrays\n**Pattern:** Heap / priority queue\n**Difficulty:** Medium\n\n**Approach:** Min-heap of size k for kth largest; balance two heaps for median.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log k) |\n| Average | O(n log k) |\n| Worst | O(n log k) |\n\n**Why:** Maintain size-k heap: n inserts each O(log k).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(k) |\n\n**Why:** Heap stores k elements (or two heaps for median).",
        'key_points': ['Pattern: Heap / priority queue', 'Time: O(n log k) worst (O(n log k) best)', 'Space: O(k) auxiliary'],
    },
    "dsa-450-heap-009-leetcode-reorganize-strings": {
        'explanation': "**Problem:** Leetcode- reorganize strings\n**Pattern:** Heap operations\n**Difficulty:** Medium\n\n**Approach:** Standard Heap approach: identify brute force, then optimize using heap operations typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Build heap O(n) or n extract-min operations O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Heap stores all n elements.",
        'key_points': ['Pattern: Heap operations', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-heap-010-merge-k-sorted-linked-lists-v-imp": {
        'explanation': "**Problem:** Merge \u201cK\u201d Sorted Linked Lists [V.IMP]\n**Pattern:** Merge lists / heap\n**Difficulty:** Hard\n\n**Approach:** Dummy head; compare heads, attach smaller, advance pointer.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n + m) |\n| Average | O(n + m) |\n| Worst | O(n + m) |\n\n**Why:** Each node compared and linked once across input lists.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Iterative merge rewires pointers without extra list.",
        'key_points': ['Pattern: Merge lists / heap', 'Time: O(n + m) worst (O(n + m) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-heap-011-smallest-range-in-k-lists": {
        'explanation': "**Problem:** Smallest range in \u201cK\u201d Lists\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-heap-012-median-in-a-stream-of-integers": {
        'explanation': "**Problem:** Median in a stream of Integers\n**Pattern:** Heap / priority queue\n**Difficulty:** Medium\n\n**Approach:** Min-heap of size k for kth largest; balance two heaps for median.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log k) |\n| Average | O(n log k) |\n| Worst | O(n log k) |\n\n**Why:** Maintain size-k heap: n inserts each O(log k).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(k) |\n\n**Why:** Heap stores k elements (or two heaps for median).",
        'key_points': ['Pattern: Heap / priority queue', 'Time: O(n log k) worst (O(n log k) best)', 'Space: O(k) auxiliary'],
    },
    "dsa-450-heap-013-check-if-a-binary-tree-is-heap": {
        'explanation': "**Problem:** Check if a Binary Tree is Heap\n**Pattern:** Heap / priority queue\n**Difficulty:** Medium\n\n**Approach:** Min-heap of size k for kth largest; balance two heaps for median.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log k) |\n| Average | O(n log k) |\n| Worst | O(n log k) |\n\n**Why:** Maintain size-k heap: n inserts each O(log k).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(k) |\n\n**Why:** Heap stores k elements (or two heaps for median).",
        'key_points': ['Pattern: Heap / priority queue', 'Time: O(n log k) worst (O(n log k) best)', 'Space: O(k) auxiliary'],
    },
    "dsa-450-heap-014-connect-n-ropes-with-minimum-cost": {
        'explanation': "**Problem:** Connect \u201cn\u201d ropes with minimum cost\n**Pattern:** Heap operations\n**Difficulty:** Medium\n\n**Approach:** Standard Heap approach: identify brute force, then optimize using heap operations typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Build heap O(n) or n extract-min operations O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Heap stores all n elements.",
        'key_points': ['Pattern: Heap operations', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-heap-015-convert-bst-to-min-heap": {
        'explanation': "**Problem:** Convert BST to Min Heap\n**Pattern:** Heap / priority queue\n**Difficulty:** Medium\n\n**Approach:** Min-heap of size k for kth largest; balance two heaps for median.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log k) |\n| Average | O(n log k) |\n| Worst | O(n log k) |\n\n**Why:** Maintain size-k heap: n inserts each O(log k).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(k) |\n\n**Why:** Heap stores k elements (or two heaps for median).",
        'key_points': ['Pattern: Heap / priority queue', 'Time: O(n log k) worst (O(n log k) best)', 'Space: O(k) auxiliary'],
    },
    "dsa-450-heap-016-convert-min-heap-to-max-heap": {
        'explanation': "**Problem:** Convert min heap to max heap\n**Pattern:** Heap / priority queue\n**Difficulty:** Medium\n\n**Approach:** Min-heap of size k for kth largest; balance two heaps for median.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log k) |\n| Average | O(n log k) |\n| Worst | O(n log k) |\n\n**Why:** Maintain size-k heap: n inserts each O(log k).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(k) |\n\n**Why:** Heap stores k elements (or two heaps for median).",
        'key_points': ['Pattern: Heap / priority queue', 'Time: O(n log k) worst (O(n log k) best)', 'Space: O(k) auxiliary'],
    },
    "dsa-450-heap-017-rearrange-characters-in-a-string-suc": {
        'explanation': "**Problem:** Rearrange characters in a string such that no two adjacent are same.\n**Pattern:** Heap operations\n**Difficulty:** Medium\n\n**Approach:** Standard Heap approach: identify brute force, then optimize using heap operations typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Build heap O(n) or n extract-min operations O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Heap stores all n elements.",
        'key_points': ['Pattern: Heap operations', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-heap-018-minimum-sum-of-two-numbers-formed-fr": {
        'explanation': "**Problem:** Minimum sum of two numbers formed from digits of an array\n**Pattern:** Heap operations\n**Difficulty:** Medium\n\n**Approach:** Standard Heap approach: identify brute force, then optimize using heap operations typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Build heap O(n) or n extract-min operations O(n log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Heap stores all n elements.",
        'key_points': ['Pattern: Heap operations', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-guide-graph": {
        'explanation': "Adjacency-list BFS/DFS: **O(V + E)**. Grid graphs: **O(rows \u00d7 cols)**. **Topological sort** for dependencies; **Dijkstra** for non-negative shortest paths.\n\nUnion-Find for dynamic connectivity in near **O(\u03b1(n))** per operation.",
        'key_points': ['BFS/DFS: O(V + E)', 'Dijkstra: O((V+E) log V)', 'Topo sort detects DAG cycle', 'Union-Find: O(α(n)) amortized'],
    },
    "dsa-450-graph-001-create-a-graph-print-it": {
        'explanation': "**Problem:** Create a Graph, print it\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-002-implement-bfs-algorithm": {
        'explanation': "**Problem:** Implement BFS algorithm\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-003-implement-dfs-algo": {
        'explanation': "**Problem:** Implement DFS Algo\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-004-detect-cycle-in-directed-graph-using": {
        'explanation': "**Problem:** Detect Cycle in Directed Graph using BFS/DFS Algo\n**Pattern:** Floyd cycle detection\n**Difficulty:** Medium\n\n**Approach:** Slow moves 1 step, fast 2 steps; meeting inside cycle proves loop.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Fast pointer traverses at most 2n nodes before cycle detected.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Two pointer references only.",
        'key_points': ['Pattern: Floyd cycle detection', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-graph-005-detect-cycle-in-undirected-graph-usi": {
        'explanation': "**Problem:** Detect Cycle in UnDirected Graph using BFS/DFS Algo\n**Pattern:** Floyd cycle detection\n**Difficulty:** Medium\n\n**Approach:** Slow moves 1 step, fast 2 steps; meeting inside cycle proves loop.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Fast pointer traverses at most 2n nodes before cycle detected.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Two pointer references only.",
        'key_points': ['Pattern: Floyd cycle detection', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-graph-006-search-in-a-maze": {
        'explanation': "**Problem:** Search in a Maze\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-007-minimum-step-by-knight": {
        'explanation': "**Problem:** Minimum Step by Knight\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-008-flood-fill-algo": {
        'explanation': "**Problem:** flood fill algo\n**Pattern:** Grid DFS/BFS flood fill\n**Difficulty:** Medium\n\n**Approach:** Scan grid; on land start DFS/BFS, mark visited, increment count.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(rows \u00d7 cols) |\n| Average | O(rows \u00d7 cols) |\n| Worst | O(rows \u00d7 cols) |\n\n**Why:** Each cell visited once across all components.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(rows \u00d7 cols) |\n\n**Why:** DFS stack or BFS queue in worst case full grid.",
        'key_points': ['Pattern: Grid DFS/BFS flood fill', 'Time: O(rows × cols) worst (O(rows × cols) best)', 'Space: O(rows × cols) auxiliary'],
    },
    "dsa-450-graph-009-clone-a-graph": {
        'explanation': "**Problem:** Clone a graph\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-010-making-wired-connections": {
        'explanation': "**Problem:** Making wired Connections\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-011-word-ladder": {
        'explanation': "**Problem:** word Ladder\n**Pattern:** BFS on implicit graph\n**Difficulty:** Medium\n\n**Approach:** BFS from startWord; generate neighbors by one-char change.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 wordLen) |\n| Average | O(n \u00d7 wordLen) |\n| Worst | O(n \u00d7 wordLen) |\n\n**Why:** Each word dequeued once; try wordLen character substitutions.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Visited set and BFS queue of words.",
        'key_points': ['Pattern: BFS on implicit graph', 'Time: O(n × wordLen) worst (O(n × wordLen) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-graph-012-dijkstra-algo": {
        'explanation': "**Problem:** Dijkstra algo\n**Pattern:** Shortest path algorithm\n**Difficulty:** Medium\n\n**Approach:** Relax edges from settled nodes; use heap for non-negative weights.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O((V + E) log V) |\n| Average | O((V + E) log V) |\n| Worst | O((V + E) log V) |\n\n**Why:** Dijkstra with min-heap relaxes each edge once. Bellman-Ford O(VE).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Distance array O(V) plus graph/heap storage.",
        'key_points': ['Pattern: Shortest path algorithm', 'Time: O((V + E) log V) worst (O((V + E) log V) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-013-implement-topological-sort": {
        'explanation': "**Problem:** Implement Topological Sort\n**Pattern:** Topological sort (Kahn/DFS colors)\n**Difficulty:** Medium\n\n**Approach:** Kahn BFS peel zero-indegree nodes or DFS 3-color cycle detection.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Adjacency list, indegree array, and queue/stack.",
        'key_points': ['Pattern: Topological sort (Kahn/DFS colors)', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-014-minimum-time-taken-by-each-job-to-be": {
        'explanation': "**Problem:** Minimum time taken by each job to be completed given by a Directed Acyclic Graph\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-015-find-whether-it-is-possible-to-finis": {
        'explanation': "**Problem:** Find whether it is possible to finish all tasks or not from given dependencies\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-016-find-the-no-of-isalnds": {
        'explanation': "**Problem:** Find the no. of Isalnds\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-017-given-a-sorted-dictionary-of-an-alie": {
        'explanation': "**Problem:** Given a sorted Dictionary of an Alien Language, find order of characters\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-018-implement-kruksal-salgorithm": {
        'explanation': "**Problem:** Implement Kruksal\u2019sAlgorithm\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-019-implement-prim-s-algorithm": {
        'explanation': "**Problem:** Implement Prim\u2019s Algorithm\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-020-total-no-of-spanning-tree-in-a-graph": {
        'explanation': "**Problem:** Total no. of Spanning tree in a graph\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-021-implement-bellman-ford-algorithm": {
        'explanation': "**Problem:** Implement Bellman Ford Algorithm\n**Pattern:** Shortest path algorithm\n**Difficulty:** Medium\n\n**Approach:** Relax edges from settled nodes; use heap for non-negative weights.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O((V + E) log V) |\n| Average | O((V + E) log V) |\n| Worst | O((V + E) log V) |\n\n**Why:** Dijkstra with min-heap relaxes each edge once. Bellman-Ford O(VE).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Distance array O(V) plus graph/heap storage.",
        'key_points': ['Pattern: Shortest path algorithm', 'Time: O((V + E) log V) worst (O((V + E) log V) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-022-implement-floyd-warshallalgorithm": {
        'explanation': "**Problem:** Implement Floyd warshallAlgorithm\n**Pattern:** Floyd cycle detection\n**Difficulty:** Medium\n\n**Approach:** Slow moves 1 step, fast 2 steps; meeting inside cycle proves loop.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Fast pointer traverses at most 2n nodes before cycle detected.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Two pointer references only.",
        'key_points': ['Pattern: Floyd cycle detection', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-graph-023-travelling-salesman-problem": {
        'explanation': "**Problem:** Travelling Salesman Problem\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-024-graph-colouringproblem": {
        'explanation': "**Problem:** Graph ColouringProblem\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-025-snake-and-ladders-problem": {
        'explanation': "**Problem:** Snake and Ladders Problem\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-026-find-bridge-in-a-graph": {
        'explanation': "**Problem:** Find bridge in a graph\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-027-count-strongly-connected-components": {
        'explanation': "**Problem:** Count Strongly connected Components(Kosaraju Algo)\n**Pattern:** Grid DFS/BFS flood fill\n**Difficulty:** Medium\n\n**Approach:** Scan grid; on land start DFS/BFS, mark visited, increment count.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(rows \u00d7 cols) |\n| Average | O(rows \u00d7 cols) |\n| Worst | O(rows \u00d7 cols) |\n\n**Why:** Each cell visited once across all components.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(rows \u00d7 cols) |\n\n**Why:** DFS stack or BFS queue in worst case full grid.",
        'key_points': ['Pattern: Grid DFS/BFS flood fill', 'Time: O(rows × cols) worst (O(rows × cols) best)', 'Space: O(rows × cols) auxiliary'],
    },
    "dsa-450-graph-028-check-whether-a-graph-is-bipartite-o": {
        'explanation': "**Problem:** Check whether a graph is Bipartite or Not\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-029-detect-negative-cycle-in-a-graph": {
        'explanation': "**Problem:** Detect Negative cycle in a graph\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-030-longest-path-in-a-directed-acyclic-g": {
        'explanation': "**Problem:** Longest path in a Directed Acyclic Graph\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-031-journey-to-the-moon": {
        'explanation': "**Problem:** Journey to the Moon\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-032-cheapest-flights-within-k-stops": {
        'explanation': "**Problem:** Cheapest Flights Within K Stops\n**Pattern:** Heap / priority queue\n**Difficulty:** Medium\n\n**Approach:** Min-heap of size k for kth largest; balance two heaps for median.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log k) |\n| Average | O(n log k) |\n| Worst | O(n log k) |\n\n**Why:** Maintain size-k heap: n inserts each O(log k).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(k) |\n\n**Why:** Heap stores k elements (or two heaps for median).",
        'key_points': ['Pattern: Heap / priority queue', 'Time: O(n log k) worst (O(n log k) best)', 'Space: O(k) auxiliary'],
    },
    "dsa-450-graph-033-oliver-and-the-game": {
        'explanation': "**Problem:** Oliver and the Game\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-034-water-jug-problem-using-bfs": {
        'explanation': "**Problem:** Water Jug problem using BFS\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-035-water-jug-problem-using-bfs": {
        'explanation': "**Problem:** Water Jug problem using BFS\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-036-find-if-there-is-a-path-of-more-than": {
        'explanation': "**Problem:** Find if there is a path of more thank length from a source\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-037-m-colouringproblem": {
        'explanation': "**Problem:** M-ColouringProblem\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-038-minimum-edges-to-reverse-o-make-path": {
        'explanation': "**Problem:** Minimum edges to reverse o make path from source to destination\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-039-paths-to-travel-each-nodes-using-eac": {
        'explanation': "**Problem:** Paths to travel each nodes using each edge(Seven Bridges)\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-040-vertex-cover-problem": {
        'explanation': "**Problem:** Vertex Cover Problem\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-041-chinese-postman-or-route-inspection": {
        'explanation': "**Problem:** Chinese Postman or Route Inspection\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-042-number-of-triangles-in-a-directed-an": {
        'explanation': "**Problem:** Number of Triangles in a Directed and Undirected Graph\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-043-minimise-the-cashflow-among-a-given": {
        'explanation': "**Problem:** Minimise the cashflow among a given set of friends who have borrowed money from each other\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-450-graph-044-two-clique-problem": {
        'explanation': "**Problem:** Two Clique Problem\n**Pattern:** Graph BFS/DFS\n**Difficulty:** Medium\n\n**Approach:** Standard Graph approach: identify brute force, then optimize using graph bfs/dfs typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(V + E) |\n| Average | O(V + E) |\n| Worst | O(V + E) |\n\n**Why:** Each vertex and edge processed once in adjacency list representation.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(V + E) |\n\n**Why:** Visited set, queue/stack, and adjacency storage.",
        'key_points': ['Pattern: Graph BFS/DFS', 'Time: O(V + E) worst (O(V + E) best)', 'Space: O(V + E) auxiliary'],
    },
    "dsa-guide-trie": {
        'explanation': "Trie supports insert/search in **O(m)** per key of length m. Space **O(n \u00d7 m)** for n strings. Beats hash maps when **prefix queries** matter (autocomplete, word search).\n\nCompress paths (radix tree) if memory is tight.",
        'key_points': ['Insert/search: O(m) per key', 'Prefix search natural fit', 'Space: O(n × m) nodes', 'vs hash: prefix wins'],
    },
    "dsa-450-trie-001-construct-a-trie-from-scratch": {
        'explanation': "**Problem:** Construct a trie from scratch\n**Pattern:** Trie traversal\n**Difficulty:** Medium\n\n**Approach:** Walk trie per character; mark end-of-word at terminal node.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(m) |\n| Average | O(m) |\n| Worst | O(m) |\n\n**Why:** m = key length; traverse/create one node per character.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n \u00d7 m) |\n\n**Why:** Trie stores up to n keys of average length m.",
        'key_points': ['Pattern: Trie traversal', 'Time: O(m) worst (O(m) best)', 'Space: O(n × m) auxiliary'],
    },
    "dsa-450-trie-002-find-shortest-unique-prefix-for-ever": {
        'explanation': "**Problem:** Find shortest unique prefix for every word in a given list\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-trie-003-word-break-problem-trie-solution": {
        'explanation': "**Problem:** Word Break Problem | (Trie solution)\n**Pattern:** Trie traversal\n**Difficulty:** Medium\n\n**Approach:** Walk trie per character; mark end-of-word at terminal node.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(m) |\n| Average | O(m) |\n| Worst | O(m) |\n\n**Why:** m = key length; traverse/create one node per character.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n \u00d7 m) |\n\n**Why:** Trie stores up to n keys of average length m.",
        'key_points': ['Pattern: Trie traversal', 'Time: O(m) worst (O(m) best)', 'Space: O(n × m) auxiliary'],
    },
    "dsa-450-trie-004-given-a-sequence-of-words-print-all": {
        'explanation': "**Problem:** Given a sequence of words, print all anagrams together\n**Pattern:** String matching / frequency\n**Difficulty:** Medium\n\n**Approach:** Build LPS for KMP or sliding window char counts for anagram.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n + m) |\n| Average | O(n + m) |\n| Worst | O(n + m) |\n\n**Why:** KMP/Rabin-Karp linear in text n plus pattern m.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(m) |\n\n**Why:** LPS array or rolling hash window size m.",
        'key_points': ['Pattern: String matching / frequency', 'Time: O(n + m) worst (O(n + m) best)', 'Space: O(m) auxiliary'],
    },
    "dsa-450-trie-005-implement-a-phone-directory": {
        'explanation': "**Problem:** Implement a Phone Directory\n**Pattern:** Trie\n**Difficulty:** Medium\n\n**Approach:** Standard Trie approach: identify brute force, then optimize using trie typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(m) |\n| Average | O(m) |\n| Worst | O(m) |\n\n**Why:** m = key length; one step per character.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n \u00d7 m) |\n\n**Why:** Trie nodes for n strings average length m.",
        'key_points': ['Pattern: Trie', 'Time: O(m) worst (O(m) best)', 'Space: O(n × m) auxiliary'],
    },
    "dsa-450-trie-006-print-unique-rows-in-a-given-boolean": {
        'explanation': "**Problem:** Print unique rows in a given boolean matrix\n**Pattern:** Trie\n**Difficulty:** Medium\n\n**Approach:** Standard Trie approach: identify brute force, then optimize using trie typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(m) |\n| Average | O(m) |\n| Worst | O(m) |\n\n**Why:** m = key length; one step per character.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n \u00d7 m) |\n\n**Why:** Trie nodes for n strings average length m.",
        'key_points': ['Pattern: Trie', 'Time: O(m) worst (O(m) best)', 'Space: O(n × m) auxiliary'],
    },
    "dsa-guide-dp": {
        'explanation': "DP = optimal substructure + overlapping subproblems. 1D linear DP often **O(n) time O(1) space** (Fibonacci, house robber). 2D string DP **O(m \u00d7 n)**. Knapsack **O(n \u00d7 W)**.\n\nAlways state state definition, transition, base case, and iteration order.",
        'key_points': ['Define state before coding', '1D rolling: O(n) O(1)', '2D LCS: O(m × n)', 'Knapsack: O(n × W)'],
    },
    "dsa-450-dp-001-coin-changeproblem": {
        'explanation': "**Problem:** Coin ChangeProblem\n**Pattern:** Dynamic programming \u2014 knapsack family\n**Difficulty:** Medium\n\n**Approach:** dp[w] = min/max ways to reach sum w using processed items.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n \u00d7 W) |\n\n**Why:** Fill DP table over n items and capacity/target W.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** 1D rolling DP over target/capacity dimension.",
        'key_points': ['Pattern: Dynamic programming — knapsack family', 'Time: O(n × W) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-002-knapsack-problem": {
        'explanation': "**Problem:** Knapsack Problem\n**Pattern:** Dynamic programming \u2014 knapsack family\n**Difficulty:** Medium\n\n**Approach:** dp[w] = min/max ways to reach sum w using processed items.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n \u00d7 W) |\n\n**Why:** Fill DP table over n items and capacity/target W.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** 1D rolling DP over target/capacity dimension.",
        'key_points': ['Pattern: Dynamic programming — knapsack family', 'Time: O(n × W) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-003-binomial-coefficientproblem": {
        'explanation': "**Problem:** Binomial CoefficientProblem\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-004-permutation-coefficientproblem": {
        'explanation': "**Problem:** Permutation CoefficientProblem\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Choose/explore/unchoose; prune invalid branches early.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Exponential search tree; permutations n!, subsets 2^n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth n plus path/used array.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-dp-005-program-for-nth-catalan-number": {
        'explanation': "**Problem:** Program for nth Catalan Number\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-006-matrix-chain-multiplication": {
        'explanation': "**Problem:** Matrix Chain Multiplication\n**Pattern:** Interval DP\n**Difficulty:** Medium\n\n**Approach:** dp[i][j] = min cost for subproblem [i,j]; iterate by length.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n\u00b3) |\n| Average | O(n\u00b3) |\n| Worst | O(n\u00b3) |\n\n**Why:** Try all split points for every interval length.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n\u00b2) |\n\n**Why:** 2D DP table over interval start/end.",
        'key_points': ['Pattern: Interval DP', 'Time: O(n³) worst (O(n³) best)', 'Space: O(n²) auxiliary'],
    },
    "dsa-450-dp-007-edit-distance": {
        'explanation': "**Problem:** Edit Distance\n**Pattern:** 2D DP on strings\n**Difficulty:** Medium\n\n**Approach:** dp[i][j] from dp[i-1][j], dp[i][j-1], dp[i-1][j-1] based on match.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(m \u00d7 n) |\n| Average | O(m \u00d7 n) |\n| Worst | O(m \u00d7 n) |\n\n**Why:** Fill (m+1)\u00d7(n+1) table comparing each char pair.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(min(m, n)) |\n\n**Why:** Rolling two-row optimization over longer dimension.",
        'key_points': ['Pattern: 2D DP on strings', 'Time: O(m × n) worst (O(m × n) best)', 'Space: O(min(m, n)) auxiliary'],
    },
    "dsa-450-dp-008-subset-sum-problem": {
        'explanation': "**Problem:** Subset Sum Problem\n**Pattern:** Dynamic programming \u2014 knapsack family\n**Difficulty:** Medium\n\n**Approach:** dp[w] = min/max ways to reach sum w using processed items.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n \u00d7 W) |\n\n**Why:** Fill DP table over n items and capacity/target W.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** 1D rolling DP over target/capacity dimension.",
        'key_points': ['Pattern: Dynamic programming — knapsack family', 'Time: O(n × W) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-009-friends-pairing-problem": {
        'explanation': "**Problem:** Friends Pairing Problem\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-010-gold-mine-problem": {
        'explanation': "**Problem:** Gold Mine Problem\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-011-assembly-line-schedulingproblem": {
        'explanation': "**Problem:** Assembly Line SchedulingProblem\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-012-painting-the-fenceproblem": {
        'explanation': "**Problem:** Painting the Fenceproblem\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-013-maximize-the-cut-segments": {
        'explanation': "**Problem:** Maximize The Cut Segments\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-014-longest-common-subsequence": {
        'explanation': "**Problem:** Longest Common Subsequence\n**Pattern:** 2D DP on strings\n**Difficulty:** Medium\n\n**Approach:** dp[i][j] from dp[i-1][j], dp[i][j-1], dp[i-1][j-1] based on match.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(m \u00d7 n) |\n| Average | O(m \u00d7 n) |\n| Worst | O(m \u00d7 n) |\n\n**Why:** Fill (m+1)\u00d7(n+1) table comparing each char pair.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(min(m, n)) |\n\n**Why:** Rolling two-row optimization over longer dimension.",
        'key_points': ['Pattern: 2D DP on strings', 'Time: O(m × n) worst (O(m × n) best)', 'Space: O(min(m, n)) auxiliary'],
    },
    "dsa-450-dp-015-longest-repeated-subsequence": {
        'explanation': "**Problem:** Longest Repeated Subsequence\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-016-longest-increasing-subsequence": {
        'explanation': "**Problem:** Longest Increasing Subsequence\n**Pattern:** Patience sorting / DP\n**Difficulty:** Medium\n\n**Approach:** Replace first tail \u2265 current with binary search; length = LIS.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n log n) |\n| Average | O(n log n) |\n| Worst | O(n log n) |\n\n**Why:** Binary search on tails array for each element.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Tails array length at most n.",
        'key_points': ['Pattern: Patience sorting / DP', 'Time: O(n log n) worst (O(n log n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-dp-017-space-optimized-solution-of-lcs": {
        'explanation': "**Problem:** Space Optimized Solution of LCS\n**Pattern:** 2D DP on strings\n**Difficulty:** Medium\n\n**Approach:** dp[i][j] from dp[i-1][j], dp[i][j-1], dp[i-1][j-1] based on match.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(m \u00d7 n) |\n| Average | O(m \u00d7 n) |\n| Worst | O(m \u00d7 n) |\n\n**Why:** Fill (m+1)\u00d7(n+1) table comparing each char pair.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(min(m, n)) |\n\n**Why:** Rolling two-row optimization over longer dimension.",
        'key_points': ['Pattern: 2D DP on strings', 'Time: O(m × n) worst (O(m × n) best)', 'Space: O(min(m, n)) auxiliary'],
    },
    "dsa-450-dp-018-lcs-longest-common-subsequence-of-th": {
        'explanation': "**Problem:** LCS (Longest Common Subsequence) of three strings\n**Pattern:** 2D DP on strings\n**Difficulty:** Medium\n\n**Approach:** dp[i][j] from dp[i-1][j], dp[i][j-1], dp[i-1][j-1] based on match.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(m \u00d7 n) |\n| Average | O(m \u00d7 n) |\n| Worst | O(m \u00d7 n) |\n\n**Why:** Fill (m+1)\u00d7(n+1) table comparing each char pair.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(min(m, n)) |\n\n**Why:** Rolling two-row optimization over longer dimension.",
        'key_points': ['Pattern: 2D DP on strings', 'Time: O(m × n) worst (O(m × n) best)', 'Space: O(min(m, n)) auxiliary'],
    },
    "dsa-450-dp-019-maximum-sum-increasing-subsequence": {
        'explanation': "**Problem:** Maximum Sum Increasing Subsequence\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-020-count-all-subsequences-having-produc": {
        'explanation': "**Problem:** Count all subsequences having product less than K\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-021-longest-subsequence-such-that-differ": {
        'explanation': "**Problem:** Longest subsequence such that difference between adjacent is one\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-022-maximum-subsequence-sum-such-that-no": {
        'explanation': "**Problem:** Maximum subsequence sum such that no three are consecutive\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-023-egg-dropping-problem": {
        'explanation': "**Problem:** Egg Dropping Problem\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-024-maximum-length-chain-of-pairs": {
        'explanation': "**Problem:** Maximum Length Chain of Pairs\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-025-maximum-size-square-sub-matrix-with": {
        'explanation': "**Problem:** Maximum size square sub-matrix with all 1s\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-026-maximum-sum-of-pairs-with-specific-d": {
        'explanation': "**Problem:** Maximum sum of pairs with specific difference\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-027-min-cost-pathproblem": {
        'explanation': "**Problem:** Min Cost PathProblem\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-028-maximum-difference-of-zeros-and-ones": {
        'explanation': "**Problem:** Maximum difference of zeros and ones in binary string\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-029-minimum-number-of-jumps-to-reach-end": {
        'explanation': "**Problem:** Minimum number of jumps to reach end\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-030-minimum-cost-to-fill-given-weight-in": {
        'explanation': "**Problem:** Minimum cost to fill given weight in a bag\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-031-minimum-removals-from-array-to-make": {
        'explanation': "**Problem:** Minimum removals from array to make max \u2013min <= K\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-032-longest-common-substring": {
        'explanation': "**Problem:** Longest Common Substring\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-033-count-number-of-ways-to-reacha-given": {
        'explanation': "**Problem:** Count number of ways to reacha given score in a game\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-034-count-balanced-binary-trees-of-heigh": {
        'explanation': "**Problem:** Count Balanced Binary Trees of Height h\n**Pattern:** Tree DFS aggregation\n**Difficulty:** Medium\n\n**Approach:** Recurse children; combine left/right results at parent for global optimum.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single post-order pass computes answer at each node once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(h) |\n\n**Why:** Recursion depth equals tree height.",
        'key_points': ['Pattern: Tree DFS aggregation', 'Time: O(n) worst (O(n) best)', 'Space: O(h) auxiliary'],
    },
    "dsa-450-dp-035-largestsum-contiguous-subarray-v-v-v": {
        'explanation': "**Problem:** LargestSum Contiguous Subarray [V>V>V>V IMP ]\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-036-smallest-sum-contiguous-subarray": {
        'explanation': "**Problem:** Smallest sum contiguous subarray\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-037-unbounded-knapsack-repetition-of-ite": {
        'explanation': "**Problem:** Unbounded Knapsack (Repetition of items allowed)\n**Pattern:** Dynamic programming \u2014 knapsack family\n**Difficulty:** Medium\n\n**Approach:** dp[w] = min/max ways to reach sum w using processed items.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n \u00d7 W) |\n\n**Why:** Fill DP table over n items and capacity/target W.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** 1D rolling DP over target/capacity dimension.",
        'key_points': ['Pattern: Dynamic programming — knapsack family', 'Time: O(n × W) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-038-word-break-problem": {
        'explanation': "**Problem:** Word Break Problem\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-039-largest-independent-set-problem": {
        'explanation': "**Problem:** Largest Independent Set Problem\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-040-partition-problem": {
        'explanation': "**Problem:** Partition problem\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-041-longest-palindromic-subsequence": {
        'explanation': "**Problem:** Longest Palindromic Subsequence\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-042-count-all-palindromic-subsequence-in": {
        'explanation': "**Problem:** Count All Palindromic Subsequence in a given String\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-043-longest-palindromic-substring": {
        'explanation': "**Problem:** Longest Palindromic Substring\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-044-longest-alternating-subsequence": {
        'explanation': "**Problem:** Longest alternating subsequence\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-045-weighted-job-scheduling": {
        'explanation': "**Problem:** Weighted Job Scheduling\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-046-coin-game-winner-where-every-player": {
        'explanation': "**Problem:** Coin game winner where every player has three choices\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-047-count-derangements-permutation-such": {
        'explanation': "**Problem:** Count Derangements (Permutation such that no element appears in its original position) [ IMPORTANT ]\n**Pattern:** Backtracking\n**Difficulty:** Medium\n\n**Approach:** Choose/explore/unchoose; prune invalid branches early.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(2^n) |\n| Average | O(2^n) |\n| Worst | O(n!) |\n\n**Why:** Exponential search tree; permutations n!, subsets 2^n.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(n) |\n\n**Why:** Recursion depth n plus path/used array.",
        'key_points': ['Pattern: Backtracking', 'Time: O(n!) worst (O(2^n) best)', 'Space: O(n) auxiliary'],
    },
    "dsa-450-dp-048-maximum-profit-by-buying-and-selling": {
        'explanation': "**Problem:** Maximum profit by buying and selling a share at most twice [ IMP ]\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-049-optimal-strategy-for-a-game": {
        'explanation': "**Problem:** Optimal Strategy for a Game\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-050-optimal-binary-search-tree": {
        'explanation': "**Problem:** Optimal Binary Search Tree\n**Pattern:** Binary search\n**Difficulty:** Medium\n\n**Approach:** Maintain left/right bounds; compare mid and discard half.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(log n) |\n| Average | O(log n) |\n| Worst | O(log n) |\n\n**Why:** Halve search space each iteration on sorted/monotonic data.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Iterative binary search uses constant pointers.",
        'key_points': ['Pattern: Binary search', 'Time: O(log n) worst (O(log n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-dp-051-palindrome-partitioningproblem": {
        'explanation': "**Problem:** Palindrome PartitioningProblem\n**Pattern:** Two pointers\n**Difficulty:** Medium\n\n**Approach:** Place pointers at ends or both at start; move based on comparison/greedy rule.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Pointers move monotonically across array/string once.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Only index pointers and scalar trackers.",
        'key_points': ['Pattern: Two pointers', 'Time: O(n) worst (O(n) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-dp-052-word-wrap-problem": {
        'explanation': "**Problem:** Word Wrap Problem\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-053-mobile-numeric-keypad-problem-imp": {
        'explanation': "**Problem:** Mobile Numeric Keypad Problem [ IMP ]\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-054-boolean-parenthesization-problem": {
        'explanation': "**Problem:** Boolean Parenthesization Problem\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-055-largest-rectangular-sub-matrix-whose": {
        'explanation': "**Problem:** Largest rectangular sub-matrix whose sum is 0\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-056-largest-area-rectangular-sub-matrix": {
        'explanation': "**Problem:** Largest area rectangular sub-matrix with equal number of 1\u2019s and 0\u2019s [ IMP ]\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-057-maximum-sum-rectangle-in-a-2d-matrix": {
        'explanation': "**Problem:** Maximum sum rectangle in a 2D matrix\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-058-maximum-profit-by-buying-and-selling": {
        'explanation': "**Problem:** Maximum profit by buying and selling a share at most k times\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-059-find-if-a-string-is-interleaved-of-t": {
        'explanation': "**Problem:** Find if a string is interleaved of two other strings\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-450-dp-060-maximum-length-of-pair-chain": {
        'explanation': "**Problem:** Maximum Length of Pair Chain\n**Pattern:** Dynamic programming\n**Difficulty:** Medium\n\n**Approach:** Standard Dynamic Programming approach: identify brute force, then optimize using dynamic programming typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(n \u00d7 W) |\n| Average | O(n \u00d7 W) |\n| Worst | O(n\u00b2) |\n\n**Why:** Depends on state dimensions: 1D O(n), 2D O(n\u00b2), knapsack O(n\u00d7W).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(W) |\n\n**Why:** Often optimized to 1D rolling array over target/capacity.",
        'key_points': ['Pattern: Dynamic programming', 'Time: O(n²) worst (O(n × W) best)', 'Space: O(W) auxiliary'],
    },
    "dsa-guide-bit-manipulation": {
        'explanation': "Bit tricks run in **O(1)** or **O(log n)** word operations. **XOR** finds single unique; **n & (n-1)** clears lowest set bit (Brian Kernighan).\n\nPower set via bits: **O(2^n \u00d7 n)** to enumerate all subsets.",
        'key_points': ['XOR cancels pairs', 'n & (n-1) clears lowest bit', 'Check power of 2: n & (n-1) == 0', 'Subset bitmask: O(2^n)'],
    },
    "dsa-450-bit-manipulation-001-count-set-bits-in-an-integer": {
        'explanation': "**Problem:** Count set bits in an integer\n**Pattern:** Bit manipulation\n**Difficulty:** Medium\n\n**Approach:** Use AND/OR/XOR/shifts; Brian Kernighan for set bits.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(1) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single ops O(1); scanning all bits/elements O(n) or O(log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Bit tricks use constant extra variables.",
        'key_points': ['Pattern: Bit manipulation', 'Time: O(n) worst (O(1) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-bit-manipulation-002-find-the-two-non-repeating-elements": {
        'explanation': "**Problem:** Find the two non-repeating elements in an array of repeating elements\n**Pattern:** Bit tricks\n**Difficulty:** Medium\n\n**Approach:** Standard Bit Manipulation approach: identify brute force, then optimize using bit tricks typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(1) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Word-level ops O(1); bit iteration O(log n) or O(n) bits.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra variables for XOR/AND/shift patterns.",
        'key_points': ['Pattern: Bit tricks', 'Time: O(n) worst (O(1) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-bit-manipulation-003-count-number-of-bits-to-be-flipped-t": {
        'explanation': "**Problem:** Count number of bits to be flipped to convert A to B\n**Pattern:** Bit tricks\n**Difficulty:** Medium\n\n**Approach:** Standard Bit Manipulation approach: identify brute force, then optimize using bit tricks typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(1) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Word-level ops O(1); bit iteration O(log n) or O(n) bits.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra variables for XOR/AND/shift patterns.",
        'key_points': ['Pattern: Bit tricks', 'Time: O(n) worst (O(1) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-bit-manipulation-004-count-total-set-bits-in-all-numbers": {
        'explanation': "**Problem:** Count total set bits in all numbers from 1 to n\n**Pattern:** Bit tricks\n**Difficulty:** Medium\n\n**Approach:** Standard Bit Manipulation approach: identify brute force, then optimize using bit tricks typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(1) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Word-level ops O(1); bit iteration O(log n) or O(n) bits.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra variables for XOR/AND/shift patterns.",
        'key_points': ['Pattern: Bit tricks', 'Time: O(n) worst (O(1) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-bit-manipulation-005-program-to-find-whether-a-no-is-powe": {
        'explanation': "**Problem:** Program to find whether a no is power of two\n**Pattern:** Bit manipulation\n**Difficulty:** Medium\n\n**Approach:** Use AND/OR/XOR/shifts; Brian Kernighan for set bits.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(1) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single ops O(1); scanning all bits/elements O(n) or O(log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Bit tricks use constant extra variables.",
        'key_points': ['Pattern: Bit manipulation', 'Time: O(n) worst (O(1) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-bit-manipulation-006-find-position-of-the-only-set-bit": {
        'explanation': "**Problem:** Find position of the only set bit\n**Pattern:** Bit tricks\n**Difficulty:** Medium\n\n**Approach:** Standard Bit Manipulation approach: identify brute force, then optimize using bit tricks typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(1) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Word-level ops O(1); bit iteration O(log n) or O(n) bits.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra variables for XOR/AND/shift patterns.",
        'key_points': ['Pattern: Bit tricks', 'Time: O(n) worst (O(1) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-bit-manipulation-007-copy-set-bits-in-a-range": {
        'explanation': "**Problem:** Copy set bits in a range\n**Pattern:** Bit tricks\n**Difficulty:** Medium\n\n**Approach:** Standard Bit Manipulation approach: identify brute force, then optimize using bit tricks typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(1) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Word-level ops O(1); bit iteration O(log n) or O(n) bits.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra variables for XOR/AND/shift patterns.",
        'key_points': ['Pattern: Bit tricks', 'Time: O(n) worst (O(1) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-bit-manipulation-008-divide-two-integers-without-using-mu": {
        'explanation': "**Problem:** Divide two integers without using multiplication, division and mod operator\n**Pattern:** Bit tricks\n**Difficulty:** Medium\n\n**Approach:** Standard Bit Manipulation approach: identify brute force, then optimize using bit tricks typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(1) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Word-level ops O(1); bit iteration O(log n) or O(n) bits.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra variables for XOR/AND/shift patterns.",
        'key_points': ['Pattern: Bit tricks', 'Time: O(n) worst (O(1) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-bit-manipulation-009-calculate-square-of-a-number-without": {
        'explanation': "**Problem:** Calculate square of a number without using *, / and pow()\n**Pattern:** Bit tricks\n**Difficulty:** Medium\n\n**Approach:** Standard Bit Manipulation approach: identify brute force, then optimize using bit tricks typical for this category.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(1) |\n| Average | O(log n) |\n| Worst | O(n) |\n\n**Why:** Word-level ops O(1); bit iteration O(log n) or O(n) bits.\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Constant extra variables for XOR/AND/shift patterns.",
        'key_points': ['Pattern: Bit tricks', 'Time: O(n) worst (O(1) best)', 'Space: O(1) auxiliary'],
    },
    "dsa-450-bit-manipulation-010-power-set": {
        'explanation': "**Problem:** Power Set\n**Pattern:** Bit manipulation\n**Difficulty:** Medium\n\n**Approach:** Use AND/OR/XOR/shifts; Brian Kernighan for set bits.\n\n### Time Complexity\n| Case | Complexity |\n| Best | O(1) |\n| Average | O(n) |\n| Worst | O(n) |\n\n**Why:** Single ops O(1); scanning all bits/elements O(n) or O(log n).\n\n### Space Complexity\n| Type | Complexity |\n| Auxiliary | O(1) |\n\n**Why:** Bit tricks use constant extra variables.",
        'key_points': ['Pattern: Bit manipulation', 'Time: O(n) worst (O(1) best)', 'Space: O(1) auxiliary'],
    },
}
