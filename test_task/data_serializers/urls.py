from django.urls import path
from data_serializers import views

urlpatterns = [
    path("sub_data/", views.SubdivisionView.as_view()),
    path("creat_user/", views.UserCreatView.as_view()),
    path("worker_detal_data/", views.WorkerDatalView.as_view()), 
    path("subworker_data/", views.SubWorkerView.as_view()),
    path("creat_subdivision/", views.SubdivisionCreatView.as_view()),
    path("creat_worker/", views.WorkerCreateView.as_view()),
]