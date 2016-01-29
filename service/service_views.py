# # Create your views here.
# from django.views.generic.list import ListView
#
# from service.models import TaskModel, Skill
#
#
# class ShowCategories(ListView):
#     model = TaskModel
#     template_name = 'service/show_categories.html'
#     context_object_name = 'task_models'
#
#     def get_queryset(self):
#         return TaskModel.objects.all()
#
#
# class ShowTaskers(ListView):
#     model = Skill
#     template_name = 'service/show_taskers.html'
#     context_object_name = 'skills'
#
#     def get_queryset(self):
#         print(self.kwargs.get('task_model_id'))
#         return Skill.objects.filter(task_model_id=self.kwargs.get('task_model_id'))
from django.http.response import HttpResponse
from django.views.generic.edit import FormView

from service.forms.skill_form import SkillForm


class EditSkillView(FormView):
    template_name = 'service/edit_skill.html'
    form_class = SkillForm

    def form_valid(self, form):
        skill = form.save()
        self.request.user.member.skills.add(skill)
        return HttpResponse('مهارت شما با موفقیت ثبت شد.')
