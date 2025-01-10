def hs(n,l,k):
    dic={1:'A',2:'B',3:'C'}
    dics={'A':1,'B':2,'C':3}
    if n==1:
        return l+'->'+k
    else:
        return hs(n-1,l,dic[6-dics[l]-dics[k]]) + '\n' + l+'->'+k + '\n' + hs(n-1,dic[6-dics[l]-dics[k]],k)
n=int(input())
print(2**n-1)
print(hs(n,'A','C'))