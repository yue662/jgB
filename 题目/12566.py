st=str(input())
st=st.lower()
i=1
while True:
    if len(st)==0:
        break
    if i==len(st):
        print('(' + st[0] + ',' + str(i) + ')', end='')
        break
    if ord(st[i])==ord(st[0]):
        i+=1
        continue
    else:
        print('('+st[0]+','+str(i)+')',end='')
        st=st[i:]
        i=1
        continue