def print_upper_words(words, staring_chars=[]):
    """Takes a list of words and prints out each word on a separate line,
    in full CAPS. You can optionally supply a list of starting_chars
    to require words to start with those chars to be printed."""

    for word in words:
        if staring_chars:
            for char in staring_chars:
                if word.lower().startswith(char.lower()):
                    print(word.upper())
        else:
            print(word.upper())


print_upper_words(
    words=["hello", "hey", "goodbye", "yo", "yes"], staring_chars=["h", "Y"]
)
