'''write a program that:
a)Capitalize each alphabet of first word
b)ends with ('.')
c)removes whitespaces
d)replace old_word with new_word'''

# capitalize the first alphabet of each word in a sentence
def capitalize_title(title):
    return title.title()


# return True if sentence ends with '.'
def check_sentence_ending(sentence):
    return sentence.endswith('.')

# remove all whitespaces from a sentence
def clean_up_spacing(sentence):
    return sentence.strip()

# replace old_word with new_word
def replace_word_choice(sentence, old_word, new_word):
    return sentence.replace(old_word, new_word)
