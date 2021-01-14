'SOSI' 


a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))
list = [a, b, c]
summ = 0
for i in list:
    if (i % 5) == 0:
        summ = summ + i
if summ == 0:
    print("ERROR")
else:
    print(summ)