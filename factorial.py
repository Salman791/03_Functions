# - Create a function called `factorio`
#   that returns it's input's factorial

def factorio(x):
    factorial = 1
    for i in range(1,x+1):
        factorial = factorial * i
    print(factorial)

factorio(5)