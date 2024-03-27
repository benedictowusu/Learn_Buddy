from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup_view(request):
    if request.method == 'post':
        form = UserCreationForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('dashboad:home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})