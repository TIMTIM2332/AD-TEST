def count_vowels(text):
    vowels = set('aeiouAEIOU')
    return sum(1 for ch in text if ch in vowels)

def is_palindrome(text):
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]
