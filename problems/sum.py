class ListNode():
    next = None

    def __init__(self, v):
        self.val = v


def addTwoNumbers(l1, l2):
    root = ListNode(0)
    s = root
    carrier = 0
    n1 = l1
    n2 = l2
    while True:
        if n1 is None:
            v1 = 0
        else:
            v1 = n1.val
            n1 = n1.next
        if n2 is None:
            v2 = 0
        else:
            v2 = n2.val
            n2 = n2.next
        val = carrier + v1 + v2
        local = val % 10
        carrier = val // 10
        s.next = ListNode(local)
        s = s.next
    return root.next


def lengthOfLongestSubstring(s):
    start = maxLength = 0
    usedChar = {}

    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[s[i]] = i

    return maxLength


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    dim = len(s)
    max_l = 0
    max_substring = [0, 0]
    for cnt in range(0, 2 * dim):
        i = cnt // 2
        shift = cnt % 2
        res = is_expanding(i, s, shift)
        # if (dim - i) < max_l:
        #     break
        if (res[1] - res[0]) >= max_l:
            max_substring = res
            max_l = (res[1] - res[0])
    return s[max_substring[0]:max_substring[1]]


def is_expanding(i, s, central_shift):
    dim = len(s)
    if i == 0:
        return [0, 0]
    l = min(i - central_shift + 1, dim - i)
    res = [i, i]
    for index in range(0, l):
        if s[i - index - central_shift] != s[i + index]:
            return res
        res = [i - index - central_shift, i + index]
    return [i - l + 1 - central_shift, i + l]


def zigzag(s, row):
    if s == "" or row == 1:
        return s
    S = fill_space(s, row)
    res = ""
    step = (2 * row - 2)
    line_num = len(S) // step
    for i in range(0, line_num):
        res += S[i * step]

    for i in range(1, row - 1):
        for j in range(0, line_num):
            base = j * step
            res += S[base + i]
            res += S[base + step - i]
    for i in range(0, line_num):
        res += S[i * step + row - 1]
    return res.replace("_", "")


def fill_space(s, row):
    dim = len(s)
    remainder = dim % (2 * row - 2)
    fill_num = (2 * row - 2) - remainder
    return s + fill_num * "_"


def sum_3(nums):
    s, h = sorted(nums), {}
    for i in s:
        try:
            h[i] += 1
        except KeyError:
            h[i] = 1

    dim = len(nums)
    final = []
    for i, v in enumerate(s):
        if i >= dim - 1:
            break
        for j in range(max(h[v], 2)):

            res = sum(s[i + h[v]:], -v * (j + 1))
            if res is not None:
                res.append(v)
                final.append(res)
        if v == 0 and h[v] > 2:
            final.append([0, 0, 0])
    return final


def sum(nums, target):
    h = {}
    for i in range(0, len(nums)):
        try:
            return [nums[h[str(nums[i])]], nums[i]]
        except KeyError:
            ops = target - nums[i]
            h[str(ops)] = i


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    res = 0
    while x != 0:
        digital = x % 10
        res = res * 10 + digital
        x = x // 10
    return res


def trap_2d(height):
    """
    :type height: List[int]
    :rtype: int
    """
    dim = len(height)
    right_max = height[:]
    left_max = height[:]
    for i in range(1, dim):
        left_max[i] = max(left_max[i - 1], left_max[i])
    for i in reversed(range(0, dim - 1)):
        right_max[i] = max(right_max[i + 1], right_max[i])
    water = height[:]
    for i in range(1, dim - 1):
        water[i] = min(right_max[i], left_max[i])
    return water


def trap(mat):
    h = len(mat)
    if h < 3:
        return 0
    w = len(mat[0])
    if w < 3:
        return 0
    vert = []
    for i in range(h):
        vert.append(trap_2d(mat[i]))
    parel = []
    for j in range(w):
        parel.append(trap_2d([mat[i][j] for i in range(h)]))
    water = 0
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            water += min(vert[row][col], parel[col][row]) - mat[row][col]
    return water

from copy import deepcopy

def trap(mat):
    h = len(mat)
    if h < 3:
        return 0
    w = len(mat[0])
    if w < 3:
        return 0
    left = deepcopy(mat)
    right = deepcopy(mat)
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            left[i][j] = max(min(left[i - 1][j], left[i][j - 1]), left[i][j])
    for i in reversed(range(1,h-1)):
        for j in reversed(range(1,w-1)):
            right[i][j] = max(min(right[i + 1][j], right[i][j + 1]), right[i][j])
    water=0
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            water += min(left[i][j],right[i][j]) - mat[i][j]

    return water


if __name__ == "__main__":
    print(trap([[5,5,5,1],[5,1,1,5],[5,1,5,5],[5,2,5,8]]))
