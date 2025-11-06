from collections import Counter

text = input("Enter a paragraph: ")

words = text.lower().split()

total_words = len(words)

word_freq = Counter(words)

top_3_words = word_freq.most_common(3)

vowels = "aeiou"
vowel_count = sum(1 for char in text.lower() if char in vowels)


print("\n--- Text Analysis Results ---")
print("Total number of words:", total_words)
print("Word frequencies:", dict(word_freq))
print("Top 3 most frequent words:", top_3_words)
print("Total number of vowels:", vowel_count)