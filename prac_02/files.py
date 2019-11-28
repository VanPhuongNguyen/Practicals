#Write file name
name = input('Enter the name: ')
f = open("name.txt", "w")
f.write(name)
f.close()

# Read file name
f = open("name.txt", "r")
name = f.read()
print('Your name is:', name)
f.close()

# Read two numbers

f = open("numbers.txt", "r")
number_1 = int(f.readline())
number_2 = int(f.readline())
sum = number_1 + number_2
print('The sum of two numbers is:', sum)
f.close()
# Read hole numbers
f = open("numbers.txt", "r")
numbers = f.read().split('\n')
for i in numbers:
    print(i)