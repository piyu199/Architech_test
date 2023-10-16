from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.create_contact,name='create_contact'),
    path('list_contact/',views.list_contact,name='list_contact'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('get_contact_list/',views.get_contact_list),
    path('contact_details/<int:id>/',views.contact_details)
]
