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
