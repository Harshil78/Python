str = 'hello world'
print(str)
print(str[0:9])
print(str[-7:-3])
print(str[:5])
print(str[6])
str1 = input("Enter any String:")
print(str1.isalnum())
print(str1.isalpha())
print(str1.isdigit())
print(str1.islower())
print(str1.isupper())
print(str1.isspace())

print(str1.find('co', 10))
print(str1.find('co', 10, 15))

print('co' in str1)
