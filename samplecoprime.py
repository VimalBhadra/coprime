def hcf(a,b):
    if(b==0):
        return a
    else:
        return hcf(b,a%b)
x=int(input())
y=int(input())
if hcf(x,y)==1:
    print('True')
else:
    print('False')
