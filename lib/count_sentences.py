import re

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            print("The value must be a string.")
            self.value = ""
        else:
            self.value = value

    def is_sentence(self):
        '''Returns True if the value ends with a period.'''
        return self.value.endswith('.')

    def is_question(self):
        '''Returns True if the value ends with a question mark.'''
        return self.value.endswith('?')

    def is_exclamation(self):
        '''Returns True if the value ends with an exclamation mark.'''
        return self.value.endswith('!')

    def count_sentences(self):
        '''Returns the number of sentences (based on punctuation marks).'''
        if not self.value:
            return 0
        # Split the string by '.', '?', and '!' punctuation marks.
        sentences = re.split(r'[.?!]', self.value)
        # Filter out empty strings (which may result from split).
        return len([s for s in sentences if s.strip()])
