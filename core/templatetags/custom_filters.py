from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def number_formatter(value, num_decimals=2):
    """
    Django template filter to convert regular numbers to a
    cool format (ie: 2K, 434.4K, 33M...)
    :param value: number
    :param num_decimals: Number of decimal digits

    Source: https://gist.github.com/dnmellen/bfc1b3005999aaff3ed4
    """

    int_value = int(value)
    formatted_number = "{{:.{}f}}".format(num_decimals)
    if int_value < 1000:
        return str(int_value)
    elif int_value < 1000000:
        return formatted_number.format(int_value / 1000.0).rstrip("0").rstrip(".") + "K"
    else:
        return (
            formatted_number.format(int_value / 1000000.0).rstrip("0").rstrip(".") + "M"
        )


@register.filter
@stringfilter
def counter_by_model(value, arg):
    """Filter to fetch a dict's value by a variable as key"""
    return "0"
