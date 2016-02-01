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
from user.models import Member


class TaskerProfileView(ListView):
    model = Member
    template_name = 'service/tasker_profile.html'
    context_object_name = 'tasker'

    def get_queryset(self, *args, **kwargs):
        return self.request.tasker


class ShowCategoriesView(ListView):
    model = Category
    template_name = 'service/show_categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()


class ShowCategorySkills(ListView):
    model = Skill
    template_name = 'service/show_category_skills.html'
    context_object_name = 'skills'

    def get_queryset(self):
        print(self.kwargs.get('category_id'))
        return Skill.objects.filter(category_id=self.kwargs.get('category_id'))


class EditSkillView(FormView):
    template_name = 'service/edit_skill.html'
    form_class = SkillForm

    def form_valid(self, form):
        tasker = self.request.user.member
        skill = form.save(commit=False)
        skill.tasker = tasker
        skill.save()
        return redirect(reverse('service:show_my_skills'))


class ShowSkillView(ListView):
    model = Skill
    template_name = 'service/show_skill.html'
    context_object_name = 'skill'

    def get_queryset(self):
        skill_id = self.kwargs.pop('skill_id', '')
        return get_object_or_404(Skill, id=skill_id)


class ShowSkillsView(ListView):
    model = Skill
    template_name = 'service/show_skills.html'
    context_object_name = 'skills'

    def get_queryset(self):
        return Skill.objects.all()


class ShowTaskers(ListView):
    model = Member
    template_name = 'service/show_taskers.html'
    context_object_name = 'taskers'

    def get_queryset(self):
        query = Member.objects.exclude(skills__isnull=True)
        print(query)
        return query


class ShowOrders(ListView):
    model = Order
    template_name = 'service/show_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user.member)


class ShowFactor(ListView):
    model = Skill
    template_name = 'service/show_factor.html'
    context_object_name = 'skill'

    def get_queryset(self, **kwargs):
        return get_object_or_404(Skill, id=kwargs.get('skill_id'))
