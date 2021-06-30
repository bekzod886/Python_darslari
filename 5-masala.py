name = str(input())
if name[-1] == 'a' or name[-1] == 'o' or name[-1] == 'u' or name[-1] == 'e' :
    print(name+'yev')
elif name[-1] == 'f':
    print(name.replace('f','p')+'ov')
else:
    print(name+'ov')
