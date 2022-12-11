from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('ligue', views.LigueView.as_view(), name='ligue'),
    path('<int:pk>/', views.EquipeView.as_view(), name='detail'),
    path('<int:question_id>/results/', views.ResultsView.as_view(), name='results'),
    path('form', views.AddMatch, name='Add-Match')
]