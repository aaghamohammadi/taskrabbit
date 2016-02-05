from django.shortcuts import render
from django.views.generic.edit import FormView

from service.models import Skill
from user.forms import SearchForm


class Search(FormView):
    template_name = 'search.html'
    form_class = SearchForm

    def form_valid(self, form):
        data = form.cleaned_data
        skill_name = data['skill_name']
        city = data['city']
        location = data['location']
        max_price = data['max_price']
        min_rate = data['min_rate']
        context = self.get_context_data()
        print(max_price)
        skills = Skill.objects.filter(price__lte=max_price).filter(rate__gte=min_rate).filter(
                title__contains=skill_name).filter(tasker__city__contains=city).filter(
            tasker__address__contains=location)
        context['skills'] = skills
        return render(self.request, template_name=self.template_name, context=context)
