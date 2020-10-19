money = int(input())


def result(animal, price):
    afford = money // price
    if animal != "sheep":
        if afford > 1:
            print(afford, animal + "s")
        else:
            print(afford, animal)
    else:
        print(afford, animal)


if money >= 6769:
    result("sheep", 6769)
elif money >= 3848:
    result("cow", 3848)
elif money >= 1296:
    result("pig", 1296)
elif money >= 678:
    result("goat", 678)
elif money >= 23:
    result("chicken", 23)
else:
    print("None")

# define some functions to follow NTTSTT
# avoid stupid mistakes
# i deleted the use of global variables cause it interfered with functional decomposition
# and JetBrains gave me a low code quality
# note use of functions
# generally don't get outer scope error
# spending a lot of time on this problem really helped me think as a coder better,
# see my mistakes, and get better at thinking with functional decomposition
# also good practice with if, elif, and else statements
