#Task1
word = input("Input a word to reverse: ")
reversed_word = ""
for i in range(len(word)-1, -1, -1):
    reversed_word += word[i]
print("Reversed word:", reversed_word)


#Task2

characters = input("Input your characters: ")
digit_count = 0
letter_count = 0
for char in characters:
    if char.isdigit():
        digit_count += 1
    elif char.isalpha():
        letter_count += 1
print("Number of digits:", digit_count)
print("Number of letters:", letter_count)

#Task3
text = "Python is difficult\nYou need to search a lot\nAnd read a lot \nin order to improve your skills dixit Esther"
result = ""
index = 0
while index < len(text):
    char = text[index]
    if char.islower():
        result += char.upper()
    elif char.isupper():
        result += char.lower()
    else:
        result += char
    index += 1
print(result)

#Task4
start = int(input("Type starting integer: "))
end = int(input("Type ending integer: "))
divisor = int(input("Type divisor: "))

num = start
while num <= end:
    if divisor == 0:
        break
    if num % divisor == 0:
        print(num, "is divisible by", divisor)
    num += 1