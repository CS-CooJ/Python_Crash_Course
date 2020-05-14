#4/23 This is the Try It Yourself work from chapter 2.
name = "joanna schindel"
message = "Hi, " + name.title() + " I am trying to learn Python.\n"
print(message)

name2 = "carol schindel"
print(name2.lower())#makes all letters lowercase
print(name2.upper())#makes all letters uppercase.
print(name2.title())#Adds Uppercase letter at beginning of words.

message = "2 Corinthians 5:17 says, 'Therefore, if anyone is in Christ,\nhe is a new creation. The old has passed away, behold the new has come.\n"
print(message)

name3 = "jesus"
message2 = name3.title()  + " once said, 'Follow me and I will make you\nfishers of men.'"
print(message2)

strip_name = " john bunyan "
print(strip_name.rstrip())#removes blank spaces on the right
print(strip_name.lstrip()) #removes blank spaces on the left
print(strip_name.strip())#removes blank spaces on both right and left
print(strip_name.title().strip())

print(2 ** 3) #** makes it compute exponents, whereas 1 * is multiplication
print(16/2)
print(100 - 92)#doesn't matter if there are spaces or not
print(2.5 + 5.5)#a capital "P" in print will cause an error

favorite_number = 24
message = "My favorite number is str(favorite_number).\n\t TeeHee!"
print(message) #\n will create on new line, \t will tab

#This is a comment and is ignored by Python. It is used to maintain information about my code to help myself and others. 


