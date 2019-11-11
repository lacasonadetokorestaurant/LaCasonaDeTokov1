from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home:home')
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/auth/login/")
