from is_palindrome import is_palindrome

# 1. Basic palindrome
assert is_palindrome("Racecar") == True

# 2. Palindrome with spaces and punctuation
assert is_palindrome("A man, a plan, a canal: Panama") == True

# 3. Not a palindrome
assert is_palindrome("ChatGPT") == False
