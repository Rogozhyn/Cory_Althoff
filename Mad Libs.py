import re

text = """
Giraffes have aroused the curiosity of __PLURAL_NOUN__ since earliest times.
The giraffe is the tallest of all living __PLURAL_NOUN__,
but scientists are unable to explain how it got its long __PART_OF_THE_BODY__.
The giraffe's tremendous height, which might reach __NUMBER__ __PLURAL_NOUN__,
comes from its legs and __BODYPART__.
"""


def mad_libs(mls):
    """
    :param mls: String with parts the user should fill out surrounded
    by double underscores. Underscores cannot
    be inside hint e.g., no __hint_hint__ only __hint__.
    """
    hints = re.findall("__.*?__", mls)
    if hints:
        for word in hints:
            new_word = input("enter a {}: ".format(word))
            mls = mls.replace(word, new_word, 1)
        print('\n ')
        print(mls)
    else:
        print("invalid mls")


mad_libs(text)
