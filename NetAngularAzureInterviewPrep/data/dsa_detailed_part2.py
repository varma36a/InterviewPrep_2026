"""Detailed explanations and C# solutions for DSA section (items 26–50)."""

DSA_DETAILED_PART2: dict[str, dict] = {
    "dsa-same-tree": {
        "explanation": (
            "**Problem:** Are two binary trees structurally identical with same values?\n\n"
            "**Approach:** Recurse: both null → true; one null or val mismatch → false; else same(left) && same(right).\n\n"
            "**Complexity:** O(n) time."
        ),
        "code": """public bool IsSameTree(TreeNode? p, TreeNode? q)
{
    if (p == null && q == null) return true;
    if (p == null || q == null || p.val != q.val) return false;
    return IsSameTree(p.left, q.left) && IsSameTree(p.right, q.right);
}""",
        "key_points": ["Null checks first", "Compare values", "Short-circuit on false"],
    },
    "dsa-lca-bst": {
        "explanation": (
            "**Problem:** Lowest common ancestor of two nodes in a BST.\n\n"
            "**Approach:** Walk from root. If both < root, go left; both > root, go right; else root is LCA.\n\n"
            "**Complexity:** O(h) time, O(1) space."
        ),
        "code": """public TreeNode? LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q)
{
    while (root != null)
    {
        if (p.val < root.val && q.val < root.val) root = root.left!;
        else if (p.val > root.val && q.val > root.val) root = root.right!;
        else return root;
    }
    return null;
}""",
        "key_points": ["Use BST ordering", "First split point is LCA", "Iterative O(h)"],
    },
    "dsa-validate-bst": {
        "explanation": (
            "**Problem:** Validate entire tree is a valid BST (strict left < node < right).\n\n"
            "**Approach:** DFS with min/max bounds per node. `long` for bounds to handle int.MinValue edge.\n\n"
            "**Complexity:** O(n) time."
        ),
        "code": """public bool IsValidBST(TreeNode? root) => Validate(root, long.MinValue, long.MaxValue);

bool Validate(TreeNode? node, long min, long max)
{
    if (node == null) return true;
    if (node.val <= min || node.val >= max) return false;
    return Validate(node.left, min, node.val)
        && Validate(node.right, node.val, max);
}""",
        "key_points": ["Bounds not just parent compare", "Use long for int edges", "In-order sorted check alternative"],
    },
    "dsa-level-order": {
        "explanation": (
            "**Problem:** Return level-order traversal (BFS) as list of levels.\n\n"
            "**Approach:** Queue; each iteration process entire level size, enqueue children.\n\n"
            "**Complexity:** O(n) time, O(n) queue space."
        ),
        "code": """public IList<IList<int>> LevelOrder(TreeNode? root)
{
    var result = new List<IList<int>>();
    if (root == null) return result;
    var q = new Queue<TreeNode>();
    q.Enqueue(root);
    while (q.Count > 0)
    {
        int size = q.Count;
        var level = new List<int>();
        for (int i = 0; i < size; i++)
        {
            var node = q.Dequeue();
            level.Add(node.val);
            if (node.left != null) q.Enqueue(node.left);
            if (node.right != null) q.Enqueue(node.right);
        }
        result.Add(level);
    }
    return result;
}""",
        "key_points": ["Queue BFS", "Fix level size before inner loop", "Zigzag = reverse alternate levels"],
    },
    "dsa-number-of-islands": {
        "explanation": (
            "**Problem:** Count connected '1' land cells in 2D grid (4-directional).\n\n"
            "**Approach:** For each unvisited '1', DFS/BFS flood-fill and mark visited ('0' or set).\n\n"
            "**Complexity:** O(rows × cols) time."
        ),
        "code": """public int NumIslands(char[][] grid)
{
    int count = 0;
    for (int r = 0; r < grid.Length; r++)
        for (int c = 0; c < grid[0].Length; c++)
            if (grid[r][c] == '1')
            {
                count++;
                Dfs(grid, r, c);
            }
    return count;
}

void Dfs(char[][] grid, int r, int c)
{
    if (r < 0 || c < 0 || r >= grid.Length || c >= grid[0].Length || grid[r][c] != '1')
        return;
    grid[r][c] = '0';
    Dfs(grid, r + 1, c); Dfs(grid, r - 1, c);
    Dfs(grid, r, c + 1); Dfs(grid, r, c - 1);
}""",
        "key_points": ["Flood fill DFS/BFS", "Mark visited in-place", "4-directional connectivity"],
    },
    "dsa-clone-graph": {
        "explanation": (
            "**Problem:** Deep copy undirected graph (each node has val and neighbors list).\n\n"
            "**Approach:** BFS/DFS with `Dictionary<Node, Node>` old→clone. Clone neighbors lazily.\n\n"
            "**Complexity:** O(V + E) time."
        ),
        "code": """public class GraphNode { public int val; public IList<GraphNode> neighbors = new List<GraphNode>(); }

public GraphNode? CloneGraph(GraphNode? node)
{
    if (node == null) return null;
    var map = new Dictionary<GraphNode, GraphNode>();
    var q = new Queue<GraphNode>();
    q.Enqueue(node);
    map[node] = new GraphNode(node.val);

    while (q.Count > 0)
    {
        var cur = q.Dequeue();
        foreach (var nei in cur.neighbors)
        {
            if (!map.ContainsKey(nei))
            {
                map[nei] = new GraphNode(nei.val);
                q.Enqueue(nei);
            }
            map[cur].neighbors.Add(map[nei]);
        }
    }
    return map[node];
}""",
        "key_points": ["Hash map old→new", "BFS avoids stack overflow", "Create clone before enqueue"],
    },
    "dsa-course-schedule": {
        "explanation": (
            "**Problem:** Can you finish all courses? `prerequisites[i] = [a,b]` means b before a.\n\n"
            "**Approach:** Build graph + indegree. Kahn's BFS topological sort — if processed count == numCourses, no cycle.\n\n"
            "**Complexity:** O(V + E) time."
        ),
        "code": """public bool CanFinish(int numCourses, int[][] prerequisites)
{
    var adj = new List<int>[numCourses];
    var indegree = new int[numCourses];
    for (int i = 0; i < numCourses; i++) adj[i] = new List<int>();

    foreach (var p in prerequisites)
    {
        adj[p[1]].Add(p[0]);
        indegree[p[0]]++;
    }

    var q = new Queue<int>();
    for (int i = 0; i < numCourses; i++)
        if (indegree[i] == 0) q.Enqueue(i);

    int done = 0;
    while (q.Count > 0)
    {
        int c = q.Dequeue();
        done++;
        foreach (int next in adj[c])
            if (--indegree[next] == 0) q.Enqueue(next);
    }
    return done == numCourses;
}""",
        "key_points": ["Topological sort", "Indegree + Kahn BFS", "Cycle if done < numCourses"],
    },
    "dsa-rotting-oranges": {
        "explanation": (
            "**Problem:** Each minute adjacent fresh oranges rot. Minutes until none fresh, or -1.\n\n"
            "**Approach:** Multi-source BFS — enqueue all rotten at t=0. Process level by level.\n\n"
            "**Complexity:** O(rows × cols) time."
        ),
        "code": """public int OrangesRotting(int[][] grid)
{
    int rows = grid.Length, cols = grid[0].Length, fresh = 0, minutes = 0;
    var q = new Queue<(int r, int c)>();
    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            if (grid[r][c] == 2) q.Enqueue((r, c));
            else if (grid[r][c] == 1) fresh++;

    int[][] dirs = { new[]{1,0}, new[]{-1,0}, new[]{0,1}, new[]{0,-1} };
    while (q.Count > 0 && fresh > 0)
    {
        minutes++;
        int size = q.Count;
        for (int i = 0; i < size; i++)
        {
            var (r, c) = q.Dequeue();
            foreach (var d in dirs)
            {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nc >= 0 && nr < rows && nc < cols && grid[nr][nc] == 1)
                {
                    grid[nr][nc] = 2;
                    fresh--;
                    q.Enqueue((nr, nc));
                }
            }
        }
    }
    return fresh == 0 ? minutes : -1;
}""",
        "key_points": ["Multi-source BFS", "Level = minutes", "Track fresh count"],
    },
    "dsa-word-ladder": {
        "explanation": (
            "**Problem:** Shortest transformation from beginWord to endWord changing one letter at a time; "
            "each step must be in wordList.\n\n"
            "**Approach:** BFS from beginWord. For each word try 26 letters at each position. "
            "Use HashSet for O(1) lookup.\n\n"
            "**Complexity:** O(M² × N) where M = word length, N = word list size."
        ),
        "code": """public int LadderLength(string beginWord, string endWord, IList<string> wordList)
{
    var set = wordList.ToHashSet();
    if (!set.Contains(endWord)) return 0;

    var q = new Queue<(string word, int steps)>();
    q.Enqueue((beginWord, 1));
    set.Remove(beginWord);

    while (q.Count > 0)
    {
        var (word, steps) = q.Dequeue();
        if (word == endWord) return steps;
        char[] arr = word.ToCharArray();
        for (int i = 0; i < arr.Length; i++)
        {
            char orig = arr[i];
            for (char c = 'a'; c <= 'z'; c++)
            {
                arr[i] = c;
                string next = new string(arr);
                if (set.Remove(next))
                    q.Enqueue((next, steps + 1));
            }
            arr[i] = orig;
        }
    }
    return 0;
}""",
        "key_points": ["BFS shortest path", "Remove from set when visited", "Wildcard bucket optimization for scale"],
    },
    "dsa-kth-largest": {
        "explanation": (
            "**Problem:** Find kth largest element (not kth distinct).\n\n"
            "**Approach:** Min-heap of size k — root is kth largest. Or quickselect O(n) average.\n\n"
            "**Complexity:** O(n log k) heap; O(n) average quickselect."
        ),
        "code": """public int FindKthLargest(int[] nums, int k)
{
    var heap = new PriorityQueue<int, int>(); // min-heap by value
    foreach (int n in nums)
    {
        heap.Enqueue(n, n);
        if (heap.Count > k) heap.Dequeue();
    }
    return heap.Peek();
}""",
        "key_points": ["Min-heap size k", "kth largest not kth smallest", "Quickselect follow-up"],
    },
    "dsa-top-k-frequent": {
        "explanation": (
            "**Problem:** Return k most frequent elements.\n\n"
            "**Approach:** Count frequencies, min-heap of size k on frequency, or bucket sort by freq index.\n\n"
            "**Complexity:** O(n log k) with heap."
        ),
        "code": """public int[] TopKFrequent(int[] nums, int k)
{
    var freq = new Dictionary<int, int>();
    foreach (int n in nums) freq[n] = freq.GetValueOrDefault(n) + 1;

    var heap = new PriorityQueue<int, int>(); // min-heap by frequency
    foreach (var (num, count) in freq)
    {
        heap.Enqueue(num, count);
        if (heap.Count > k) heap.Dequeue();
    }
    return heap.UnorderedItems.Select(x => x.Element).ToArray();
}""",
        "key_points": ["Frequency map first", "Min-heap on freq", "Bucket sort O(n) alternative"],
    },
    "dsa-find-median-stream": {
        "explanation": (
            "**Problem:** Add numbers and return median at any time.\n\n"
            "**Approach:** Two heaps — max-heap for lower half, min-heap for upper half. "
            "Balance sizes so maxLower ≥ minUpper and size diff ≤ 1.\n\n"
            "**Complexity:** O(log n) add, O(1) median."
        ),
        "code": """public class MedianFinder
{
    private readonly PriorityQueue<int, int> _low = new();  // max-heap (negate)
    private readonly PriorityQueue<int, int> _high = new(); // min-heap

    public void AddNum(int num)
    {
        _low.Enqueue(num, -num);
        _high.Enqueue(_low.Dequeue(), _low.Peek());
        if (_low.Count < _high.Count)
            _low.Enqueue(_high.Dequeue(), -_high.Peek());
    }

    public double FindMedian() =>
        _low.Count > _high.Count ? _low.Peek() : (_low.Peek() + _high.Peek()) / 2.0;
}""",
        "key_points": ["Two heaps balance", "Max-left min-right", "Negate for max-heap in .NET"],
    },
    "dsa-binary-search": {
        "explanation": (
            "**Problem:** Find target index in sorted array, or -1.\n\n"
            "**Approach:** Classic binary search with inclusive bounds `left=0, right=n-1`, `mid = left + (right-left)/2`.\n\n"
            "**Complexity:** O(log n) time, O(1) space."
        ),
        "code": """public int Search(int[] nums, int target)
{
    int left = 0, right = nums.Length - 1;
    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) return mid;
        if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}""",
        "key_points": ["left <= right loop", "Avoid overflow mid formula", "Template for many variants"],
    },
    "dsa-search-rotated": {
        "explanation": (
            "**Problem:** Search target in rotated sorted array (no duplicates).\n\n"
            "**Approach:** Binary search — one half is always sorted. Check if target in sorted half; adjust bounds.\n\n"
            "**Complexity:** O(log n) time."
        ),
        "code": """public int Search(int[] nums, int target)
{
    int l = 0, r = nums.Length - 1;
    while (l <= r)
    {
        int mid = l + (r - l) / 2;
        if (nums[mid] == target) return mid;
        if (nums[l] <= nums[mid]) // left half sorted
        {
            if (nums[l] <= target && target < nums[mid]) r = mid - 1;
            else l = mid + 1;
        }
        else // right half sorted
        {
            if (nums[mid] < target && target <= nums[r]) l = mid + 1;
            else r = mid - 1;
        }
    }
    return -1;
}""",
        "key_points": ["Identify sorted half", "Target in sorted range?", "No duplicates assumed"],
    },
    "dsa-min-rotated": {
        "explanation": (
            "**Problem:** Find minimum element in rotated sorted array.\n\n"
            "**Approach:** Binary search comparing `mid` with `right`. If `nums[mid] > nums[r]`, min in right half; else in left including mid.\n\n"
            "**Complexity:** O(log n) time."
        ),
        "code": """public int FindMin(int[] nums)
{
    int l = 0, r = nums.Length - 1;
    while (l < r)
    {
        int mid = l + (r - l) / 2;
        if (nums[mid] > nums[r]) l = mid + 1;
        else r = mid;
    }
    return nums[l];
}""",
        "key_points": ["Compare mid vs right", "l < r not l <= r", "Pivot = smallest index"],
    },
    "dsa-koko-bananas": {
        "explanation": (
            "**Problem:** Koko eats bananas from piles; each hour one pile (or part). Find minimum eating speed k to finish in h hours.\n\n"
            "**Approach:** Binary search on speed [1, max(piles)]. Feasibility: sum of ceil(pile/k) ≤ h.\n\n"
            "**Complexity:** O(n log max(piles)) time."
        ),
        "code": """public int MinEatingSpeed(int[] piles, int h)
{
    int lo = 1, hi = piles.Max(), best = hi;
    while (lo <= hi)
    {
        int mid = lo + (hi - lo) / 2;
        long hours = piles.Sum(p => (p + mid - 1) / mid); // ceil division
        if (hours <= h) { best = mid; hi = mid - 1; }
        else lo = mid + 1;
    }
    return best;
}""",
        "key_points": ["Binary search on answer", "Feasibility check", "Ceil division trick"],
    },
    "dsa-climbing-stairs": {
        "explanation": (
            "**Problem:** n stairs; climb 1 or 2 steps. How many distinct ways?\n\n"
            "**Approach:** dp[i] = dp[i-1] + dp[i-2] (Fibonacci). Rolling two variables.\n\n"
            "**Complexity:** O(n) time, O(1) space."
        ),
        "code": """public int ClimbStairs(int n)
{
    if (n <= 2) return n;
    int a = 1, b = 2;
    for (int i = 3; i <= n; i++)
        (a, b) = (b, a + b);
    return b;
}""",
        "key_points": ["Fibonacci DP", "Ways = prev1 + prev2", "O(1) rolling space"],
    },
    "dsa-house-robber": {
        "explanation": (
            "**Problem:** Max money robbing linear street; can't rob adjacent houses.\n\n"
            "**Approach:** dp[i] = max(dp[i-1], dp[i-2] + nums[i]). Track rob/skip with two vars.\n\n"
            "**Complexity:** O(n) time, O(1) space."
        ),
        "code": """public int Rob(int[] nums)
{
    int skip = 0, take = 0;
    foreach (int n in nums)
        (skip, take) = (Math.Max(skip, take), skip + n);
    return Math.Max(skip, take);
}""",
        "key_points": ["Take vs skip DP", "Cannot rob adjacent", "House Robber II = circular variant"],
    },
    "dsa-coin-change": {
        "explanation": (
            "**Problem:** Minimum coins to make amount (unlimited each coin), or -1.\n\n"
            "**Approach:** dp[0..amount], dp[0]=0, dp[a]=min(dp[a-c]+1) for each coin c.\n\n"
            "**Complexity:** O(amount × coins) time."
        ),
        "code": """public int CoinChange(int[] coins, int amount)
{
    var dp = new int[amount + 1];
    Array.Fill(dp, amount + 1);
    dp[0] = 0;
    for (int a = 1; a <= amount; a++)
        foreach (int c in coins)
            if (c <= a) dp[a] = Math.Min(dp[a], dp[a - c] + 1);
    return dp[amount] > amount ? -1 : dp[amount];
}""",
        "key_points": ["Unbounded knapsack", "Initialize with infinity", "Bottom-up 1D DP"],
    },
    "dsa-lis": {
        "explanation": (
            "**Problem:** Length of longest strictly increasing subsequence.\n\n"
            "**Approach:** Patience sorting — `tails[i]` = smallest tail of LIS length i+1. "
            "Binary search position for each num.\n\n"
            "**Complexity:** O(n log n) time."
        ),
        "code": """public int LengthOfLIS(int[] nums)
{
    var tails = new List<int>();
    foreach (int n in nums)
    {
        int lo = 0, hi = tails.Count;
        while (lo < hi)
        {
            int mid = lo + (hi - lo) / 2;
            if (tails[mid] < n) lo = mid + 1;
            else hi = mid;
        }
        if (lo == tails.Count) tails.Add(n);
        else tails[lo] = n;
    }
    return tails.Count;
}""",
        "key_points": ["Patience sorting O(n log n)", "tails array + binary search", "DP O(n²) easier to explain"],
    },
    "dsa-lcs": {
        "explanation": (
            "**Problem:** Length of longest common subsequence of two strings.\n\n"
            "**Approach:** 2D DP: if s1[i]==s2[j], dp[i,j]=dp[i-1,j-1]+1; else max of neighbors.\n\n"
            "**Complexity:** O(m × n) time and space."
        ),
        "code": """public int LongestCommonSubsequence(string text1, string text2)
{
    int m = text1.Length, n = text2.Length;
    var dp = new int[m + 1, n + 1];
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++)
            dp[i, j] = text1[i - 1] == text2[j - 1]
                ? dp[i - 1, j - 1] + 1
                : Math.Max(dp[i - 1, j], dp[i, j - 1]);
    return dp[m, n];
}""",
        "key_points": ["2D DP table", "Match → diagonal + 1", "Space optimize to 1D row"],
    },
    "dsa-word-break": {
        "explanation": (
            "**Problem:** Can string be segmented into dictionary words?\n\n"
            "**Approach:** dp[i] = true if prefix s[0..i) breakable. Try all word lengths ending at i.\n\n"
            "**Complexity:** O(n² × wordLen) with hash set lookup."
        ),
        "code": """public bool WordBreak(string s, IList<string> wordDict)
{
    var set = wordDict.ToHashSet();
    var dp = new bool[s.Length + 1];
    dp[0] = true;
    for (int i = 1; i <= s.Length; i++)
        for (int j = 0; j < i; j++)
            if (dp[j] && set.Contains(s.Substring(j, i - j)))
            {
                dp[i] = true;
                break;
            }
    return dp[s.Length];
}""",
        "key_points": ["dp[i] prefix breakable", "Try all split points j", "HashSet for O(1) word lookup"],
    },
    "dsa-subsets": {
        "explanation": (
            "**Problem:** Return all subsets (power set) of distinct integers.\n\n"
            "**Approach:** Backtrack — at each index include or exclude. Or iterative: double result by adding element.\n\n"
            "**Complexity:** O(n × 2^n) output size."
        ),
        "code": """public IList<IList<int>> Subsets(int[] nums)
{
    var result = new List<IList<int>>();
    void Dfs(int i, List<int> path)
    {
        if (i == nums.Length) { result.Add(new List<int>(path)); return; }
        path.Add(nums[i]);
        Dfs(i + 1, path);
        path.RemoveAt(path.Count - 1);
        Dfs(i + 1, path);
    }
    Dfs(0, new List<int>());
    return result;
}""",
        "key_points": ["Include/exclude backtrack", "Copy path at leaf", "2^n subsets"],
    },
    "dsa-combination-sum": {
        "explanation": (
            "**Problem:** All unique combinations where candidates sum to target; each candidate reusable.\n\n"
            "**Approach:** Backtrack from index, add candidate, recurse same index if reuse allowed. Prune when sum > target.\n\n"
            "**Complexity:** Exponential in target/min(candidates)."
        ),
        "code": """public IList<IList<int>> CombinationSum(int[] candidates, int target)
{
    Array.Sort(candidates);
    var result = new List<IList<int>>();
    void Dfs(int start, int remain, List<int> path)
    {
        if (remain == 0) { result.Add(new List<int>(path)); return; }
        for (int i = start; i < candidates.Length; i++)
        {
            if (candidates[i] > remain) break;
            path.Add(candidates[i]);
            Dfs(i, remain - candidates[i], path); // i not i+1 — reuse
            path.RemoveAt(path.Count - 1);
        }
    }
    Dfs(0, target, new List<int>());
    return result;
}""",
        "key_points": ["Reuse → recurse same index", "Sort + prune", "Copy path at target hit"],
    },
    "dsa-permutations": {
        "explanation": (
            "**Problem:** Return all permutations of distinct integers.\n\n"
            "**Approach:** Backtrack with `used[]` array. At each step pick unused element.\n\n"
            "**Complexity:** O(n × n!) time."
        ),
        "code": """public IList<IList<int>> Permute(int[] nums)
{
    var result = new List<IList<int>>();
    var used = new bool[nums.Length];
    var path = new List<int>();

    void Dfs()
    {
        if (path.Count == nums.Length) { result.Add(new List<int>(path)); return; }
        for (int i = 0; i < nums.Length; i++)
        {
            if (used[i]) continue;
            used[i] = true;
            path.Add(nums[i]);
            Dfs();
            path.RemoveAt(path.Count - 1);
            used[i] = false;
        }
    }
    Dfs();
    return result;
}""",
        "key_points": ["used[] tracking", "n! permutations", "Swap-based alternative in-place"],
    },
}
