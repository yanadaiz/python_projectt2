def fun(left, right, s):
    dist = 1
    while left - dist >= 0 and right + dist <= (len(s) - 1):
        if s[left - dist] != s[right + dist]:
            break
        dist += 1
    return dist - 1
def l(pal1, pal2):  #max len (pal1, pal2)
    if len(pal1) >= len(pal2):
        return pal1
    return pal2

s = input("Input string: >")

if s == '':   #check correct input
    print("ERR: empty string")
    s = input("Repeat input: >")
palindrom = ''
if len(s) == 1:
    palindrom = s
else:
    for i in range(len(s)):
        pal1, pal2, pal3 = '', '', ''
        if i > 0 and i < (len(s) - 1):
            dist = fun(i, i, s)
            pal1 = s[(i - dist):(i + dist + 1):] #palindrom len 2k+1
            
            if s[i] == s[i - 1]:  #palindrom len 2k
                dist = fun(i - 1, i, s)
                pal2 = s[(i - dist):(i + 1 + dist + 1):]
                
            if s[i] == s[i + 1]:  #palindrom len 2k
                dist = fun(i, i + 1, s)
                pal3 = s[(i - dist):(i + 1 + dist + 1):]
                
        palindrom = l(palindrom, l(l(pal1, pal2), l(pal1, pal3)))

if len(palindrom) == 1:
    print("Max palindrom: <", s[0], ">", sep='')
else:
    print("Max palindrom: <", palindrom, ">", sep='')
