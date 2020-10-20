def swap_case(s):
    for i in s:
        if i.islower()==True:
            i=i.upper();
        elif i.isupper()==True:
            i=i.lower();
    return s

if __name__ == 'main':
    s = input()
    result = swap_case(s)
    print(result)
