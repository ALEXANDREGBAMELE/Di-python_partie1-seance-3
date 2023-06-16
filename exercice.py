# Given a list [("name", "Elie"), ("job", "Instructor")],
# create a dictionary that looks like this {'job': 'Instructor', 'name': 'Elie'} 
# (the order does not matter).

my_list = [("name", "Elie"), ("job", "Instructor")]
my_dict = dict({})
for key, value in my_list:
    my_dict[key] = value
print(my_dict)


# Given two lists ["CA", "NJ", "RI"]
# and ["California", "New Jersey", "Rhode Island"]
# return a dictionary that looks like
# this {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.
# You can research the zip method to help you.
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

my_dict2 = dict({})
my_dict2 = dict(zip(list1, list2))
print(my_dict2)
# or

print({list2[i]:list1[i] for i in range(0,3)})
