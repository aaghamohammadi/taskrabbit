# # Create your views here.
# from django.views.generic.list import ListView
#
# from service.models import TaskModel, Skill
#
#
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from review.forms import CommentForm
from service.forms.skill_form import SkillForm
from service.models import Skill, Category, Order


class ShowCategories(ListView):
    model = Category
    template_name = 'service/show_categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()


# class ShowTaskers(ListView):
#     model = Skill
#     template_name = 'service/show_taskers.html'
#     context_object_name = 'skills'
#
#     def get_queryset(self):
#         print(self.kwargs.get('task_model_id'))
#         return Skill.objects.filter(task_model_id=self.kwargs.get('task_model_id'))


class EditSkillView(FormView):
    template_name = 'service/edit_skill.html'
    form_class = SkillForm

    def form_valid(self, form):
        tasker = self.request.user.member
        skill = form.save(commit=False)
        skill.tasker = tasker
        skill.save()
        return redirect(reverse('service:show_my_skills'))


class ShowSkillsView(ListView):
    model = Skill
    template_name = 'service/show_skills.html'
    context_object_name = 'skills'

    def get_queryset(self, *args, **kwargs):
        print(self.request.tasker)
        return Skill.objects.all()


class ShowSkillView(TemplateView):
    model = Skill
    template_name = 'service/show_skill.html'
    context_object_name = 'skill'

    def get_context_data(self, **kwargs):
        context = super(ShowSkillView, self).get_context_data()
        skill_id = self.kwargs.pop('skill_id', '')
        context['skill'] = get_object_or_404(Skill, id=skill_id)
        context['comment_form'] = CommentForm(initial={'comment_set': context['skill'].comment_set})

        return context


class ShowOrders(ListView):
    model = Order
    template_name = 'service/show_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user.member)
