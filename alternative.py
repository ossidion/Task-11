# This program reads in a string and makes each alternate
# character into an upper case character and each other alternate
# character a lower case character.

string = "My name is Alexander" # This is the string to which the case will be changed. 
new_string = "" # This variable will be used to contain the new string. 

i = 0 # This counter will be used to automate the program into a for loop.

for i in range(len(string)):            # A for loop has been used to add each character
    if i % 2 == 0:                      # from the "string". If the index of the character
        new_string += string[i].upper() # is even, the program will make that character
    else:                               # uppercase.  
        new_string += string[i].lower() # Odds will be added as lowercase.

print(new_string)   # The string is printed to the user. 

new_string_2 = []   # An empty list has been stored within the variable "new_string_2" so we
                    # can append to it at lines 23 and 25. 
new_string = string.split(" ")          # The string has been split into the "new_string" variable which 
for i in range(len(new_string)):        # is now a list. We can now iterate over each word. 
    if i % 2 == 0:                      # If the index of the item in the list is even, the program will 
        new_string_2.append(new_string[i].lower()) # make that character lowercase and add it to the empty  
    else:                               # list "new_sting_2" which was declared at line 18.
        new_string_2.append(new_string[i].upper()) # Odds will be added as uppercase.

new_string_2 = " ".join(new_string_2)   # The list is joined together as a string with spaces inbetween each
print(new_string_2)                     # item from the list. 

