
class ListNode():
    next = None
    def __init__(self,v):
        self.val = v

def sum(nums,target):
    h={}
    for i in range(0,len(nums)):
        try:
            return [h[str(nums[i])],i]
        except KeyError:
            ops = target - nums[i]
            h[str(ops)] = i

def addTwoNumbers(l1, l2):
        root = ListNode(0)
        s = root
        carrier = 0
        n1=l1
        n2=l2
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
            carrier = val//10
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
    max_l= 0
    max_substring = [0,0]
    for cnt in range(0,2*dim):
        i = cnt //2
        shift = cnt %2
        res = is_expanding(i,s,shift)
        # if (dim - i) < max_l:
        #     break
        if (res[1] - res[0]) >= max_l:
            max_substring = res
            max_l = (res[1] - res[0])
    return s[max_substring[0]:max_substring[1]]


def is_expanding(i,s,central_shift):
    dim = len(s)
    if i == 0:
        return [0,0]
    l = min(i-central_shift + 1,dim - i)
    res = [i,i]
    for index in range(0,l):
        if s[i-index - central_shift] != s[i + index]:
            return res
        res = [i-index-central_shift , i +index]
    return [i - l + 1 - central_shift, i + l]


def zigzag(s,row):
    if s == "" or row == 1:
        return s
    S = fill_space(s,row)
    res = ""
    step = (2*row-2)
    line_num = len(S)//step
    for i in range(0,line_num):
        res += S[i * step]

    for i in range(1,row-1):
        for j in range(0, line_num):
            base = j * step
            res += S[base + i]
            res += S[base + step - i]
    for i in range(0, line_num):
        res += S[i * step + row -1]
    return res.replace("_","")



def fill_space(s,row):
    dim = len(s)
    remainder= dim % (2*row - 2)
    fill_num = (2*row-2) - remainder
    return s + fill_num*"_"
if __name__ == "__main__":
    print("output: " + zigzag("PAYPALISHIRING",3))
    print("expect: PAHNAPLSIIGYIR")


