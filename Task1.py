n = float(input('Введите число '))
def sum(n):                            
    if n < 0:                         
        n = n * -1
    num = 0
    for i in str(n):
        if i != '.':
            num += int(i)
    return num
print(sum(n))