string = input("Enter the string you want to see: ")

# start a dictionary to store the number of each character

char_count = {}

# navigate through the string and count the recurrence of each character
for i in string: 
   if i in char_count:
      char_count[i]+= 1
   else:
      char_count[i] = 1

# print the character frequency
for key, value in char_count.items(): 
    print(key + " = " + str(value))
