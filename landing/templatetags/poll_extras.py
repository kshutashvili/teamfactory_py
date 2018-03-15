# This Python file uses the following encoding: utf-8

from django import template
from django.urls import resolve, reverse
from django.utils import translation
register = template.Library()

@register.filter(name='first_digit')
def first_digit(number):
	if number == 0:
		return 'none-seats'
	else:
		return str(number)[0]


@register.filter(name='last_digit')
def last_digit(number):
	if len(str(number)) == 1:
		return 'style-none'
	else:
		return str(number)[1]

@register.filter(name='zero_count_seats')
def zero_count_seats(number):
	if number == 0:
		return 'zero-number'
	else:
		return ''






class TranslatedURL(template.Node):
    def __init__(self, language):
        self.language = language

    def render(self, context):
        view = resolve(context['request'].path)
        request_language = translation.get_language()
        translation.activate(self.language)
        print(view.args)
        url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        translation.activate(request_language)
        context['request'].session[translation.LANGUAGE_SESSION_KEY] = request_language
        return url


@register.tag(name='translate_url')
def do_translate_url(parser, token):
    language = token.split_contents()[1]
    return TranslatedURL(language)
