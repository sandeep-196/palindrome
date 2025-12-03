def is_palindrome(text):
    return text == text[::-1]
word="MALAYALAM"
if is_palindrome(word):
     print("this string is palindrome")
else:
     print("This is not palindrome")
