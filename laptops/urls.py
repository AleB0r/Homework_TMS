from django.urls import path

from laptops.views import (
    LaptopsListView,
    AddLaptopView, LaptopDetailView, MyLaptopsView, EditLaptopView, LaptopAddFavorite, LaptopCheckFavorite,
    FavoritesView, AddToCartView, ViewCart

)

urlpatterns = [
    path("", LaptopsListView.as_view(), name="laptops_list"),
    path('add/', AddLaptopView.as_view(), name='laptop_add'),
    path('<int:pk>/', LaptopDetailView.as_view(), name='laptop_details'),
    path('my-laptops/', MyLaptopsView.as_view(), name='my_laptops'),
    path('edit/<int:pk>/', EditLaptopView.as_view(), name='laptop_edit'),
    path('favorite/<int:pk>/', LaptopAddFavorite, name='laptop_add_favorite'),
    path('favorite/<int:pk>/check/', LaptopCheckFavorite.as_view(), name='laptop_check_favorite'),
    path('favorites/', FavoritesView.as_view(), name='view_favorites'),
    path('add-to-cart/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', ViewCart.as_view(), name='view_cart'),
]
