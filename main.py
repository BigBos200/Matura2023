f = open("Dane_2305/pi.txt")


lines = f.readlines()
s = len(lines)
licz = 0
T = []
INT = []
for i in range(s):
    st = lines[licz].strip()


    if licz < s-1:
        T.append(st+(lines[licz +1].strip()))
        licz +=1


print(T)

for l in T:
    INT.append(int(l))


print(INT)

for p in INT:
    if p > 90:
        print(p)



f.close()

