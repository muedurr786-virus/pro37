from django import forms
from .models import *


class DepartmentForm(forms.ModelForm):
    class Meta:
        model= DepartmentModel
        fields = "__all__"

class TeacherForms(forms.ModelForm):
    class Meta:
        model=TecharModel
        fields = "__all__"