def parent(right_n, left_n):
    left_str="("
    right_str=")"
    result=[]
    def combination(right_count, left_count, com_str):
        print(left_count, right_count, com_str)
        if right_count > 0 and left_count > 0:
            com_str = com_str + left_str
            left_count -=1
            combination(right_count, left_count, com_str)
            com_str = com_str[:-1]
            com_str = com_str + right_str
            right_count -=1
            combination(right_count, left_count+1, com_str)
        
        elif right_count > 0:
            com_str = com_str + right_str
            right_count -=1
            combination(right_count, left_count, com_str)

        elif left_count > 0:
            com_str = com_str + left_str
            left_count -=1
            combination(right_count, left_count, com_str)
        else:
            if len(com_str) ==(right_n +left_n):
                temp = com_str
                while(True):
                    t = temp
                    t = t.replace("()","")
                    if len(t)==0:
                        result.append(com_str)
                        return
                    if len(t) == len(temp):
                        return 
                    
                    temp = t
    combination(right_n, left_n, '')

    return result
print(parent(3,3))