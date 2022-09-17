

number = 23456

# number = str(number)

# print(number[::-1])

# Finding the remainder by 10 will always get the last digit of the number
# If we divide any number by 10 and reassign it to itself we will get rid of the last digit.

last_digit = number % 10

number//=10 # We get rid of the actual last digit of the number on this line.

fourth_digit = number % 10
number//=10

third_digit = number %10
number//=10

second_digit = number %10
number//=10

first_digit = number %10
number//=10

reversed_num = str(last_digit) + str(fourth_digit)+str(third_digit) + str(second_digit)
+ str(first_digit)
print(reversed_num)
print(last_digit,fourth_digit,third_digit,second_digit,first_digit)














