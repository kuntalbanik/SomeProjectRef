# Practice codes

# List comprehension
n = [m for m in range(1, 20)]
# print(n)

n.append(1000)
# print(n)


# Tuple example
# immutable data type
tu = ("localhost", 80)
# print(tu)


# Sets
se = {10, 20, 30}
# print(type(se))


# Zip function example

list_one = [10, 20, 40, 50]
list_two = [3, 40, 77, 88, 76]

for a, b in zip(list_one, list_two):
    # print(a, b)
    pass


if len(list_one) > len(list_two):
    list_length = len(list_two)
else:
    list_length = len(list_one)


print(list_length)

for item in range(list_length):
    # print(list_one[item], list_two[item])
    pass

# ##############################
# ##############################

# Json example
import json

#
# dictionary to json
# convert dictionary data to json format for API
#
d = {
    "course_name": "Python",
    "fees": 15000,
}

f = json.dumps(d)
# print(type(f))
# print(f)


#
# json to dictionary
# convert any json date received from any API
#

sample_json = '{"cname": "Python", "fees": 12000, "duration": "12th months"}'

g = json.loads(sample_json)
# print(type(g))
# print(g)
for data in g:
    # print(data, g[data])
    pass


# ############################
# ############################
#
# example of reading & writing json file
#
# json read
json_read = open("Codes/posts.json", "r")
read_data = json_read.read()
final_data = json.loads(read_data)

for j_data in final_data:
    # print(j_data)
    print(j_data["id"], j_data["title"])

# print(type(j_data))

# json write
# Data to be written
write_json = {
    "cname": "Python",
    "fees": 12000,
    "duration": "12th months",
}

json_write = open("Codes/json_write.json", "a")

write_data = json.dumps(write_json, indent=4)  # tab indentation

# write json to file
# json_write.write(write_data)
