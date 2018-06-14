# class Solution:
#     def findUnsortedSubarray(self, nums):
#         self.nums = nums
#
#         sort_nums = sorted(self.nums)
#         print(sort_nums)
#
#         for l in range(len(self.nums)):
#             if not self.nums[l] == sort_nums[l]:
#                 break
#         for r in range(len(self.nums))[::-1]:
#             if not self.nums[r] == sort_nums[r]:
#                 break
#
#         print(l)
#         print(r)
#
#         unsortSubarray = self.nums[l:r+1]
#         # print(unsortSubarray)
#         leng = len(unsortSubarray)
#         print(leng)
#         return leng
#
#
#
#         # judge = True
#         #
#         # while judge:
#         #
#         #     if self.nums == []:
#         #         break
#         #
#         #     mini = min(self.nums)
#         #     maxi = max(self.nums)
#         #     judge = False
#         #
#         #     if self.nums[0] == mini:
#         #         del self.nums[0]
#         #         judge = True
#         #     if self.nums[-1] == maxi:
#         #         del self.nums[-1]
#         #         judge = True
#         #
#         # return self.nums
#
#
# # a = [2, 31, 22, 3, 14, 5, 6, 87, 27,46,100]
# a = [1]
# n = Solution()
# # n.findUnsortedSubarray(a)
# print(n.nums)
#
# # import profile
# # import pstats
# #
# # def AAA():
# #     a = [i for i in range(10)]
# #     b = 'a b t d e f g h i j k l m n'.split()
# #     print(a)
# #     print(b)
# #
# #     x = []
# #     for item in a:
# #         x.append(item*item)
# #     print(x)
# #
# # if __name__ == "__main__":
# #     profile.run("AAA()", "prof.txt")
# #     p = pstats.Stats("prof.txt")
# #     p.sort_stats("time").print_stats()
# #
# #
# #

x = {"a":1, "b":2}
def aaa(m):
    if m in x:
        return True

print(aaa('a'))
