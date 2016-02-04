# Create your views here.
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.views.generic.edit import FormView, CreateView

from review.forms import CommentForm, RatingForm


class CreateCommentView(CreateView):
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user.member
        comment.save()
        return HttpResponse()


class CreateRateView(CreateView):
    form_class = RatingForm

    def form_valid(self, form):
        rate = form.save(commit=False)
        rate.customer = self.request.user.member
        rate.save()
        self.change_status(rate.order)
        return HttpResponse()

    @staticmethod
    def change_status(order):
        print(order.status)
        order.status = 'D'
        order.save()
