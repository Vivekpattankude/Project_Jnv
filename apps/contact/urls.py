from django.urls import path
from apps.contact import views

urlpatterns = [
    path('', views.ContactList.as_view(), name='contact_list'),
    path('<int:pk>', views.ContactDetail.as_view(), name='contact_detail'),
]
