# Using the Python language, have the function AlphabetSoup(str) take the str string parameter being passed and return the string with the letters in alphabetical order (ie. hello becomes ehllo). Assume numbers and punctuation symbols will not be included in the string.
# Sample Test Cases
# Input:"coderbyte"

# Output:"bcdeeorty"


# Input:"hooplah"

# Output:"ahhloop"


def AlphabetSoup(string):
    ans = ''
    for y in range(0, len(string)):
        minCharVal = 1000
        minCharIndex = 0
        for x in range(0, len(string)):
            if ord(string[x]) < minCharVal:
                minCharVal = ord(string[x])
                minCharIndex = x
        ans += str(string[minCharIndex])
        string = string[:minCharIndex] + string[minCharIndex + 1:]
    print(ans)
# keep this function call here
AlphabetSoup(input())