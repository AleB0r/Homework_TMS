from django.urls import path

from laptops.views import (
                    LaptopsListView,
                    AddLaptopView

                           )

urlpatterns = [
    path("", LaptopsListView.as_view(), name="laptops_list"),
    path('add/', AddLaptopView.as_view(), name='laptop_add'),
]
