class Solution:
    def reverseWords(self, s: str) -> str:
        # list1 = list(s.split(" "))
        # res = ""
        # print(list1)

        # for i in list1:
        #     test = ""
        #     for j in i[::-1]:
        #         test+=j
        #     res+=test+" "

        # print(res)
        # return res.rstrip()

        words = s.split()

        return [word[::-1] for word in words]



obj = Solution()
obj.reverseWords("Let's take LeetCode contest")
