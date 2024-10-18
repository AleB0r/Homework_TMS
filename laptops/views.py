from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from laptops.forms import AddLaptopForm, EditLaptopForm
from laptops.models import Laptop, FavoriteLaptop, Cart


class LaptopsListView(ListView):
    model = Laptop
    template_name = 'laptops.html'


class AddLaptopView(LoginRequiredMixin, CreateView):
    form_class = AddLaptopForm
    template_name = 'laptop_add.html'
    success_url = reverse_lazy('laptops_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LaptopDetailView(DetailView):
    model = Laptop
    template_name = 'laptop_detail.html'
    context_object_name = 'laptop'


class MyLaptopsView(LoginRequiredMixin, ListView):
    model = Laptop
    template_name = 'my_laptops.html'
    context_object_name = 'laptops'

    def get_queryset(self):
        return Laptop.objects.filter(user=self.request.user)


class EditLaptopView(LoginRequiredMixin, UpdateView):
    model = Laptop
    form_class = EditLaptopForm
    template_name = 'edit_laptop.html'

    def get_success_url(self):
        return reverse_lazy('laptop_details', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        # Получаем экземпляр ноутбука
        self.object = self.get_object()

        # Проверяем, является ли текущий пользователь владельцем ноутбука
        if self.object.user != self.request.user:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)

@csrf_exempt
@login_required
def LaptopAddFavorite(request, pk):
    user= request.user
    laptop = get_object_or_404(Laptop, pk=pk)
    if user in laptop.favorites.all():
        laptop.favorites.remove(user)
    else:
        laptop.favorites.add(user)
    laptop.save()
    return JsonResponse({'Status': "ok"})


class LaptopCheckFavorite(LoginRequiredMixin, View):
    def get(self, request, pk):
        try:
            laptop = Laptop.objects.get(pk=pk)
            is_liked = laptop.is_liked_by_user(request.user)
            return JsonResponse({"isLiked": is_liked})
        except Laptop.DoesNotExist:
            return JsonResponse({"error": "Laptop does not exist"}, status=404)


class FavoritesView(LoginRequiredMixin, ListView):
    model = Laptop
    template_name = 'favorites.html'
    context_object_name = 'favorite_laptops'

    def get_queryset(self):
        user = self.request.user
        return Laptop.objects.filter(favoritelaptop__user=user)


class AddToCartView(View):
    def post(self, request, pk):
        laptop = Laptop.objects.get(pk=pk)
        user = request.user

        # Get or create the cart for the user
        cart, created = Cart.objects.get_or_create(user=user)

        # Add the laptop to the cart
        cart.laptops.add(laptop)

        messages.success(request, f"{laptop.name} has been added to your cart.")
        return redirect('view_cart')


class ViewCart(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user

        # Retrieve the cart for the user
        cart = Cart.objects.get(user=user)

        context = {
            'cart': cart,
        }

        return render(request, 'cart.html', context)