from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # <---- Here
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def roulette_home(request):
    context = {
        'username': request.user.username,
        'money': 1000,  # placeholder
    }
    return render(request, 'roulette/roulette.html', context)

@login_required
def leaderboard(request):
    profiles = Profile.objects.select_related('user').order_by('-money')
    return render(request, 'leaderboard.html', {'profiles': profiles})



