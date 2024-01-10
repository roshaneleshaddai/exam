from django.shortcuts import render
from .forms import SignupForm
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            return render(request, 'success.html', {'form_data': form.cleaned_data})
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})
