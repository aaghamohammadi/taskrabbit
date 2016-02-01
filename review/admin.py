from django.contrib import admin

# Register your models here.
from review.models import Comment, Rate, CommentSet

admin.site.register(Comment)
admin.site.register(Rate)
admin.site.register(CommentSet)