# Python all()

def check_all(check):
    return all(check)

check_list=[(True,True,True),(True,False,True),
            (),(1,0,3),(1,2,False),(1,2,True)]

check_all_rest =[check_all(check) for check in check_list]
print(check_all_rest)



