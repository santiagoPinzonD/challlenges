def checkPalindrome(inputString):
    if str(inputString) == str(inputString)[::-1]:
        print("is palindrome")
    else:
        print("is not palindrome")
