def func():
    print("this function1")


func()


# print character by n value
def disp(char, n):
    for i in range(n):
        print(char)


disp("#", 5)


# default argument


def disp(char="$", n=30):
    for i in range(n):
        print(char)


disp("#", 5)
disp("#")
disp()
