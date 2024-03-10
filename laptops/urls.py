from django.urls import path

from laptops.views import (
                    laptops_list,
                    laptop_add,

                           )

urlpatterns = [
    path("", laptops_list, name="laptops_list"),
    path('add/', laptop_add, name='laptop_add'),
]
