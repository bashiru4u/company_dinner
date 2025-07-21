from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Food, Vote
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('menu_list')
    else:
        form = SignUpForm()
    return render(request, 'menu/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('menu_list')


def menu_list(request):
    error = None
    # Inline login handling
    if request.method == 'POST' and 'username' in request.POST:
        uname = request.POST.get('username', '').strip()
        pwd   = request.POST.get('password', '').strip()
        if uname and pwd:
            user = authenticate(request, username=uname, password=pwd)
            if user:
                login(request, user)
                return redirect('menu_list')
            else:
                error = 'Invalid username or password'
    foods = Food.objects.all().annotate(votes_count=Count('votes'))
    # Global vote check: has this user voted any food?
    has_voted_any = request.user.is_authenticated and Vote.objects.filter(user=request.user).exists()
    return render(request, 'menu/menu_list.html', {
        'foods': foods,
        'has_voted_any': has_voted_any,
        'error': error,
    })


def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    # Global and per-food vote status
    has_voted_any = request.user.is_authenticated and Vote.objects.filter(user=request.user).exists()
    has_voted = has_voted_any and Vote.objects.filter(user=request.user, food=food).exists()
    return render(request, 'menu/food_detail.html', {
        'food': food,
        'has_voted_any': has_voted_any,
        'has_voted': has_voted,
    })


@login_required
def cast_vote(request, pk):
    # Only allow first vote
    if not Vote.objects.filter(user=request.user).exists():
        food = get_object_or_404(Food, pk=pk)
        Vote.objects.create(user=request.user, food=food)
    return redirect('menu_list')