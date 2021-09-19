import random


# _______________Task_1_______________ #
def swap_case():
    print("Введите значение S")
    s = str(input())
    if len(s) > 1000:
        print("Слишком много символов")
    else:
        print(s.swapcase())


swap_case()


# _______________Task_2_______________ #
def print_second_max():
    print("Введите значение n")
    n = int(input())
    A = []
    B = []
    if n < 2 or n > 10:
        print("Недопустимое значение n")
    else:
        for i in range(n):
            A.append(random.randint(-100, 100))
        A.sort()
        B = list(set(A))
        B.sort()
        print(B[-2])


print_second_max()


# _______________Task_3_______________ #
print("Ввудите значение N"); N = int(input())
for i in range(1, N):
    print(int(i*((10**i)-1)/9))