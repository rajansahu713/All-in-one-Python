# Python any

def check_any(check):
    return any(check)

check_any_list=[(True,True,True),(True,False,True),
                (),(1,0,3),(1,2,False),(1,2,True)]
result_any_fuctions=[check_any(check) for check in check_any_list]

print(result_any_fuctions)

