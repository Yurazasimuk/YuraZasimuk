from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .models import ClothingItem, Category

# Головна сторінка
def index(request):
    clothing_items = ClothingItem.objects.all()  # Вибір усіх товарів
    return render(request, 'store/index.html', {'clothing_items': clothing_items})

# Реєстрація
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Перенаправлення на головну сторінку
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})

# Вхід
def login_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Перенаправлення на головну сторінку
    else:
        form = UserCreationForm()
    return render(request, 'store/login.html', {'form': form})

# Вихід
def logout_view(request):
    logout(request)
    return redirect('index')  # Перенаправлення на головну сторінку

# Перегляд товару
def clothing_item_detail(request, item_id):
    item = ClothingItem.objects.get(id=item_id)
    return render(request, 'store/clothing_item_detail.html', {'item': item})

# Додавання товару в корзину (сесія)
def add_to_cart(request, item_id):
    item = ClothingItem.objects.get(id=item_id)
    cart = request.session.get('cart', [])
    cart.append(item.id)
    request.session['cart'] = cart
    return redirect('index')

# Перегляд корзини
def view_cart(request):
    cart_ids = request.session.get('cart', [])
    cart_items = ClothingItem.objects.filter(id__in=cart_ids)
    total_price = sum(item.price for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})


class Order:
    pass

def checkout(request):
    cart_ids = request.session.get('cart', [])
    cart_items = ClothingItem.objects.filter(id__in=cart_ids)
    total_price = sum(item.price for item in cart_items)

    if request.method == 'POST':
        # Створюємо нове замовлення
        order = Order.objects.create(
            user=request.user,
            total_price=total_price,
        )

        # Додаємо товари в замовлення
        order.items.set(cart_items)
        order.save()

        # Очищаємо корзину в сесії
        request.session['cart'] = []

        return redirect('order_success')  # Перехід на сторінку успішного оформлення

    return render(request, 'store/checkout.html', {'cart_items': cart_items, 'total_price': total_price})
def order_success(request):
    return render(request, 'store/order_success.html')
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/order_history.html', {'orders': orders})
def remove_from_cart(request, item_id):
    cart = request.session.get('cart', [])
    if item_id in cart:
        cart.remove(item_id)
        request.session['cart'] = cart
    return redirect('view_cart')
def clothing_list(request):
    items = ClothingItem.objects.all()
    return render(request, 'store/clothing_list.html', {'items': items})
def item_detail(request, item_id):
    item = ClothingItem.objects.get(id=item_id)
    return render(request, 'store/item_detail.html', {'item': item})
def clothing_list(request):
    categories = Category.objects.all()
    clothing_items = ClothingItem.objects.all()
    return render(request, 'store/clothing_list.html', {'clothing_items': clothing_items, 'categories': categories})

def add_to_cart(request, item_id):
    cart = request.session.get('cart', [])
    cart.append(item_id)
    request.session['cart'] = cart
    return redirect('clothing_list')

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', [])
    cart.remove(item_id)
    request.session['cart'] = cart
    return redirect('view_cart')
def checkout(request):
    cart_ids = request.session.get('cart', [])
    cart_items = ClothingItem.objects.filter(id__in=cart_ids)
    total_price = sum(item.price for item in cart_items)
    if request.method == 'POST':
        order = Order.objects.create(user=request.user, total_price=total_price)
        order.items.set(cart_items)
        order.save()
        request.session['cart'] = []
        return redirect('order_detail', order_id=order.id)
    return render(request, 'store/checkout.html', {'cart_items': cart_items, 'total_price': total_price})
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/order_list.html', {'orders': orders})
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('password_change_done')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'store/change_password.html', {'form': form})
from django.shortcuts import render
from .models import ClothingItem, Category

def filter_clothing_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    clothing_items = ClothingItem.objects.filter(category=category)
    return render(request, 'store/clothing_list.html', {'clothing_items': clothing_items, 'category': category})
from django.shortcuts import redirect

def add_to_cart(request, item_id):
    cart = request.session.get('cart', [])
    if item_id not in cart:
        cart.append(item_id)
        request.session['cart'] = cart
    return redirect('view_cart')

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', [])
    if item_id in cart:
        cart.remove(item_id)
        request.session['cart'] = cart
    return redirect('view_cart')
from .models import Order

def place_order(request):
    cart_ids = request.session.get('cart', [])
    cart_items = ClothingItem.objects.filter(id__in=cart_ids)
    total_price = sum(item.price for item in cart_items)

    order = Order.objects.create(user=request.user, total_price=total_price)

    # Додати обробку замовлених товарів до замовлення
    for item in cart_items:
        order.items.add(item)

    # Очистити кошик
    request.session['cart'] = []

    return redirect('order_confirmation', order_id=order.id)
def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'store/order_confirmation.html', {'order': order})
def add_to_cart(request, item_id):
    cart = request.session.get('cart', [])
    if item_id in cart:
        cart.append(item_id)
    else:
        cart.append(item_id)
    request.session['cart'] = cart
    return redirect('view_cart')
# в store/views.py
from django.shortcuts import render
from .models import Order
from django.contrib.auth.decorators import login_required

@login_required
def view_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/my_orders.html', {'orders': orders})
from django.contrib.auth.decorators import login_required

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/my_orders.html', {'orders': orders})
# store/views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматичний вхід після реєстрації
            return redirect('home')  # Перенаправлення на головну сторінку після реєстрації
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})
# store/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
from django.contrib.auth.decorators import login_required

@login_required
def my_orders(request):
    # Твій код для обробки замовлень
    return render(request, 'store/my_orders.html')
# store/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправлення на сторінку логіну після реєстрації
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
# store/views.py
from django.shortcuts import render
from .models import ClothingItem

def clothing_list(request):
    # Отримуємо всі предмети одягу
    clothing_items = ClothingItem.objects.all()  # Замість ClothingItem потрібно використовувати модель твого одягу
    return render(request, 'store/clothing_list.html', {'clothing_items': clothing_items})
# store/views.py
from django.shortcuts import render
from .models import ClothingItem

def product_list(request):
    clothing_items = ClothingItem.objects.all()
    return render(request, 'store/products.html', {'clothing_items': clothing_items})
# store/views.py
from django.shortcuts import render
from .models import ClothingItem

def clothing_item_list(request):
    # Отримуємо всі товари з бази даних
    items = ClothingItem.objects.all()
    return render(request, 'store/clothing_item_list.html', {'items': items})
