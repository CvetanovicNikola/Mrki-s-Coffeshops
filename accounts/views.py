from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


""" def accounts(request):
    return render(request, "accounts.html")
 """


def login(request):
    if request.method == "POST":
        user = auth.authenticate(
            username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Username or password is incorrect."})
    else:
        return render(request, "login.html")


def signin(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Account created for {username} you can now log in.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "accounts/signin.html", {"form": form})

    """ if request.POST["username"] == "" or request.POST["password1"] == "" or request.POST["password2"] == "" or request.POST["email"] == "":
        return render(request, "accounts/signin.html", {"error": "Please fill all fields."})

    if len(request.POST["password1"]) < 6:
        return render(request, "accounts/signin.html", {"error": "Password must be at least 6 characters long."})

    if request.POST["password1"] == request.POST["password2"]:
        try:
            user = User.objects.get(username=request.POST["username"])
            return render(request, "accounts/signin.html", {"error": "Username already taken."})
        except User.DoesNotExist:
            user = User.objects.create_user(
                request.POST["username"], password=request.POST["password1"], email=request.POST["email"])
            auth.login(request, user)
            return redirect("home")
    else:
        return render(request, "accounts/signin.html", {"error": "Passwords must match."})
else:
    return render(request, "accounts/signin.html")
"""


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("home")


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, "Your account has been updated.")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {

        "u_form": u_form,
        "p_form": p_form

    }

    return render(request, "profile.html", context)
