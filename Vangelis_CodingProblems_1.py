import math
a = input("Please enter a number: ")
b = input("Please enter another number: ")
a = int(a)
b = int(b)

sum_result = a + b
print("The sum of a and b is", sum_result)

diff_result = a - b
print("The difference when b is subtracted from a is", diff_result)

prod_result = a * b
print("The product of a and b is", prod_result)

quot_result = a // b
print("The quotient when a is divided by b is", quot_result)

mod_result = a % b
print("The remainder when a is divided by b is", mod_result)

log_result = math.log10(a)
print("The result of log{10}a is", log_result)

exp_result = a ** b
print("The result of a^b is", exp_result)