# Find most common words or Occurance of words 

from collections import Counter
import re


text = input("Enter your text: ")


words = re.findall(r'\b\w+\b', text.lower())


print("\nTotal number of words:", len(words))


word_frequency = Counter(words)

print("\nFrequency of each word:")
for word, count in word_frequency.items():
    print(word, ":", count)


print("\n10 most frequent words:")
for word, count in word_frequency.most_common(10):
    print(word, ":", count)