# Practice codes

# Zip function example
list_one = [10, 20, 40, 50]
list_two = [3, 40, 77, 88, 76]

for a, b in zip(list_one, list_two):
    print(a, b)


if len(list_one) > len(list_two):
    list_length = len(list_two)
else:
    list_length = len(list_one)

print(list_length)

for item in range(list_length):
    print(list_one[item], list_two[item])

# ##############################

# Json example
import json

d = {
    "course_name": "Python",
    "fees": 15000,
}

f = json.dumps(d)

print(f)
