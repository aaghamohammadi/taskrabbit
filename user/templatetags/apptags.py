from django import template

register = template.Library()


@register.filter(name='field_type')
def field_type(field):
    return field.field.widget.__class__.__name__


@register.filter
def selected_choice(form, field_name):
    return dict(form.fields[field_name].choices)[form.data[field_name]]
