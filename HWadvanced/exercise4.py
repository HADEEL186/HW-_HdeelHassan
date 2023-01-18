def longest_word(filename):
    with open(filename, 'r') as file:
              words = file.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('text.txt'))