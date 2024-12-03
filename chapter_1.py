# 1. DATA TYPES
# this is the number data type
4124234234234

# This is a string data type (a string of characters - alphanumeric)
"my nam3is james"


print('hello world')

# sub-objective (print out the string hello world)


# This is the list / array data type, contains a series or sequence of values that can be of any data type themselves
shopping_list = ['eggs', 
 'bananas', 
 'milk', 
 4, 
 []
 ]

# this is an object data type / dictionary
def jello():
    print('jello')
person = {
    # "name": "james",
    "age": 28,
    "action": jello
}

# boolean - truthy falsey
True
False

# None - absence of information
None


# A data type is a type of data that is friendly to python

# 2.0 Variables - a variable is a label for some data
number_of_eggs = 5

my_string = 'hello world'

print(number_of_eggs * 2)

# 3.0 Logic and operations
# If block - if condition is true, execute this code, otherwise skip it
if number_of_eggs > 4:
    print('you have more than 4 eggs')

print('We passed the if block')

if 'name' in person:
    print(person['name'])
else:
    print('the key name is not avaialble within the person dictionary')

if 'bananas' in shopping_list:
    print('Need to get bananas')
else:
    print('Dont need bananas')

# Logical operators - and / or

if number_of_eggs > 5 and number_of_eggs < 20:
    print('Okay, we also have less than 20 eggs so the egg range is between 5 - 20')

if number_of_eggs < 6 or number_of_eggs >= 20:
    print('Okay, the number of eggs is outside the ideal range which is 5 - 20')
   
# operators
x = 3
y = 4
print(x * y + x - y / x)

# remainder operator (%)
remainder = y % x
print(remainder == 10 % 3)

# equality == (checks if the left is equal to the right)
x == y #this would be false because x is 3 and y is 4 and therefore not equal

# not (! or not)
x != y # this would be true because x is not equal to y

if not number_of_eggs == 4:
    print(f'The number of eggs is not equal to four, but instead: {number_of_eggs}')

# loops (while / for)
count = 0
while count < number_of_eggs:
    print('hello world')
    count = count + 2
    if count == 3:
        break

for x in shopping_list:
    print(x)

for i in range(10):
    print(i)

length_of_my_array = len(shopping_list)
for j in range(length_of_my_array):
    current_index = j
    current_value = shopping_list[j]
    print(f'The current index is: {current_index} and the value at that index in the list/array is {current_value}')

def print_funny_word(funny_word):
    '''this function takes an argument and prints out the word provided as an argument, in addition to the word gilgamesh'''
    return
    print('gilgamesh & ', funny_word)


for k in range(3):
    print_funny_word('doug')

def multiply_two_numbers(input1, input2):
    return input1 * input2

product = multiply_two_numbers(8, 7)
print(product)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def jello_two(self):
        print('jello jello')

new_person = Person('doug', 28)

new_person.jello_two()
print(new_person.name)


new_new_person = Person('lucy', 42)