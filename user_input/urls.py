from django .urls import path
from . import views

urlpatterns=[
    path("",views.user_input, name="user_input/"),
    path("user_output/",views.user_output, name="user_output")
    
]