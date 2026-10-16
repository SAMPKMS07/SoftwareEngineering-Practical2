
# Software Engineering Practical 2
# Sample program for AWS CodeBuild

def add_numbers(a, b):
    return a + b

num1 = 10
num2 = 20

result = add_numbers(num1, num2)

print("AWS Software Engineering Practical 2")
print("First number:", num1)
print("Second number:", num2)
print("Sum:", result)

if result == 30:
    print("Test Passed!")
else:
    print("Test Failed!")
