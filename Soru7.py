from collections import Counter
import re

def most_common_letter_with_word(text):
    # Remove non-alphabetic characters and split the text into words
    words = re.findall(r'\b\w+\b', text.lower())

    # Join all words to form a single string
    cleaned_text = ''.join(words)

    # Count the occurrences of each letter in the cleaned text
    letter_counts = Counter(cleaned_text)

    # Find the most common letter
    most_common_letter, frequency = letter_counts.most_common(1)[0]

    # Find the word containing the most common letter
    for word in words:
        if most_common_letter in word:
            return most_common_letter, word

    # If the most common letter is not found in any word (unlikely), return None
    return most_common_letter, None

# Prompt the user to enter a text string
text = input("Please enter a text with at least 7 words, including your name and surname: ")

# Find and display the most common letter and the word containing it in the text
common_letter, word_with_letter = most_common_letter_with_word(text)
print("The most frequently occurring letter in the entered text is:", common_letter)
if word_with_letter:
    print("The word containing the most frequent letter is:", word_with_letter)
else:
    print("The most frequent letter does not appear within any word.")




