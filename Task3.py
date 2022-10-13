string1 = input('Введите фразу ')
string2 = input('Введите часть фразы ')
arr = string1.split()
n = 0
x = 0
while n != len(arr):
    if string2 == arr[n]:
        x += 1
    n +=1

print(x)