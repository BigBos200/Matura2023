f = open("Dane_2305/pi.txt")

lines = f.readlines()
s = len(lines)
count = 0
dicton = {}
T = []

def addT(lines, count, s, T):
    for i in range(s):
        st = lines[count].strip()

        if count < s - 1:
            T.append(st + (lines[count + 1].strip()))
            count += 1

    return T

def ilT(T, dicton):
    for i in T:
        dicton[i] = T.count(i)

    return dicton

addT(lines, count, s, T)
ilT(T, dicton)



def test1(dicton):
    minn = (min(dicton.values()))
    maxx = (max(dicton.values()))

    key_min = next(k for k, v in dicton.items() if v == minn)
    key_max = next(k for k, v in dicton.items() if v == maxx)

    print(key_min, minn)
    print(key_max, maxx)

    return key_min, key_max, minn, maxx

test1(dicton)