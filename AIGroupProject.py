from collections import Counter
import string

###word frequency
def freq_word_func(filepath):
    try:
        # Open the file
        with open(filepath, 'r', encoding='utf-8') as f:
            # Read the contents of the file
            text = f.read()
            # Make all the characters lowercase
            text = text.lower()
            # Remove punctuation marks and digits from the text
            text = text.translate(text.maketrans("", "", string.punctuation + string.digits))
            # Split the text into words
            words = text.split()
            # Count the frequency of each word
            word_freq = Counter(words)
            # Sort the words by frequency
            sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
            # Print the words and their frequency
            for word, frequency in sorted_words:
                print(f'{word} : {frequency}')
    except FileNotFoundError:
        print("File not found")
    except:
        print("An error occurred")
###character  frequency
def frequency_char(filepath):
    try:
        # Open the file
        with open(filepath, 'r', encoding='utf-8') as f:
            # Read the contents of the file
            text = f.read()
            # Make all the characters lowercase
            text = text.lower()
            # Remove punctuation marks, digits and whitespaces from the text
            text = text.translate(text.maketrans("", "", string.punctuation + string.digits + string.whitespace))
            # Count the frequency of each character
            char_freq = Counter(text)
            # Sort the characters by frequency
            sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
             # Print the first five most frequently occurring characters
            for i in range(5):
                print(sorted_chars[i])
    except FileNotFoundError:
        print("File not found")
    except:
        print("An error occurred")
###Stastical output
def text_stats(filepath):
    try:
        # Open the file
        with open(filepath, 'r', encoding='utf-8') as f:
            # Read the contents of the file
            text = f.read()
            # Remove punctuation marks from the text
            text = text.translate(text.maketrans("", "", string.punctuation))
            # Split the text into lines
            lines = text.split('\n')
            # Count the number of lines
            line_count = len(lines)
             # Split the text into words
            words = text.split()
            # Count the number of words
            word_count = len(words)
            # Count the number of characters
            char_count = len(text)
            # Print the statistics
            print(f'Total lines: {line_count}')
            print(f'Total words: {word_count}')
            print(f'Total characters: {char_count}')
    except FileNotFoundError:
        print("File not found")
    except:
        print("An error occurred")
        
###call function for frequency of words
freq_word_func('h.txt')
frequency_char('h.txt')
text_stats('h.txt')
