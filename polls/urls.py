from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('', views.logout, name="logout"),
    path('polls/', views.index, name='index'),
    path('polls/<int:question_id>/', views.detail, name='detail'),
    path('polls/<int:question_id>/results/', views.results, name='results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
    path('addquestion', views.addquestion, name="addquestion"),
]