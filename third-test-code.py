#printing *

print("*")

#printing * in column wise

for i in range(5):
    print("*")

#printing * in row wise

for i in range(5):
    print("*", end=" ")

#printing right angled triangle using *

for i in range(1, 6):
    for j in  range(i):
        print("*", end=" ")
    print()

#printing square using *

for i in range(5):
    for i in range(5):
        print("*", end=" ")
    print()

#printing right angled triangle(right angled) using *

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")

    for k in range(i):
        print("*", end=" ")
    print()

#printing pyramid using *

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")

    for k in range(2*i - 1):
        print("*", end=" ")
    print()

    #printing reverse pyramid using *

n = 5
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")

    for k in range(2*i - 1):
        print("*", end=" ")
    print()

#printing diomond using *

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")

    for k in range(2*i - 1):
        print("*", end=" ")
    print()

for i in range(n - 1, 0, -1):
        for j in range(n - i):
            print(" ", end=" ")

        for k in range(2*i - 1):
            print("*", end=" ")
        print()