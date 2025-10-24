def count_vowels(text):
    return sum(1 for ch in text if ch.lower() in 'aeiou')

def reverse_string(s):
    return s[::-1]
