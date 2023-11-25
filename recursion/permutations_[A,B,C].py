def permun(nums):
    result =[]
    if len(nums) == 1:
        return [nums[:]]
    
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permun(nums)

        for perm in perms:
            perm.append(n)

        result.extend(perms)
        nums.append(n)
    return result

print(permun(['A',"B","C"]))