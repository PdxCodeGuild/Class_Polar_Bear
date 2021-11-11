from . import views
from django.urls import path

app_name = 'lab03_polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:qid>/', views.poll_features, name='poll_features'),
    path('<int:qid>/poll_results/', views.poll_results, name='poll_results'),
    path('<int:qid>/poll_vote/', views.poll_vote, name='poll_vote'),
]

