from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('', views.LigueView.as_view(), name='ligues'),
    path('class_equipes/<int:ligue_id>', views.EquipesView.as_view(), name='class_equipes'),
    path('<int:pk>/', views.EquipeView.as_view(), name='detail'),
    path('form', views.add_match, name='Add-Match'),
    path('form/<int:match_id>', views.modify_match, name='Modify-Match'),
    path('create_matches/<int:ligue_id>', views.create_matches, name='create_matches')
]