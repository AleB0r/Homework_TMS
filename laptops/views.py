from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView

from laptops.forms import AddLaptopForm
from laptops.models import Laptop


class LaptopsListView(ListView):
    model = Laptop
    template_name = 'laptops.html'


class AddLaptopView(LoginRequiredMixin, CreateView):
    form_class = AddLaptopForm
    template_name = 'laptop_add.html'
    success_url = reverse_lazy('laptops_list')
