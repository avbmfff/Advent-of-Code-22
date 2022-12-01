fileinput = open('input1', 'r')

max = 0
arr = []
sum = 0
for i in fileinput.readlines():
    if i and i.strip():
        sum += int(i)
    else:
        arr.append(int(sum))
        sum = 0
    if max < sum:
        max = sum

print("The answer for 1 part is", max)


arr.sort(reverse=True)
sum = 0
i = 0
while i != 3:
    sum += int(arr[i])
    i += 1

print("The answer for 2 part is", sum)