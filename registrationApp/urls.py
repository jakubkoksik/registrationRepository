from django.urls import path
from registrationApp import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('newPerson/', views.NewPewsonView.as_view(), name='newPerson'),
    path('done/', views.DoneView.as_view(), name='done'),
    path('personList/', views.PersonListView.as_view(), name='personList'),
    path('personDetail/<int:pk>/', views.PersonDetailView.as_view(), name='personDetail'),
    path('deletePerson/<int:pk>/', views.DeletePersonView.as_view(), name='deletePerson'),
    path('changeWorkStatus/<int:pk>/', views.changeWorkStatus, name='changeWorkStatus')
]