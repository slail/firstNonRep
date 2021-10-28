def firstNonRepeatingCharacter(string):
    """
    Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the
    string's first non-repeating character. The first non-repeating character is the first character in a string that
    occurs only once. If the input string doesn't have any non-repeating characters, your function should return -1.
    """
    character_frequency = {}
    for character in string:
        character_frequency[character] = character_frequency.get(character, 0) + 1

    for index in range(len(string)):
        character = string[index]
        if character_frequency[character] == 1:
            return index
    return -1


print(firstNonRepeatingCharacter("abcdaef"))
