# Create your views here.
from django.views.generic.list import ListView

from service.models import TaskModel


class ShowCategories(ListView):
    model = TaskModel
    template_name = 'service/show_categories.html'
    context_object_name = 'task_models'

    def get_queryset(self):
        print("salam")
        return TaskModel.objects.all()

