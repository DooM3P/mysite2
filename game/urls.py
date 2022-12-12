from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('', views.LigueView.as_view(), name='ligues'),
    path('class_equipes/<int:ligue_id>', views.EquipesView.as_view(), name='class_equipes'),
    path('<int:pk>/', views.EquipeView.as_view(), name='detail'),
    path('<int:question_id>/results/', views.ResultsView.as_view(), name='results'),
    path('form', views.AddMatch, name='Add-Match')
]