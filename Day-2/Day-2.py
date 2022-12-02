fileinput = open('input', 'r')


def GetPoints1(f, s):
    newsum = 0
    if s == 'X':
        s = 'A'
        newsum = 1
    if s == 'Y':
        s = 'B'
        newsum = 2
    if s == 'Z':
        s = 'C'
        newsum = 3
    if f == s:
        return 3 + newsum
    if (f == "A" and s == "B") or (f == "B" and s == "C") or (f == "C" and s == "A"):
        return 6 + newsum
    return 0 + newsum

def GetPoints2(f, s):
    sum = 0
    if s == 'Y':
        if f == 'A':
            sum = 3+1
            return sum
        if f == 'B':
            sum = 3 + 2
            return sum
        if f == 'C':
            sum = 3 + 3
            return sum
    if s == 'X':
        if f == 'A':
            sum = 0 + 3
            return sum
        if f == 'B':
            sum = 0 + 1
            return sum
        if f == 'C':
            sum = 0 + 2
            return sum
    if s == 'Z':
        if f == 'A':
            sum = 6 + 2
            return sum
        if f == 'B':
            sum = 6 + 3
            return sum
        if f == 'C':
            sum = 6 + 1
            return sum
    return 0


commonsum1 = 0
commonsum2 = 0
for i in fileinput.readlines():
    first = i[0]
    second = i[2]
    commonsum1 += GetPoints1(first, second)
    commonsum2 += GetPoints2(first, second)

print("Answer for first part is ", commonsum1)
print("Answer for second part is ", commonsum2)