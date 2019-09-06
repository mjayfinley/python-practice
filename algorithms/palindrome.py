user_word = input('Please enter a word: ')


def palindrome(word):
    for i in range(0, len(word)):
        if word[i] != word[len(word) - i - 1]:
            return False
        else:
            return True


# print(f'{word} is not a palindrome')
# print(f'{word} is a palindrome')
print(palindrome(user_word))


def palindrome_build_in(word):
    rev = ''.join(reversed(word))
    print(rev)

    if (word == rev):
        return True
    return False


print(palindrome_build_in(user_word))
