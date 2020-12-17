
print(f'Enter a number and I will let you know if it is an even or odd number')
a = int(input())
print(a)
while a != 0:
    if a % 2 == 0:
        print(f'The number {a} is an even number')
    else:
        print(f'The number {a} is an odd number')
    print(f'please re-enter a new nonzero number or enter 0 if you want to stop')
    a = int(input())
print(f'goodbye since you already entered {0} to stop the program')
