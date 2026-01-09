text = input("Enter Text: ")

numOfLetters = 0
numOfWords = 0
numOfDigits = 0

for i in text:
    i = i.lower()
    if i>='a' and i<='z':
        numOfLetters = numOfLetters + 1
    elif i>='0' and i<='9':
        numOfDigits = numOfDigits + 1
    elif i==' ':
        numOfWords = numOfWords + 1

print("Number of Letters: ", numOfLetters)
print("Number of Digits: ", numOfDigits)
print("Number of Words: ", numOfWords + 1)