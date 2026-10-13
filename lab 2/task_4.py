text = input("Enter a word or short sentence: ")

char_count = 0
vowel_count = 0
space_count = 0

vowels = "aeiouAEIOU"

for char in text:
    char_count = char_count + 1

    if char in vowels:
        vowel_count = vowel_count + 1

    if char == " ":
        space_count = space_count + 1

print("Number of characters:", char_count)
print("Number of vowels:", vowel_count)
print("Number of spaces:", space_count)
