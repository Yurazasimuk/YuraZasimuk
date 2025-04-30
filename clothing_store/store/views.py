from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Clothing, Category, Cart, Order

def home(request):
    categories = Category.objects.all()
    clothes = Clothing.objects.all()
    return render(request, 'store/home.html', {'categories': categories, 'clothes': clothes})

def clothing_detail(request, pk):
    item = get_object_or_404(Clothing, pk=pk)
    return render(request, 'store/clothing_detail.html', {'item': item})

def clothing_by_category(request, category_id):
    categories = Category.objects.all()
    clothes = Clothing.objects.filter(category_id=category_id)
    return render(request, 'store/home.html', {'categories': categories, 'clothes': clothes})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Cart.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})

@login_required
def add_to_cart(request, clothing_id):
    cart = get_object_or_404(Cart, user=request.user)
    item = get_object_or_404(Clothing, id=clothing_id)
    cart.items.add(item)
    return redirect('view_cart')

@login_required
def remove_from_cart(request, clothing_id):
    cart = get_object_or_404(Cart, user=request.user)
    item = get_object_or_404(Clothing, id=clothing_id)
    cart.items.remove(item)
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'store/cart.html', {'cart': cart})

@login_required
def place_order(request):
    cart = get_object_or_404(Cart, user=request.user)
    if cart.items.exists():
        order = Order.objects.create(user=request.user)
        order.items.set(cart.items.all())
        cart.items.clear()
    return redirect('view_orders')

@login_required
def view_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/orders.html', {'orders': orders})
