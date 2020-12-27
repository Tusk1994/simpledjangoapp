from django import template

from pymorphy2 import MorphAnalyzer
from pymorphy2.shapes import restore_capitalization

register = template.Library()
morph = MorphAnalyzer()


@register.filter
def plural(phrase, number):
    if not phrase or not number:
        return phrase
    return process_phrase(phrase, pluralize_word, number)


def process_phrase(phrase, func, number):
    parts = [func(part, number) for part in phrase.split()]
    return ' '.join(parts)


def pluralize_word(word, number):
    """
    Согласует слово с числом
    """

    parsed = morph.parse(word)
    if isinstance(parsed, list):
        pluralized = parsed[0].make_agree_with_number(number)
        if pluralized is not None:
            return restore_capitalization(pluralized.word, word)

    return word
