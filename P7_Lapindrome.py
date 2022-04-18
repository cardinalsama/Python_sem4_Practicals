# Input test cases
print("Input: ")
n = int(input("Enter test case no: "))

sList = list()

for i in range(n):
    sList.append(input())

for i in range(n):
    str = sList[i]
    s1, s2 = '', ''

    if len(str) % 2 == 0:
        s1 = str[: len(str) // 2]
        s2 = str[len(str) // 2 :]
    else:
        s1 = str[: len(str) // 2]
        s2 = str[len(str) // 2 + 1 :]

    list1 = list(s1)
    list2 = list(s2)

    list1.sort()
    list2.sort()

    print()
    print("Output: ")

    if str(list1) == str(list2):
        print("YES")
    else:
        print("NO")
