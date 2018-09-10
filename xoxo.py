def factorial2(m):
    if m == 0:
        return 1
    else:
        return m * factorial2(m-1)
m =int(input("The factorial of the num is: "  ))
print(factorial2(m))