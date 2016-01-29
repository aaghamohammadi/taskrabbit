from django.contrib import admin

# Register your models here.
from review.models import Comment, Rating, CommentSet

admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(CommentSet)