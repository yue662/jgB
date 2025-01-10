sl=list(map(str,input().split()))
d1={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen ':16,'seventeen':17,'eighteen':18,'nineteen':19}
d2={'twenty':20,'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90}
d3=['negative']
def num1(lk):
    if len(lk)==1:
        return d1[lk[0]]
    else:
        return d2[lk[0]]+d1[lk[1]]
def num2(lk):
    if 'hundred' in lk:
        return d1[lk[0]]*100+num1(lk[2:])
    else:
        return num1(lk)
def num3(lk):
    if 'thousand' in lk:
        return num2(lk[0:lk.index('thousand')])*1000+num2(lk[lk.index('thousand')+1:])
    else:
        return num2(lk)
def num4(lk):
    if 'million' in lk:
        return num2(lk[0:lk.index('million')])*1000000+num3(lk[lk.index('million')+1:])
    else:
        return num3(lk)
if sl[0] in d3:
    su=num4(sl[1:])*(-1)
else:
    su=num4(sl)
print(su)