a = int(input('0<a<1000 a= '))
i=a%10
b=a//10%10
u=a//100
r=0
if i==1:
    r='I'
if i==2:
    r='II'
if i==3:
    r='III'
if i==4:
    r='IV'
if i==5:
    r='V'
if i==6:
    r='VI'
if i==7:
    r='VII'
if i==8:
    r='VIII'
if i==9:
    r='IX'
ir=0
if b==1:
    ir='X'
if b==2:
    ir='XX'
if b==3:
    ir='XXX'
if b==4:
    ir='XL'
if b==5:
    ir='L'
if b==6:
    ir='LX'
if b==7:
    ir='LXX'
if b==8:
    ir='LXXX'
if b==9:
    ir='XC'
ur=0
if u==1:
    ur='C'
if u==2:
    ur='CC'
if u==3:
    ir='CCC'
if u==4:
    ur='CD'
if u==5:
    ur='D'
if u==6:
    ur='DC'
if u==7:
    ur='DCC'
if u==8:
    ur='DCCC'
if u==9:
    ur='CM'
print(ur+ir+r)