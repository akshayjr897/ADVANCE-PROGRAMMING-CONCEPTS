# Find-and-Replace Operations in Text Files


filename = input("Enter the file name: ")


target = input("Enter the word or phrase to find: ")
replacement = input("Enter the replacement word or phrase: ")


choice = input("Case-sensitive replacement? (yes/no): ")


with open(filename, "r") as file:
    text = file.read()


if choice.lower() == "yes":
    new_text = text.replace(target, replacement)

else:
    import re
    new_text = re.sub(re.escape(target), replacement, text, flags=re.IGNORECASE)

new_filename = "modified_" + filename

with open(new_filename, "w") as file:
    file.write(new_text)

print("Replacement completed successfully!")
print("Modified file saved as:", new_filename)