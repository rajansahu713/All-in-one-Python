# ans =[]

# def combination(nums, target, i, cursum, temp):
#     if i < len(nums):
#         if cursum > target:
#             return
        
#         # if i == len(nums):
#         #     if cursum == target:
#         #         ans.extend(temp)
#         #         return 
#         if cursum == target:
#             if temp in sorted(ans):
#                 return
#             ans.append(temp)
#             return
            
#         cursum += nums[i]
#         temp.append(nums[i])

        
#         combination(nums, target, i, cursum, temp)
#         cursum -=nums[i]
#         temp.pop(-1)
#         combination(nums, target, i+1, cursum, temp)
#     else:
#         return 



# nums =[2,2,3]
# combination(nums, 5, 0, 0, [])
# print(ans)


def combinationSum(candidates, target):
    ans = []
    helper = []
    findAns(0, target, candidates, ans, helper)
    return ans

def findAns(index, target, arr, ans, helper):
    if index == len(arr):
        if target == 0:
            ans.append(helper[:])
        return
    
    if arr[index] <= target:
        helper.append(arr[index])
        findAns(index, target - arr[index], arr, ans, helper)
        helper.pop()
    
    findAns(index + 1, target, arr, ans, helper)

arr =[2,2,3]
print(combinationSum(arr, 5))