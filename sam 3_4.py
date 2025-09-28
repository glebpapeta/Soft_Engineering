sentence = input("Enter a sentence: ")

print("Length:", len(sentence))
print("Lowercase:", sentence.lower())

vowels = 'aeiou'
vowel_count = sum(1 for char in sentence.lower() if char in vowels)
print("Vowel count:", vowel_count)

new_sentence = sentence.replace("ugly", "beauty")
print("After replacement:", new_sentence)

print("Starts with 'The':", sentence.startswith("The"))
print("Ends with 'end':", sentence.endswith("end"))
