print("Input : ")
n = int(input())
lst = [0] * n
input_str = input()
lst_str = input_str.split()
lst = [int(x) for x in lst_str]


max = lst[0]
second_max = 0
for i in range(0, len(lst)):
    if(lst[i] > max):
        second_max = max
        max = lst[i]
    if(lst[i] > second_max and lst[i] < max):
        second_max = lst[i]
         
print("Output : ")
print(second_max)
