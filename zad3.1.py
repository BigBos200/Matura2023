f = open("Dane_2305/pi.txt")


lines = f.readlines()
s = len(lines)
licz = 0
T = []
INT = []


def appT(licz, T, s, lines):
    for i in range(s):
        st = lines[licz].strip()

        if licz < s - 1:
            T.append(st + (lines[licz + 1].strip()))
            licz += 1

    print(T)
    return T

def appINT(INT, T):
    for l in T:
        INT.append(int(l))

    print(INT)
    return T

IL = []
def over90(INT, IL):
    for p in INT:
        if p > 90:
              IL.append(p)
    return IL


appT(licz, T, s, lines)
appINT(INT, T)
over90(INT, IL)

print(len(IL))
