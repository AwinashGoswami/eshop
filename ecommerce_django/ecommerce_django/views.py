
from django.shortcuts import render, redirect
from eshop.models import Category, Product, UserCreateForm
from django.contrib.auth import authenticate, login


def index(request):
    category = Category.objects.all()
    # product = Product.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        product = Product.objects.filter(
            sub_category=category_id).order_by('-id')
    else:
        product = Product.objects.all()

    context = {
        'category': category,
        'product': product
    }
    
    return render(request, 'index.html', context)


def base(request):
    return render(request, 'base.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']

            )
            login(request, new_user)
            return redirect('index')
        else:
            form = UserCreateForm()

        context = {
            'form': form
        }
        return render(request, 'auth/signup.html', context)
