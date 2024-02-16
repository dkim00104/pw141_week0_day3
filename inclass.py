obj = [1,2,3]

print(obj)

len(obj)

# function
# syntax to create function are as follows:
# def [NAME](PARAMETERS):

def talk():
    print("...")
    print("yapa yapa yapa")
    print("...")
    print("done talking")

def blender(fruit1, fruit2):
    print("...blending...")
    smoothie = "You made a " + fruit1 + " and " + fruit2 + " smoothie!"
    return smoothie

s1 = blender("strawberry", "banana")
s2 = blender("kiwi", "mango")
s3 = blender("blueberry", "raspberry")

print(s1)
print(s2)
print(s3)

print(blender("passionfruit", "watermelon"))

for num in range(11):
    print(num)


def print_up_to(num):
    for num in range(num + 1):
        print(num)

print_up_to(15)

print_up_to(20)

def area(length, width):
    return length * width

print(area(10,20))

def get_max(nums):
    current_biggest = None
    for num in nums:
        if current_biggest == None:
            current_biggest = num 

        if current_biggest < num:
            current_biggest = num
    return current_biggest

big = [100,200,300]

print(get_max(big))