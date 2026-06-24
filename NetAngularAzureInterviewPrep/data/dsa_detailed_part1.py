"""Detailed explanations and C# solutions for DSA section (items 1–25)."""

DSA_DETAILED_PART1: dict[str, dict] = {
    "dsa-two-sum": {
        "explanation": (
            "**Problem:** Given `int[] nums` and `target`, return indices of two numbers that sum to `target`. "
            "Exactly one solution exists; don't reuse the same element.\n\n"
            "**Approach:** One-pass hash map. For each `nums[i]`, check if `target - nums[i]` was seen. "
            "Store value → index as you go.\n\n"
            "**Complexity:** O(n) time, O(n) space."
        ),
        "code": """// LeetCode 1 — Two Sum
public int[] TwoSum(int[] nums, int target)
{
    var seen = new Dictionary<int, int>(); // value → index
    for (int i = 0; i < nums.Length; i++)
    {
        int need = target - nums[i];
        if (seen.TryGetValue(need, out int j))
            return new[] { j, i };
        seen[nums[i]] = i;
    }
    return Array.Empty<int>();
}

// nums = [2,7,11,15], target = 9 → [0,1]""",
        "key_points": ["Hash map one-pass", "O(n) time", "Return indices not values", "Don't reuse same index"],
    },
    "dsa-contains-duplicate": {
        "explanation": (
            "**Problem:** Return true if any value appears at least twice.\n\n"
            "**Approach:** Add each number to a `HashSet`. If `Add` returns false, duplicate found.\n\n"
            "**Complexity:** O(n) time, O(n) space. Sorting alternative: O(n log n) time, O(1) extra if in-place."
        ),
        "code": """public bool ContainsDuplicate(int[] nums)
{
    var set = new HashSet<int>();
    foreach (int n in nums)
        if (!set.Add(n)) return true;
    return false;
}""",
        "key_points": ["HashSet.Add returns false on duplicate", "O(n)", "Sort alternative for O(1) space"],
    },
    "dsa-product-except-self": {
        "explanation": (
            "**Problem:** Return array `answer` where `answer[i]` is product of all elements except `nums[i]`. "
            "No division allowed; O(n) time, O(1) extra space (output excluded).\n\n"
            "**Approach:** First pass left→right: `answer[i] = product of nums[0..i-1]`. "
            "Second pass right→left: multiply by product of nums[i+1..n-1] using running suffix.\n\n"
            "**Complexity:** O(n) time, O(1) extra."
        ),
        "code": """public int[] ProductExceptSelf(int[] nums)
{
    int n = nums.Length;
    var ans = new int[n];
    ans[0] = 1;
    for (int i = 1; i < n; i++)
        ans[i] = ans[i - 1] * nums[i - 1]; // prefix products

    int suffix = 1;
    for (int i = n - 1; i >= 0; i--)
    {
        ans[i] *= suffix;
        suffix *= nums[i];
    }
    return ans;
}""",
        "key_points": ["Prefix then suffix pass", "No division", "O(1) extra space"],
    },
    "dsa-max-subarray": {
        "explanation": (
            "**Problem:** Find contiguous subarray with largest sum (Kadane's algorithm).\n\n"
            "**Approach:** Track `currentSum` ending at index i. Either extend previous subarray or start fresh at `nums[i]`. "
            "`maxSum = max(maxSum, currentSum)`.\n\n"
            "**Complexity:** O(n) time, O(1) space."
        ),
        "code": """public int MaxSubArray(int[] nums)
{
    int current = nums[0], best = nums[0];
    for (int i = 1; i < nums.Length; i++)
    {
        current = Math.Max(nums[i], current + nums[i]);
        best = Math.Max(best, current);
    }
    return best;
}
// [-2,1,-3,4,-1,2,1,-5,4] → 6 (subarray [4,-1,2,1])""",
        "key_points": ["Kadane's algorithm", "Extend or restart", "Handles all-negative arrays"],
    },
    "dsa-merge-intervals": {
        "explanation": (
            "**Problem:** Merge all overlapping intervals.\n\n"
            "**Approach:** Sort by start. Iterate: if current overlaps last merged (start ≤ last.end), extend end; "
            "else append new interval.\n\n"
            "**Complexity:** O(n log n) sort, O(n) merge."
        ),
        "code": """public int[][] Merge(int[][] intervals)
{
    Array.Sort(intervals, (a, b) => a[0].CompareTo(b[0]));
    var merged = new List<int[]>();
    foreach (var iv in intervals)
    {
        if (merged.Count == 0 || iv[0] > merged[^1][1])
            merged.Add(new[] { iv[0], iv[1] });
        else
            merged[^1][1] = Math.Max(merged[^1][1], iv[1]);
    }
    return merged.ToArray();
}""",
        "key_points": ["Sort by start", "Overlap: start ≤ last.end", "Extend end with Max"],
    },
    "dsa-group-anagrams": {
        "explanation": (
            "**Problem:** Group strings that are anagrams of each other.\n\n"
            "**Approach:** Canonical key per string — sorted chars or 26-char frequency count. "
            "Bucket into `Dictionary<string, List<string>>`.\n\n"
            "**Complexity:** O(n · k log k) with sort key (k = max string length)."
        ),
        "code": """public IList<IList<string>> GroupAnagrams(string[] strs)
{
    var map = new Dictionary<string, List<string>>();
    foreach (string s in strs)
    {
        char[] chars = s.ToCharArray();
        Array.Sort(chars);
        string key = new string(chars);
        if (!map.ContainsKey(key)) map[key] = new List<string>();
        map[key].Add(s);
    }
    return map.Values.Cast<IList<string>>().ToList();
}""",
        "key_points": ["Sorted string as key", "Or char-count key O(n·k)", "Dictionary of lists"],
    },
    "dsa-longest-consecutive": {
        "explanation": (
            "**Problem:** Longest consecutive integer sequence length in unsorted array. O(n) required.\n\n"
            "**Approach:** Put all numbers in `HashSet`. Only start counting from `n` if `n-1` not in set "
            "(sequence start). Walk `n, n+1, n+2...`.\n\n"
            "**Complexity:** O(n) — each element visited at most twice."
        ),
        "code": """public int LongestConsecutive(int[] nums)
{
    var set = nums.ToHashSet();
    int best = 0;
    foreach (int n in set)
    {
        if (set.Contains(n - 1)) continue; // not a sequence start
        int len = 1;
        while (set.Contains(n + len)) len++;
        best = Math.Max(best, len);
    }
    return best;
}""",
        "key_points": ["HashSet O(1) lookup", "Only start at sequence head", "O(n) total"],
    },
    "dsa-valid-palindrome": {
        "explanation": (
            "**Problem:** Is string a palindrome after considering only alphanumeric and ignoring case?\n\n"
            "**Approach:** Two pointers at ends. Skip non-alphanumeric; compare lowercased chars.\n\n"
            "**Complexity:** O(n) time, O(1) space."
        ),
        "code": """public bool IsPalindrome(string s)
{
    int l = 0, r = s.Length - 1;
    while (l < r)
    {
        while (l < r && !char.IsLetterOrDigit(s[l])) l++;
        while (l < r && !char.IsLetterOrDigit(s[r])) r--;
        if (char.ToLowerInvariant(s[l]) != char.ToLowerInvariant(s[r]))
            return false;
        l++; r--;
    }
    return true;
}""",
        "key_points": ["Two pointers", "Skip non-alnum", "ToLowerInvariant"],
    },
    "dsa-two-sum-ii": {
        "explanation": (
            "**Problem:** Sorted array, find 1-based indices of two numbers summing to target. Exactly one solution.\n\n"
            "**Approach:** Left at 0, right at n-1. If sum too small, move left++; too big, move right--.\n\n"
            "**Complexity:** O(n) time, O(1) space."
        ),
        "code": """public int[] TwoSum(int[] numbers, int target)
{
    int l = 0, r = numbers.Length - 1;
    while (l < r)
    {
        int sum = numbers[l] + numbers[r];
        if (sum == target) return new[] { l + 1, r + 1 };
        if (sum < target) l++;
        else r--;
    }
    return Array.Empty<int>();
}""",
        "key_points": ["Sorted → two pointers", "1-based indices", "O(1) space"],
    },
    "dsa-container-water": {
        "explanation": (
            "**Problem:** Vertical lines at heights[i]; max water between two lines.\n\n"
            "**Approach:** Two pointers at ends. Area = min(h[l], h[r]) × (r-l). "
            "Move the shorter line inward (only shorter can improve).\n\n"
            "**Complexity:** O(n) time, O(1) space."
        ),
        "code": """public int MaxArea(int[] height)
{
    int l = 0, r = height.Length - 1, best = 0;
    while (l < r)
    {
        int area = Math.Min(height[l], height[r]) * (r - l);
        best = Math.Max(best, area);
        if (height[l] < height[r]) l++;
        else r--;
    }
    return best;
}""",
        "key_points": ["Move shorter pointer", "Greedy two pointers", "Width shrinks every step"],
    },
    "dsa-trapping-rain": {
        "explanation": (
            "**Problem:** Elevation map — how much rain water is trapped?\n\n"
            "**Approach (two pointers):** Track `leftMax` and `rightMax`. "
            "Process the side with smaller max; water at pointer = max(0, sideMax - height).\n\n"
            "**Complexity:** O(n) time, O(1) space."
        ),
        "code": """public int Trap(int[] height)
{
    int l = 0, r = height.Length - 1, leftMax = 0, rightMax = 0, water = 0;
    while (l < r)
    {
        if (height[l] < height[r])
        {
            leftMax = Math.Max(leftMax, height[l]);
            water += leftMax - height[l];
            l++;
        }
        else
        {
            rightMax = Math.Max(rightMax, height[r]);
            water += rightMax - height[r];
            r--;
        }
    }
    return water;
}""",
        "key_points": ["Two pointers", "Process smaller max side", "Prefix max alternative O(n) space"],
    },
    "dsa-longest-substring": {
        "explanation": (
            "**Problem:** Length of longest substring without repeating characters.\n\n"
            "**Approach:** Sliding window [l, r]. Expand r, track char index in map. "
            "If char seen in window, move l past last occurrence.\n\n"
            "**Complexity:** O(n) time, O(min(n, alphabet)) space."
        ),
        "code": """public int LengthOfLongestSubstring(string s)
{
    var last = new Dictionary<char, int>();
    int l = 0, best = 0;
    for (int r = 0; r < s.Length; r++)
    {
        if (last.TryGetValue(s[r], out int prev) && prev >= l)
            l = prev + 1;
        last[s[r]] = r;
        best = Math.Max(best, r - l + 1);
    }
    return best;
}""",
        "key_points": ["Sliding window", "Hash map last index", "Move l on duplicate"],
    },
    "dsa-min-window-substring": {
        "explanation": (
            "**Problem:** Smallest substring of `s` containing all characters of `t` (including frequency).\n\n"
            "**Approach:** Expand window until valid (all t chars satisfied), then shrink from left while still valid. "
            "Track `need` and `have` counts.\n\n"
            "**Complexity:** O(|s| + |t|) time."
        ),
        "code": """public string MinWindow(string s, string t)
{
    var need = new Dictionary<char, int>();
    foreach (char c in t) need[c] = need.GetValueOrDefault(c) + 1;

    int have = 0, required = need.Count;
    int l = 0, bestLen = int.MaxValue, bestStart = 0;
    var window = new Dictionary<char, int>();

    for (int r = 0; r < s.Length; r++)
    {
        char c = s[r];
        window[c] = window.GetValueOrDefault(c) + 1;
        if (need.ContainsKey(c) && window[c] == need[c]) have++;

        while (have == required)
        {
            if (r - l + 1 < bestLen) { bestLen = r - l + 1; bestStart = l; }
            char left = s[l++];
            if (need.ContainsKey(left) && window[left]-- == need[left]) have--;
        }
    }
    return bestLen == int.MaxValue ? "" : s.Substring(bestStart, bestLen);
}""",
        "key_points": ["Expand until valid, shrink", "Frequency maps", "Track have vs required"],
    },
    "dsa-sliding-window-max": {
        "explanation": (
            "**Problem:** Max in each sliding window of size k.\n\n"
            "**Approach:** Monotonic deque storing indices (decreasing values). "
            "Front = current max. Drop indices outside window; pop back while ≤ new value.\n\n"
            "**Complexity:** O(n) — each index pushed/popped once."
        ),
        "code": """public int[] MaxSlidingWindow(int[] nums, int k)
{
    var dq = new LinkedList<int>(); // indices, decreasing nums value
    var result = new int[nums.Length - k + 1];

    for (int i = 0; i < nums.Length; i++)
    {
        while (dq.Count > 0 && dq.First!.Value < i - k + 1)
            dq.RemoveFirst();
        while (dq.Count > 0 && nums[dq.Last!.Value] <= nums[i])
            dq.RemoveLast();
        dq.AddLast(i);
        if (i >= k - 1) result[i - k + 1] = nums[dq.First!.Value];
    }
    return result;
}""",
        "key_points": ["Monotonic deque", "Store indices not values", "Amortized O(n)"],
    },
    "dsa-max-consecutive-ones": {
        "explanation": (
            "**Problem:** Longest subarray of 1s if you can flip at most k zeros.\n\n"
            "**Approach:** Sliding window counting zeros. When zeros > k, shrink from left.\n\n"
            "**Complexity:** O(n) time, O(1) space."
        ),
        "code": """public int LongestOnes(int[] nums, int k)
{
    int l = 0, zeros = 0, best = 0;
    for (int r = 0; r < nums.Length; r++)
    {
        if (nums[r] == 0) zeros++;
        while (zeros > k)
        {
            if (nums[l] == 0) zeros--;
            l++;
        }
        best = Math.Max(best, r - l + 1);
    }
    return best;
}""",
        "key_points": ["Sliding window on zeros", "Shrink when zeros > k", "Variable window size"],
    },
    "dsa-reverse-linked-list": {
        "explanation": (
            "**Problem:** Reverse singly linked list.\n\n"
            "**Iterative:** Three pointers prev/null, curr, next. "
            "**Recursive:** Reverse rest, point next to current.\n\n"
            "**Complexity:** O(n) time, O(1) iterative space."
        ),
        "code": """public class ListNode { public int val; public ListNode? next; }

public ListNode? ReverseList(ListNode? head)
{
    ListNode? prev = null, curr = head;
    while (curr != null)
    {
        var next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}""",
        "key_points": ["Three-pointer iterative", "Recursive O(n) stack", "Return new head prev"],
    },
    "dsa-merge-two-lists": {
        "explanation": (
            "**Problem:** Merge two sorted linked lists into one sorted list.\n\n"
            "**Approach:** Dummy head sentinel. Compare heads, attach smaller, advance. "
            "Append remainder.\n\n"
            "**Complexity:** O(n + m) time, O(1) space."
        ),
        "code": """public ListNode? MergeTwoLists(ListNode? l1, ListNode? l2)
{
    var dummy = new ListNode();
    var tail = dummy;
    while (l1 != null && l2 != null)
    {
        if (l1.val <= l2.val) { tail.next = l1; l1 = l1.next; }
        else { tail.next = l2; l2 = l2.next; }
        tail = tail.next;
    }
    tail.next = l1 ?? l2;
    return dummy.next;
}""",
        "key_points": ["Dummy node pattern", "Compare and advance", "Append leftover list"],
    },
    "dsa-linked-list-cycle": {
        "explanation": (
            "**Problem:** Does linked list have a cycle?\n\n"
            "**Approach:** Floyd's algorithm — slow moves 1, fast moves 2. Cycle iff they meet.\n\n"
            "**Complexity:** O(n) time, O(1) space."
        ),
        "code": """public bool HasCycle(ListNode? head)
{
    var slow = head;
    var fast = head;
    while (fast?.next != null)
    {
        slow = slow!.next;
        fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
}""",
        "key_points": ["Floyd tortoise & hare", "O(1) space", "Find cycle start: reset slow to head"],
    },
    "dsa-remove-nth-node": {
        "explanation": (
            "**Problem:** Remove the nth node from the end (1-indexed).\n\n"
            "**Approach:** Dummy before head. Advance fast n+1 steps, then move both until fast reaches end. "
            "`slow.next = slow.next.next`.\n\n"
            "**Complexity:** O(n) one pass."
        ),
        "code": """public ListNode? RemoveNthFromEnd(ListNode? head, int n)
{
    var dummy = new ListNode { next = head };
    var slow = dummy;
    var fast = dummy;
    for (int i = 0; i <= n; i++) fast = fast!.next;
    while (fast != null) { slow = slow!.next; fast = fast.next; }
    slow.next = slow.next?.next;
    return dummy.next;
}""",
        "key_points": ["Dummy handles remove head", "n+1 gap between pointers", "Single pass"],
    },
    "dsa-valid-parentheses": {
        "explanation": (
            "**Problem:** Valid if brackets open/close in correct order.\n\n"
            "**Approach:** Stack of opening chars. On closing, pop must match.\n\n"
            "**Complexity:** O(n) time, O(n) space."
        ),
        "code": """public bool IsValid(string s)
{
    var stack = new Stack<char>();
    var pairs = new Dictionary<char, char> { [')']='(', [']']='[', ['}']='{' };
    foreach (char c in s)
    {
        if (pairs.ContainsValue(c)) stack.Push(c);
        else if (stack.Count == 0 || stack.Pop() != pairs[c]) return false;
    }
    return stack.Count == 0;
}""",
        "key_points": ["Stack matching", "Empty stack at end", "Early false on mismatch"],
    },
    "dsa-min-stack": {
        "explanation": (
            "**Problem:** Stack with push, pop, top, getMin — all O(1).\n\n"
            "**Approach:** Store `(value, currentMin)` pairs. On push, new min = min(val, stack min).\n\n"
            "**Complexity:** O(1) per operation, O(n) space."
        ),
        "code": """public class MinStack
{
    private readonly Stack<(int val, int min)> _s = new();

    public void Push(int val) =>
        _s.Push((val, _s.Count == 0 ? val : Math.Min(val, _s.Peek().min)));

    public void Pop() => _s.Pop();
    public int Top() => _s.Peek().val;
    public int GetMin() => _s.Peek().min;
}""",
        "key_points": ["Pair (value, min)", "Or separate min stack", "All O(1)"],
    },
    "dsa-daily-temperatures": {
        "explanation": (
            "**Problem:** For each day, days until a warmer temperature (0 if none).\n\n"
            "**Approach:** Monotonic decreasing stack of indices. When current temp > stack top, "
            "pop and set `answer[pop] = i - pop`.\n\n"
            "**Complexity:** O(n) time."
        ),
        "code": """public int[] DailyTemperatures(int[] temperatures)
{
    int n = temperatures.Length;
    var ans = new int[n];
    var stack = new Stack<int>();
    for (int i = 0; i < n; i++)
    {
        while (stack.Count > 0 && temperatures[i] > temperatures[stack.Peek()])
        {
            int j = stack.Pop();
            ans[j] = i - j;
        }
        stack.Push(i);
    }
    return ans;
}""",
        "key_points": ["Monotonic stack", "Store indices", "Pop when warmer found"],
    },
    "dsa-largest-rectangle": {
        "explanation": (
            "**Problem:** Largest rectangle area in histogram.\n\n"
            "**Approach:** Monotonic increasing stack of indices. On pop, height = heights[popped], "
            "width extends to current index and back to stack top.\n\n"
            "**Complexity:** O(n) time."
        ),
        "code": """public int LargestRectangleArea(int[] heights)
{
    var stack = new Stack<int>();
    int best = 0;
    for (int i = 0; i <= heights.Length; i++)
    {
        int h = i == heights.Length ? 0 : heights[i];
        while (stack.Count > 0 && h < heights[stack.Peek()])
        {
            int height = heights[stack.Pop()];
            int width = stack.Count == 0 ? i : i - stack.Peek() - 1;
            best = Math.Max(best, height * width);
        }
        stack.Push(i);
    }
    return best;
}""",
        "key_points": ["Sentinel height 0 at end", "Width when popping", "Classic monotonic stack"],
    },
    "dsa-max-depth-tree": {
        "explanation": (
            "**Problem:** Maximum depth (height) of binary tree.\n\n"
            "**Approach:** DFS: `1 + max(left, right)`. BFS: count levels.\n\n"
            "**Complexity:** O(n) time."
        ),
        "code": """public class TreeNode { public int val; public TreeNode? left, right; }

public int MaxDepth(TreeNode? root) =>
    root == null ? 0 : 1 + Math.Max(MaxDepth(root.left), MaxDepth(root.right));""",
        "key_points": ["Recursive DFS", "Base null → 0", "BFS level count alternative"],
    },
    "dsa-invert-tree": {
        "explanation": (
            "**Problem:** Mirror the binary tree (swap left/right at every node).\n\n"
            "**Approach:** DFS preorder: swap children, recurse both sides.\n\n"
            "**Complexity:** O(n) time, O(h) stack."
        ),
        "code": """public TreeNode? InvertTree(TreeNode? root)
{
    if (root == null) return null;
    (root.left, root.right) = (root.right, root.left);
    InvertTree(root.left);
    InvertTree(root.right);
    return root;
}""",
        "key_points": ["Swap at each node", "Pre-order DFS", "BFS queue swap works too"],
    },
}
