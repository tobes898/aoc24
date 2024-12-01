file = open("real_input.txt")
output = []
left = []
right = []
for line in file:
    temp = line.strip().split()
    left.append(int(temp[0]))
    right.append(int(temp[1]))

left.sort()
right.sort()

res = 0
for i in range(len(left)):
    res += abs(left[i] - right[i])


file.close()

tracker = {}

for i in range(len(right)):
    if right[i] not in tracker:
        tracker[right[i]] = 0
    tracker[right[i]] += 1

res2 = 0
for i in range(len(left)):
    if left[i] not in tracker:
        continue
    res2 += left[i] * tracker[left[i]]

print(res)
print(res2)
