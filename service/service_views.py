# # Create your views here.
# from django.views.generic.list import ListView
#
# from service.models import TaskModel, Skill
#
#
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

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


class ShowSkillView(ListView):
    model = Skill
    template_name = 'service/show_skill.html'
    context_object_name = 'skill'

    def get_queryset(self, *args, **kwargs):
        skill_id = self.kwargs.pop('skill_id', '')
        return get_object_or_404(Skill, id=skill_id)


class ShowOrders(ListView):
    model = Order
    template_name = 'service/show_orders.html'
    context_object_name = 'order'

    def get_queryset(self):
        return Order.objects.filter(basket__customer=self.request.user.member)
