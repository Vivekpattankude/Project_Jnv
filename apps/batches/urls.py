from django.urls import path
from apps.batches import views
# from django.conf.urls import url

urlpatterns = [
    path('', views.BatchesList.as_view(), name='batches_list'),
    path('<int:pk>', views.BatchesDetail.as_view(), name='batches_detail'),
]
# urlpatterns=[
#      url('',views.batchesApi),
#      url('<int:pk>',views.batchesApi),
# ]

