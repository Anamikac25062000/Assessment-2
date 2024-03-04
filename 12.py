#12) Write a function that takes a sentence as input and returns a new sentence with the words reversed, while keeping the order of the words in the sentence.



input_sentence = input("Enter a sentence: ")
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = reversed(words)
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

result = reverse_words(input_sentence)

print("Reversed sentence with reversed words:", result)
