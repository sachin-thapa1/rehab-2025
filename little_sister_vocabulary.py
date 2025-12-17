"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return 'un' + word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    rest = [prefix + word for  word in vocab_words[1:]]
    return ' :: '.join([prefix] + rest)


def remove_suffix_ness(word):
    if word.endswith('ness'):
        base = word[:-4]
        if base.endswith('i'):
            base = base[:-1] + 'y'
    return base

def adjective_to_verb(sentence, index):
    base = sentence.split()
    word = base[index]
    word = word.strip('.')
    return word + 'en'
    