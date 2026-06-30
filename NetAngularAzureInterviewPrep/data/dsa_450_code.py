"""Generate C# solution code for Love Babbar 450 DSA problems."""

from __future__ import annotations

import re
from typing import Callable

from data.dsa_detailed import DSA_DETAILED


def _header(problem: str, meta: dict) -> str:
    return (
        f"// {problem}\n"
        f"// Pattern: {meta['pattern']}\n"
        f"// Time: {meta['time_worst']} | Space: {meta['space_auxiliary']}\n"
    )


def _method_name(problem: str) -> str:
    words = re.findall(r"[a-z0-9]+", problem.lower())[:5]
    if not words:
        return "Solve"
    name = "".join(w.capitalize() for w in words)
    return name[:48] or "Solve"


# Legacy LeetCode-style solutions mapped by problem-title keywords
_LEGACY_KEYS: list[tuple[str, str]] = [
    (r"largest sum contiguous|kadane", "dsa-max-subarray"),
    (r"merge intervals", "dsa-merge-intervals"),
    (r"group anagram", "dsa-group-anagrams"),
    (r"longest consecutive", "dsa-longest-consecutive"),
    (r"valid palindrome", "dsa-valid-palindrome"),
    (r"container.*water", "dsa-container-water"),
    (r"trapping rain", "dsa-trapping-rain"),
    (r"longest substring without repeating", "dsa-longest-substring"),
    (r"minimum window", "dsa-min-window-substring"),
    (r"sliding window maximum", "dsa-sliding-window-max"),
    (r"reverse.*linked list", "dsa-reverse-linked-list"),
    (r"merge two sorted list", "dsa-merge-two-lists"),
    (r"cycle.*linked list|linked list.*cycle", "dsa-linked-list-cycle"),
    (r"remove nth node|n.?th node from the end", "dsa-remove-nth-node"),
    (r"valid parenthes|balanced parenthes", "dsa-valid-parentheses"),
    (r"min stack|getmin.*o\(1\)", "dsa-min-stack"),
    (r"daily temperature", "dsa-daily-temperatures"),
    (r"largest rectangle|histogram", "dsa-largest-rectangle"),
    (r"max.*depth.*tree|maximum depth", "dsa-max-depth-tree"),
    (r"invert.*tree|mirror.*tree", "dsa-invert-tree"),
    (r"same tree", "dsa-same-tree"),
    (r"lowest common ancestor|lca", "dsa-lca-bst"),
    (r"validate.*bst|check.*bst", "dsa-validate-bst"),
    (r"level order|level-order", "dsa-level-order"),
    (r"number of islands", "dsa-number-of-islands"),
    (r"clone graph", "dsa-clone-graph"),
    (r"course schedule|topological sort", "dsa-course-schedule"),
    (r"rotting orange", "dsa-rotting-oranges"),
    (r"word ladder", "dsa-word-ladder"),
    (r"kth largest|kth max", "dsa-kth-largest"),
    (r"top k frequent|k frequent", "dsa-top-k-frequent"),
    (r"median.*stream", "dsa-find-median-stream"),
    (r"search in rotated|rotated sorted array", "dsa-search-rotated"),
    (r"minimum in rotated|min in rotated", "dsa-min-rotated"),
    (r"climbing stair|count.*ways.*step", "dsa-climbing-stairs"),
    (r"house robber", "dsa-house-robber"),
    (r"coin change", "dsa-coin-change"),
    (r"longest increasing subsequence|\blis\b", "dsa-lis"),
    (r"longest common subsequence|\blcs\b", "dsa-lcs"),
    (r"word break", "dsa-word-break"),
    (r"power set|all subset|subsequence", "dsa-subsets"),
    (r"combination sum", "dsa-combination-sum"),
    (r"permutation", "dsa-permutations"),
    (r"product except self", "dsa-product-except-self"),
    (r"contains duplicate", "dsa-contains-duplicate"),
    (r"two sum", "dsa-two-sum"),
]


def _legacy_code(text: str) -> str | None:
    for pattern, key in _LEGACY_KEYS:
        if re.search(pattern, text, re.I):
            code = DSA_DETAILED.get(key, {}).get("code", "").strip()
            if code:
                return code
    return None


def _code_reverse_array(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public void Reverse(int[] nums)
{
    for (int l = 0, r = nums.Length - 1; l < r; l++, r--)
        (nums[l], nums[r]) = (nums[r], nums[l]);
}"""


def _code_max_min(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public (int min, int max) MinMax(int[] nums)
{
    int min = nums[0], max = nums[0];
    foreach (int n in nums)
    {
        if (n < min) min = n;
        if (n > max) max = n;
    }
    return (min, max);
}"""


def _code_kth_element(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public int FindKthLargest(int[] nums, int k)
{
    // Min-heap of size k — O(n log k)
    var heap = new PriorityQueue<int, int>();
    foreach (int n in nums)
    {
        heap.Enqueue(n, n);
        if (heap.Count > k) heap.Dequeue();
    }
    return heap.Peek();
}"""


def _code_dutch_flag(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public void Sort012(int[] nums)
{
    int lo = 0, mid = 0, hi = nums.Length - 1;
    while (mid <= hi)
    {
        if (nums[mid] == 0) (nums[lo], nums[mid]) = (nums[mid], nums[lo]), lo++, mid++;
        else if (nums[mid] == 1) mid++;
        else (nums[mid], nums[hi]) = (nums[hi], nums[mid]), hi--;
    }
}"""


def _code_union_intersection(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public (int[] union, int[] inter) UnionIntersection(int[] a, int[] b)
{
    int i = 0, j = 0;
    var u = new List<int>(), inter = new List<int>();
    while (i < a.Length && j < b.Length)
    {
        if (a[i] < b[j]) u.Add(a[i++]);
        else if (a[i] > b[j]) u.Add(b[j++]);
        else { u.Add(a[i]); inter.Add(a[i]); i++; j++; }
    }
    while (i < a.Length) u.Add(a[i++]);
    while (j < b.Length) u.Add(b[j++]);
    return (u.ToArray(), inter.ToArray());
}"""


def _code_rotate_array(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public void RotateRight(int[] nums, int k)
{
    k %= nums.Length;
    Reverse(nums, 0, nums.Length - 1);
    Reverse(nums, 0, k - 1);
    Reverse(nums, k, nums.Length - 1);
}

void Reverse(int[] a, int l, int r)
{
    while (l < r) (a[l], a[r]) = (a[r], a[l]), l++, r--;
}"""


def _code_binary_search(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public int BinarySearch(int[] nums, int target)
{
    int lo = 0, hi = nums.Length - 1;
    while (lo <= hi)
    {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] == target) return mid;
        if (nums[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}"""


def _code_merge_sort(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public void MergeSort(int[] a)
{
    if (a.Length <= 1) return;
    int mid = a.Length / 2;
    var left = a[..mid];
    var right = a[mid..];
    MergeSort(left); MergeSort(right);
    Merge(a, left, right);
}

void Merge(int[] a, int[] l, int[] r)
{
    int i = 0, j = 0, k = 0;
    while (i < l.Length && j < r.Length)
        a[k++] = l[i] <= r[j] ? l[i++] : r[j++];
    while (i < l.Length) a[k++] = l[i++];
    while (j < r.Length) a[k++] = r[j++];
}"""


def _code_quick_sort(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public void QuickSort(int[] a, int lo, int hi)
{
    if (lo >= hi) return;
    int p = Partition(a, lo, hi);
    QuickSort(a, lo, p - 1);
    QuickSort(a, p + 1, hi);
}

int Partition(int[] a, int lo, int hi)
{
    int pivot = a[hi], i = lo;
    for (int j = lo; j < hi; j++)
        if (a[j] <= pivot) (a[i], a[j]) = (a[j], a[i]), i++;
    (a[i], a[hi]) = (a[hi], a[i]);
    return i;
}"""


def _code_heap_sort(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public void HeapSort(int[] a)
{
    for (int i = a.Length / 2 - 1; i >= 0; i--) Heapify(a, a.Length, i);
    for (int end = a.Length - 1; end > 0; end--)
    {
        (a[0], a[end]) = (a[end], a[0]);
        Heapify(a, end, 0);
    }
}

void Heapify(int[] a, int n, int i)
{
    int largest = i, l = 2 * i + 1, r = 2 * i + 2;
    if (l < n && a[l] > a[largest]) largest = l;
    if (r < n && a[r] > a[largest]) largest = r;
    if (largest != i)
    {
        (a[i], a[largest]) = (a[largest], a[i]);
        Heapify(a, n, largest);
    }
}"""


def _code_hash_map(problem: str, meta: dict) -> str:
    m = _method_name(problem)
    return _header(problem, meta) + f"""public int {m}(int[] nums)
{{
    var freq = new Dictionary<int, int>();
    foreach (int n in nums)
        freq[n] = freq.GetValueOrDefault(n) + 1;
    // Use frequency map / complement lookup per problem constraints
    return 0;
}}"""


def _code_sliding_window(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public int LongestWindow(string s)
{
    var seen = new Dictionary<char, int>();
    int best = 0, left = 0;
    for (int right = 0; right < s.Length; right++)
    {
        if (seen.TryGetValue(s[right], out int idx))
            left = Math.Max(left, idx + 1);
        seen[s[right]] = right;
        best = Math.Max(best, right - left + 1);
    }
    return best;
}"""


def _code_two_pointers(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public int TwoPointers(int[] nums)
{
    int left = 0, right = nums.Length - 1, ans = 0;
    while (left < right)
    {
        // Update answer from nums[left] and nums[right]
        if (/* move left */) left++;
        else right--;
    }
    return ans;
}"""


def _code_linked_list_node(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public class ListNode
{
    public int val;
    public ListNode? next;
    public ListNode(int val = 0, ListNode? next = null) => (this.val, this.next) = (val, next);
}

public ListNode? ReverseList(ListNode? head)
{
    ListNode? prev = null;
    while (head != null)
    {
        var next = head.next;
        head.next = prev;
        prev = head;
        head = next;
    }
    return prev;
}"""


def _code_tree_node(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public class TreeNode
{
    public int val;
    public TreeNode? left, right;
    public TreeNode(int val = 0, TreeNode? left = null, TreeNode? right = null)
        => (this.val, this.left, this.right) = (val, left, right);
}

public IList<int> Inorder(TreeNode? root)
{
    var res = new List<int>();
    void Dfs(TreeNode? n)
    {
        if (n == null) return;
        Dfs(n.left);
        res.Add(n.val);
        Dfs(n.right);
    }
    Dfs(root);
    return res;
}"""


def _code_bfs_graph(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public int Bfs(int start, List<int>[] graph)
{
    var q = new Queue<int>();
    var seen = new HashSet<int> { start };
    q.Enqueue(start);
    int depth = 0;
    while (q.Count > 0)
    {
        int size = q.Count;
        for (int i = 0; i < size; i++)
        {
            int u = q.Dequeue();
            foreach (int v in graph[u])
                if (seen.Add(v)) q.Enqueue(v);
        }
        depth++;
    }
    return depth;
}"""


def _code_dfs_graph(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public void Dfs(int u, List<int>[] graph, bool[] seen)
{
    seen[u] = true;
    foreach (int v in graph[u])
        if (!seen[v]) Dfs(v, graph, seen);
}

public int CountComponents(int n, List<int>[] graph)
{
    var seen = new bool[n];
    int comps = 0;
    for (int i = 0; i < n; i++)
        if (!seen[i]) { Dfs(i, graph, seen); comps++; }
    return comps;
}"""


def _code_dijkstra(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public int[] Dijkstra(int n, List<(int to, int w)>[] graph, int src)
{
    var dist = Enumerable.Repeat(int.MaxValue, n).ToArray();
    dist[src] = 0;
    var pq = new PriorityQueue<int, int>();
    pq.Enqueue(src, 0);
    while (pq.Count > 0)
    {
        pq.TryDequeue(out int u, out int d);
        if (d > dist[u]) continue;
        foreach (var (v, w) in graph[u])
        {
            int nd = d + w;
            if (nd < dist[v]) { dist[v] = nd; pq.Enqueue(v, nd); }
        }
    }
    return dist;
}"""


def _code_dp_knapsack(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public int CoinChange(int[] coins, int amount)
{
    var dp = Enumerable.Repeat(amount + 1, amount + 1).ToArray();
    dp[0] = 0;
    for (int a = 1; a <= amount; a++)
        foreach (int c in coins)
            if (c <= a) dp[a] = Math.Min(dp[a], dp[a - c] + 1);
    return dp[amount] > amount ? -1 : dp[amount];
}"""


def _code_dp_lcs(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public int Lcs(string a, string b)
{
    int m = a.Length, n = b.Length;
    var dp = new int[m + 1, n + 1];
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++)
            dp[i, j] = a[i - 1] == b[j - 1]
                ? dp[i - 1, j - 1] + 1
                : Math.Max(dp[i - 1, j], dp[i, j - 1]);
    return dp[m, n];
}"""


def _code_backtrack(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public IList<IList<int>> Subsets(int[] nums)
{
    var res = new List<IList<int>>();
    void Dfs(int i, List<int> path)
    {
        res.Add(new List<int>(path));
        for (int j = i; j < nums.Length; j++)
        {
            path.Add(nums[j]);
            Dfs(j + 1, path);
            path.RemoveAt(path.Count - 1);
        }
    }
    Dfs(0, new List<int>());
    return res;
}"""


def _code_trie(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public class Trie
{
    private readonly Trie[] _next = new Trie[26];
    private bool _end;

    public void Insert(string word)
    {
        var node = this;
        foreach (char c in word)
        {
            int i = c - 'a';
            node._next[i] ??= new Trie();
            node = node._next[i];
        }
        node._end = true;
    }

    public bool Search(string word)
    {
        var node = this;
        foreach (char c in word)
        {
            int i = c - 'a';
            if (node._next[i] == null) return false;
            node = node._next[i];
        }
        return node._end;
    }
}"""


def _code_bit(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public int SingleNumber(int[] nums)
{
    int x = 0;
    foreach (int n in nums) x ^= n; // XOR cancels pairs
    return x;
}

public int CountSetBits(int n)
{
    int count = 0;
    while (n != 0) { n &= n - 1; count++; } // Brian Kernighan
    return count;
}"""


def _code_matrix(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public void SpiralOrder(int[][] matrix)
{
    int top = 0, bottom = matrix.Length - 1;
    int left = 0, right = matrix[0].Length - 1;
    var res = new List<int>();
    while (top <= bottom && left <= right)
    {
        for (int c = left; c <= right; c++) res.Add(matrix[top][c]);
        top++;
        for (int r = top; r <= bottom; r++) res.Add(matrix[r][right]);
        right--;
        if (top <= bottom)
        {
            for (int c = right; c >= left; c--) res.Add(matrix[bottom][c]);
            bottom--;
        }
        if (left <= right)
        {
            for (int r = bottom; r >= top; r--) res.Add(matrix[r][left]);
            left++;
        }
    }
}"""


def _code_stack(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public bool IsValidParentheses(string s)
{
    var stack = new Stack<char>();
    foreach (char c in s)
    {
        if (c is '(' or '[' or '{') stack.Push(c);
        else
        {
            if (stack.Count == 0) return false;
            char o = stack.Pop();
            if (c == ')' && o != '(' || c == ']' && o != '[' || c == '}' && o != '{')
                return false;
        }
    }
    return stack.Count == 0;
}"""


def _code_monotonic_stack(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public int[] NextGreater(int[] nums)
{
    var res = new int[nums.Length];
    Array.Fill(res, -1);
    var st = new Stack<int>();
    for (int i = 0; i < nums.Length; i++)
    {
        while (st.Count > 0 && nums[i] > nums[st.Peek()])
            res[st.Pop()] = nums[i];
        st.Push(i);
    }
    return res;
}"""


def _code_greedy(problem: str, meta: dict) -> str:
    return _header(problem, meta) + """public int ActivitySelection(int[][] intervals)
{
    Array.Sort(intervals, (a, b) => a[1].CompareTo(b[1])); // sort by finish time
    int count = 0, lastEnd = int.MinValue;
    foreach (var iv in intervals)
        if (iv[0] >= lastEnd) { count++; lastEnd = iv[1]; }
    return count;
}"""


# (regex, generator) — first match wins after legacy lookup
_CODE_RULES: list[tuple[str, Callable[[str, dict], str]]] = [
    (r"reverse the array|reverse an array", _code_reverse_array),
    (r"maximum and minimum|max and min|max.*min element", _code_max_min),
    (r"kth.*max|kth.*min|kth largest|kth smallest", _code_kth_element),
    (r"0.*1.*2|three color|dutch", _code_dutch_flag),
    (r"union.*intersection|intersection.*union", _code_union_intersection),
    (r"rotate.*array|cyclically rotate", _code_rotate_array),
    (r"binary search|search.*sorted", _code_binary_search),
    (r"merge sort", _code_merge_sort),
    (r"quick sort|quicksort", _code_quick_sort),
    (r"heap sort|heapsort|sort.*heap", _code_heap_sort),
    (r"sliding window|smallest window|longest substring", _code_sliding_window),
    (r"two pointer|palindrome.*string|container.*water", _code_two_pointers),
    (r"linked list|linkedlist", _code_linked_list_node),
    (r"binary tree|bst|tree node|inorder|preorder|postorder", _code_tree_node),
    (r"dijkstra", _code_dijkstra),
    (r"\bbfs\b|breadth first|level order", _code_bfs_graph),
    (r"\bdfs\b|depth first|connected component", _code_dfs_graph),
    (r"knapsack|coin change|subset sum", _code_dp_knapsack),
    (r"longest common subsequence|\blcs\b", _code_dp_lcs),
    (r"backtrack|subset|permutation|n.?queen|maze|sudoku", _code_backtrack),
    (r"trie|prefix tree", _code_trie),
    (r"bit manip|set bit|power of two|xor|power set", _code_bit),
    (r"matrix|2d array|spiral|row.*column", _code_matrix),
    (r"parenthes|stack", _code_stack),
    (r"next greater|monotonic|histogram|stock span", _code_monotonic_stack),
    (r"greedy|activity selection|fractional", _code_greedy),
    (r"hash|frequency|anagram|duplicate|count.*element", _code_hash_map),
]

_PATTERN_FALLBACK: dict[str, Callable[[str, dict], str]] = {
    "Hash map one-pass": _code_hash_map,
    "Hash map / frequency count": _code_hash_map,
    "Binary search": _code_binary_search,
    "Sliding window": _code_sliding_window,
    "Two pointers": _code_two_pointers,
    "Iterative/recursive reversal": _code_linked_list_node,
    "Floyd cycle detection": _code_linked_list_node,
    "Stack matching": _code_stack,
    "Monotonic stack": _code_monotonic_stack,
    "BFS level-order traversal": _code_bfs_graph,
    "Tree DFS aggregation": _code_tree_node,
    "Grid DFS/BFS flood fill": _code_matrix,
    "Topological sort (Kahn/DFS colors)": _code_bfs_graph,
    "Shortest path algorithm": _code_dijkstra,
    "Dynamic programming — knapsack family": _code_dp_knapsack,
    "2D DP on strings": _code_dp_lcs,
    "Backtracking": _code_backtrack,
    "Greedy choice": _code_greedy,
    "Trie traversal": _code_trie,
    "Bit manipulation": _code_bit,
    "Matrix traversal / in-place transform": _code_matrix,
    "Heap / priority queue": _code_kth_element,
    "In-place reversal / rotation": _code_reverse_array,
    "Dutch national flag / counting": _code_dutch_flag,
    "Sorting algorithm": _code_merge_sort,
}


def generate_csharp(problem: str, topic: str, meta: dict) -> str:
    """Return C# code for a DSA problem."""
    text = problem.lower()

    legacy = _legacy_code(text)
    if legacy:
        return _header(problem, meta) + legacy

    for pattern, fn in _CODE_RULES:
        if re.search(pattern, text, re.I):
            return fn(problem, meta)

    pattern = meta.get("pattern", "")
    if pattern in _PATTERN_FALLBACK:
        return _PATTERN_FALLBACK[pattern](problem, meta)

    # Topic-based last resort
    topic_fn = {
        "Array": _code_hash_map,
        "Matrix": _code_matrix,
        "String": _code_sliding_window,
        "Searching & Sorting": _code_binary_search,
        "LinkedList": _code_linked_list_node,
        "Binary Trees": _code_tree_node,
        "Binary Search Trees": _code_tree_node,
        "Greedy": _code_greedy,
        "BackTracking": _code_backtrack,
        "Stacks & Queues": _code_stack,
        "Heap": _code_kth_element,
        "Graph": _code_bfs_graph,
        "Trie": _code_trie,
        "Dynamic Programming": _code_dp_knapsack,
        "Bit Manipulation": _code_bit,
    }.get(topic, _code_hash_map)

    return topic_fn(problem, meta)
