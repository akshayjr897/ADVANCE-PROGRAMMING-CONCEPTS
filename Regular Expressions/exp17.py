
# hastags yes or not 

import re

def extract_hashtags(text):
    pattern = r'#[A-Za-z0-9_]+'
    hashtags = re.findall(pattern, text)
    return hashtags

text = input("Enter your social media post: ")

print("Hashtags:", extract_hashtags(text))