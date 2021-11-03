# Author CCG 11/2/21

string = input('Enter a string: ')

x = len(string)

halfx = x // 2

print(string[0:halfx])
print(string[halfx:x])