from django.urls import path
import apps.jobhunt.views as views
urlpatterns = [
    path('', views.application_list, name='application_list'),
    path('create/', views.application_create, name='application_create'),
    path('/update/', views.application_update, name='application_update'),
    path('/delete/', views.application_delete, name='application_delete'),
]
