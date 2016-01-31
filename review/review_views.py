# Create your views here.
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.views.generic.edit import FormView, CreateView

from review.forms import CommentForm


class CreateCommentView(CreateView):
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user.member
        comment.save()
        return HttpResponse()