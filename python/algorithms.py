def directiveComparative(text):  # O(n)
    """

    :param text: text to be comparative
    :return bool: if the text is palindrome
    """
    text = text.lower().replace(" ", "")

    # Compare each character since the start to end.
    for i in range(len(text) // 2):  # O(n/2)
        if text[i] != text[len(text) - i - 1]:
            return False
    return True


def reversiComparative(text):
    """

    :param text: text to be comparative
    :return bool: if the text is palindrome
    """
    # Transform text to lower case and replce spaces without them
    text = text.lower().replace(" ", "")

    # Compare the text with his reverse part
    return text == text[::-1]


def recursiveApproach(text):  # O(n)
    """

    :param text: text to be comparative
    :return bool: if the text is palindrome
    """
    # Transform text to lower and replace it without spaces
    text = text.lower().replace(" ", "")

    def aux_function(s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return aux_function(s[1:-1])

    return aux_function(text)
