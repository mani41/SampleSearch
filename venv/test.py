import math

n = int(input())  # Reading input from STDIN
# print(n)         # Writing output to STDOUT

a = [x for x in range(1, n + 1)]

print(a)
# for i in a:
#    print(i,end=" ")

for i in range(2, int(math.sqrt(n)) + 1):
    j = 2;
    while (j * i < n + 1):
        a[j * i-1] = 0
        j = j + 1
print(a)
for i in range(1, n):
    if (a[i] != 0):
        print(a[i], end=" ")

