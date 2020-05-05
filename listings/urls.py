from django.urls import path

from listings import views

app_name = 'listings'

urlpatterns = [
    path('', views.ListingsListView.as_view(), name='listings'),
    path('<int:pk>/', views.ListingDetailView, name='listing'),
    path('search/', views.ListingSearchDetailView.as_view(), name='search'),
]
