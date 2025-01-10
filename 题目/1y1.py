n=int(input())
ins = str(input())
ords = []
outs = ''
for i in range(0, len(ins)):
    ords.append(ord(ins[i]))
    if ords[i] >= 97:
        outs+=chr((ords[i]-97+26-n)%26+97)
    else:
        outs+=chr((ords[i]-65+26-n)%26+65)
print(outs)