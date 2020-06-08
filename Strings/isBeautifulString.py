'''
String is said to be beautiful if each letter of the string appears at most as
many times as the previous letter in the alphabet within the string.

b cannot occur more times than a; c occurs no more times than b

Ex: isBeatifulString('bbbaacdafe') -> True

'''

# TS O(n)
def isBeautifulString(string):
    
    # Input = @string : string
    # Output = @boolean
    
    if string is None:
        return False

    lookup = {}

    for character in string:
        lookup[character]= lookup.get(character, 0) + 1

    for current_char in lookup:
        prev_char_freq = lookup.get(chr(ord(current_char) -1), None)
        
        if prev_char_freq is None or lookup[current_char] > prev_char_freq:
            if current_char is not 'a':
                return False

    return True

print(isBeautifulString('aaabbbccddeef'))# True
print(isBeautifulString('aabbb'))        # False
print(isBeautifulString('bbc'))          # False
print(isBeautifulString('bbbaacdafe'))   # True
