from django.urls import path
from . import views

app_name = 'video_games'
urlpatterns = [
    # ex: /video_games/
    path('', views.index, name='index'),
    # ex: /video_games/5/
    path('<int:console_id>/', views.detail, name='detail'),
    path('<int:console_id>/comment_detail', views.comment_detail, name='comment_detail'),
]
