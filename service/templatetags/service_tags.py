from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def show_skill(context, skill, num):
    context['skill'] = skill
    context['num'] = num
    return render_to_string('service/tags/show_skill.html', context=context)
