word = str(input())
word_1 = word[: :-1]

def is_palindrome():
    if word_1 == word:
        print("True")
    else:
        print("False")

is_palindrome()
    