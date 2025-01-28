#
# python errors classified into two category
# 1. syntax error (e.g. colon, indentation, etc.)
# 2. logical error (Exceptions)
#

print(5 / 0)  # ZeroDivisionError: division by zero

list_one = [1, 3, 4, 5]
print(list_one[5])  # IndexError: list index out of range

#
#
#

try:
    x = int(input("Please enter a number: "))

except ValueError:
    print("Oops!  That was no valid number.  Try again...")


#
#
#
#

try:
    f = open("myfile.txt")
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise


#
#
#


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
