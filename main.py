def getLetters(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    total_letters = 0

    for char in text:
        if char.isalpha():
            total_letters += 1

    return total_letters


def getChars(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    total_chars = 0

    for char in text:
        total_chars += 1

    return total_chars


def getWordCount(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    words = text.split()
    word_count = len(words)

    return word_count
  
