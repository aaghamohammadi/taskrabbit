from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from django.views.generic import FormView, ListView

from manager.forms.category_form import CreateCategoryForm
from service.models import Category
from user.models import Member


class CreateCategoryView(FormView):
    template_name = 'manager/index.html'
    form_class = CreateCategoryForm

    def form_valid(self, form):
        form.save()

        return redirect(reverse('manager:show_categories.html'))


class ShowCategoriesView(ListView):
    model = Category
    template_name = 'manager/show_categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()


class ShowUsersView(ListView):
    model = Member
    template_name = 'manager/show_users.html'
    context_object_name = 'members'

    def get_queryset(self):
        return Member.objects.all()
