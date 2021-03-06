from django.urls import path

from pages import views

app_name = 'pages'

urlpatterns = [
    path('', views.MainPageView.as_view(), name='index'),
    path('about/', views.AboutPageView.as_view(), name='about'),
]
