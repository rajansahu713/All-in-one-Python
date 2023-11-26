def permutations(letter):
    result =[]

    if len(letter) ==1:
        return [letter[:]]

    for i in range(len(letter)):
        n = letter.pop(0)
        perms = permutations(letter)
        for perm in perms:
            perm.append(n)
        if len(perms[0])==3:
            perms =[perm for perm in perms if perm[2] !="B"]
        result.extend(perms)
        letter.append(n)

    return result

letter= ["A","B","C"]
print(permutations(letter))