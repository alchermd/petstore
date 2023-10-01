from django import template

register = template.Library()


def itoprice(value):
    return "$" + str(value / 100)


register.filter("itoprice", itoprice)
