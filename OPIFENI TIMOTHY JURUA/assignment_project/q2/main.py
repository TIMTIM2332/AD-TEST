from string_tools import count_vowels, is_palindrome

def main():
    text = input('Enter text: ')
    print('Vowels:', count_vowels(text))
    print('Palindrome:', is_palindrome(text))

if __name__ == '__main__':
    main()
