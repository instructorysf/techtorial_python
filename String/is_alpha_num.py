
# isalpha() method
# It only returns true when all charachter of the string is letters .

s = "This is text"
print(s.isalpha()) 
# False and the reason for that is spaces are not considered as letters. 

# s = s.replace(" ","")
print(s.replace(" ","").isalpha())
#True because using replace method we removed all the spaces from the string.

print(s.replace(" ","-").isalpha())
# IT will print False because - is not a letter.

print(type(s.isalpha())) # class<bool>

# isnumeric() only returns true when all the charachters are numeric 

s1 = "777-777-7777"
print(s1.isnumeric())
#False because - is not a numeric type.

print(s1.replace("-","").isnumeric())
# True
s1 = "7777b4eh3"
print(s1.isnumeric())
# It will return False

# isalnum checks if the all string consist of letters and numbers

print(s1.isalnum())
#It will True
s1 = "777-777-7777"

print(s1.isalnum())
#False because it has - 

s2 = "string"
s3 ="777777"
print(s2.isalnum()) #
print(s3.isalnum()) #
















