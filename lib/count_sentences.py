#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  # Use the setter to assign the initial value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        """Returns True if the value ends with a period."""
        return self.value.endswith('.')

    def is_question(self):
        """Returns True if the value ends with a question mark."""
        return self.value.endswith('?')

    def is_exclamation(self):
        """Returns True if the value ends with an exclamation mark."""
        return self.value.endswith('!')

    def count_sentences(self):
        """Counts the number of sentences in the value."""
        import re
        # Split the string by sentence-ending punctuation
        sentences = re.split(r'[.!?]+', self.value)
        # Filter out any empty strings
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)

# Example usage
simple_string = MyString("one. two. three?")
print(simple_string.count_sentences())  # Output: 3