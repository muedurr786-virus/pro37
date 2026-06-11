from django.urls import path
from .views import *

urlpatterns = [
    path('',Departmentpage,name='department'),
    path('departmentedit/edit<int:id>/',Departmenteditpage,name='departmentedit'),
    path('departmentdelet/edit<int:id>/',Departmentdeletepage,name='departmentdelet'),
    path('teacher/',Techarpage, name='teacher'),
    path('departmentedit/edit<int:id>/',Techareditpage,name='Techareditpage'),
    path('departmentdelet/edit<int:id>/',Techardeletpage,name='Techardeletpage'),
    # path('student/',studentpage,name='student'),
]
