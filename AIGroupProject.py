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

###call function for frequency of words
freq_word_func('readme.txt')