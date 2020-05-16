from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='app-listings'),
    path('<int:listing_id>', views.listing, name='app-listing'),
    path('search/', views.search, name='app-search'),

]
