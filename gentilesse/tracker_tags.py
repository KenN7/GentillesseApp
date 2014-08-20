from django import template
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils.html import escape

register = template.Library()

@register.simple_tag
def label_style(label):
    if label.inverted:
        fg = '#fff'
    else:
        fg = '#000'
        style = "background-color: {bg}; color: {fg}; vertical-align: middle;"
        return style.format(bg=label.color, fg=fg)
