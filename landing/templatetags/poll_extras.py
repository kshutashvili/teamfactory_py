from django import template

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


