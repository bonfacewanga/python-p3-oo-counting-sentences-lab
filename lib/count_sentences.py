#!/usr/bin/env python3
import re

class MyString:
    def __init__(self,value = ''):
        self.value = value
        
    def get_value(self):
        return self._value 
  
    def set_value(self,value):
        if isinstance(value, str):
            self._value = value
        else:
            print('The value must be a string.')

    value = property(get_value, set_value)

    def is_sentence(self):
        return True if self._value.endswith('.') else False
    
    def is_question(self):
    
        return True if self._value.endswith('?') else False
    def is_exclamation(self):
        return True if self._value.endswith('!') else False

    def count_sentences(self):
        sentence = self._value
        char = ['.','!','?']
        for i in sentence:
            if i in char:
                sentence = sentence.replace(i,'-')
        result = re.split('-',sentence)
        clean = [word for word in result if word != '']
        length = len(clean)
        # print(new) 
        return length

