from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from accounts.forms import UserCreationForm


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/user_create.html', context={'form': form})


def login_view(request, *args, **kwargs):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url != 'None':
                return redirect(next_url)
            return redirect('list')
        else:
            context['has_error'] = True
            context['next'] = next_url
            context['username'] = username
    else:
        context = {'next': request.GET.get('next'), 'form': UserCreationForm}
    return render(request, 'registration/login.html', context=context)


def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('login')
