def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num=int(input("Enter a number: "))
result=even_odd(num)
print("The number", num, "is", result)