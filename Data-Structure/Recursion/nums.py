nums = [3,4, 2]

def comibination(nums, target):
    result =[]
    def create_combination(i, cur, total):
        print(cur, i)
        if total == target:
            result.append(cur[:])

        if i >= len(nums) or total > target:
            return 
        cur.append(nums[i])
        create_combination(i, cur, total + nums[i])
        cur.pop()
        create_combination(i+1, cur, total)
    create_combination(0, [], 0)
    return result
    

target =7
print(comibination(nums, target))