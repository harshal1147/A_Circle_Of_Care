from django.urls import path
from microapp import views
urlpatterns = [
    path('',views.index,name='index'),
    path('feedback/',views.feedback,name='feedback'),
    path('ai-suggestions/',views.aisuggestions, name='aisuggestions'),
    path('about/',views.about,name='about'),
    path('footer/',views.footer,name='footer'),
    path('navbar/',views.navbar,name='navbar'),
    path('profile/',views.profile,name='profile'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('terms/',views.terms,name='terms'),
    path('logout/', views.logout_view, name='logout'),

    path('api/chat/', views.chat_api, name='chat_api'),
    path('ai-assistant/', views.ai_assistant_view, name='assistant'),

]