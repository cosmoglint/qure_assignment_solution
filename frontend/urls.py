from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [

    path('', views.index, name='home'),
    path('sign_up/', views.sign_up, name="sign-up"),
    path('people/', views.index),
    path('accounts/', include('django.contrib.auth.urls')),
    path('people_list/', views.people_list, name="people_list"),
    path('user/', views.get_user, name="current_user"),

]
