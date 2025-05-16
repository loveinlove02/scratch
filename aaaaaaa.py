sentence = 'abbbca'

st = ''

for c in sentence:
    if c!='.' and c!=' ':
        st+=c

size = len(st)
n = size//2

for i in range(0, n, 1):
    if st[i]!=st[size-1-i]:
        result = False
        break
    else:
        result = True

print(result)

