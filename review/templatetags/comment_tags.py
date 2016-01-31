from django import template
from django.template.loader import render_to_string

from review.forms import CommentForm

register = template.Library()


@register.simple_tag(takes_context=True)
def comment_form_show(context, comment_set):
    context['comment_form'] = CommentForm(initial={'comment_set': comment_set})
    context['comment_set'] = comment_set
    return render_to_string('review/comment.html', context=context)
