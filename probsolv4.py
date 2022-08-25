'''Given a string S and a character C (as string of length 1), return a string with the characters surrounding any occurrence of C reversed. 
For example, if S is "Hello beautiful world" and C is a space, return "Hellb oeautifuw lorld". '''

st =list('hello beautiful world')
s = " "
st1 = []
for i in range(len(st)):
  if st[i] == s:
    st1.pop(i-1)
    st[i-1],st[i+1] = st[i+1],st[i-1]
    st1.append(st[i-1])
    st1.append(s)
    st1.append(st[i+1])
    st1.pop(i+1)
  else:
    st1.append(st[i])
print(''.join(st1))


