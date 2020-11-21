from django.urls import path
from . import views
from .views import register, profile
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', register, name="register"),
    path('profile/', profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name='hackaton_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='hackaton_app/logout.html'), name='logout'),
    path('flashcard_create/', views.flashcard_create, name='flashcard_create'),
    path('flashcard_create_oquestion/', views.flashcard_create_oquestion, name='flashcard_create_oquestion'),
    path('flashcard_show/', views.Flashcard_ListView, name='flashcard_show'),
    path('assigned_flashcard/', views.AssignedFlashcardListView.as_view(), name='assigned_flashcard_show'),
    path('assign_flashcard/', views.flashcard_assign, name='assign_flashcard'),
]
