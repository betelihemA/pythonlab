import string
from collections import Counter
try:
        
        text=input("Enter a string : ")       
        # Remove punctuation marks from the line
        text = text.translate(text.maketrans("", "", string.punctuation + " "))
         # Count the frequency of each character
        char_freq = Counter(text)
        # Iterate through the character frequency dictionary
        for char, count in char_freq.items():
            if count == 1:
                print(f'{count} {char}')
            else:
                print(f'{count} {char}(s)')
except TypeError:
        print("Invalid Input provided")
except:
        print("An error occurred")
