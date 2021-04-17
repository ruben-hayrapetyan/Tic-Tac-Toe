def correct_sentence(text: str) -> str:
    if text[0].isupper() and text[-1] == '.':
        print(text)
        return text

    elif text[0].isupper() and text[-1] != '.':
        print(text)
        text = text + '.'
        print(text)
        return text

    elif (not text[0].isupper()) and text[-1] == '.':
        print(text)
        position = 0
        n_character = text[0].upper()
        print(n_character)
        string = text[:position] + n_character + text[position + 1:]
        print(string)
        return string


    elif (not text[0].isupper()) and (text[-1] != '.'):
        print(text)
        text = text + '.'
        print(text)
        position = 0
        n_character = text[0].upper()
        print(n_character)
        string = text[:position] + n_character + text[position + 1:]
        return string


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")
