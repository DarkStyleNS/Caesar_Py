from string import ascii_letters
letters = ascii_letters
length = len(letters)
word = str(input("please enter your name!!!"))
key = int(input("please enter key!!!"))
challange_word = ""
for letter in word:
    index = letters.index(letter)
    challange_index = (index + key)%length
    challange_letter = letters[challange_index]
    challange_word += challange_letter + " "
print(challange_word)
