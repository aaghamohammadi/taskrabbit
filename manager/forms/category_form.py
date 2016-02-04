from django.forms import ModelForm
from service.models import Category


class CreateCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        labels = {
            "name": 'نام دسته بندی',
            "image": 'عکس'
        }
