def IntInput(x,y):
    while True:
        try:
            print(y, end="")
            x= int(input())
        except ValueError:
            continue
        if x >= 0:
            return x
            break
        else:
            continue
value = IntInput(int, "Please enter a positive integer:")


print(value)
