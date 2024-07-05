try:
    print(10/0)
except ZeroDivisionError:
    print("Sorry")

try:
    print(10 / 0)
except TypeError:
    print("types")
except ValueError:
    print("Value")
except ZeroDivisionError:
    print("Sorry")
#     relevant except block only runs


try:
    print(10 / 0)
except TypeError:
    print("types")
except ValueError:
    print("Value")

#     there is no revelant except block so it run the empty except block but the empty except block present in last only
except :
    print("Sorry")

