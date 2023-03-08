from django.contrib.auth import login, authenticate


from django.shortcuts import render, redirect

from users.forms import UserRegistrationForm, LoginForm
from users.models import Person


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect("events_list")

    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('events_list')

    return render(
        request=request,
        template_name="registration/login.html",
        context={"form": form}
    )


def loginView(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('events_listC')
    return render(request, 'Registration/login.html', {'form': form})



