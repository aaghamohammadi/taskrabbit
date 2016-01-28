
# from django.core.urlresolvers import reverse

# __author__ = 'garfild'
#
#
# class EditTask(FormView):
#     template_name = 'manager/edit_task.html'
#     form_class = EditTaskForm
#
#     def form_valid(self, form):
#         form.save()
#         return redirect(reverse('manager:task_model_list'))
#
#     def form_invalid(self, form):
#         print(form.errors)
#         return HttpResponse("ridi ")
#
#
# class ModelTaskList(ListView):
#     model = TaskModel
#     template_name = 'manager/show_task_models.html'
#     context_object_name = 'task_models'
#
#     def get_queryset(self):
#         return TaskModel.objects.all()
#
#
# class TaskerVerification(ListView):
#     # model = Customer
#     template_name = 'manager/verification.html'
#     context_object_name = 'Taskers'
#
#     # def get_queryset(self):
#     #     return Customer.objects.all()
#
#
# class DeleteTasker(View):
#     def post(self, request, **kwargs):
#         tasker_id = kwargs.pop('tasker_id')
#         # Customer.objects.get(id=tasker_id).delete()
#         return redirect(reverse('manager:verification_task'))
#
#
# class DeleteTask(View):
#     def post(self, request, **kwargs):
#         task_model_id = kwargs.pop('task_model_id')
#         TaskModel.objects.get(id=task_model_id).delete()
#         return redirect(reverse('manager:task_model_list'))
#
#
# class TaskerRegistration(FormView):
#     template_name = 'manager/tasker_registration.html'
#     form_class = TaskerRegistrationForm
#
#     def form_valid(self, form):
#         customer = form.save(commit=False)
#         email = form.cleaned_data['email']
#         user = User.objects.get(email=email)
#         customer.user = user
#         customer.save()
#         return redirect(reverse('manager:tasker_registration'))
#
