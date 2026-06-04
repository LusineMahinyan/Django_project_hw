from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import (
    get_user_model,
    login,
    authenticate,
    logout,
)

from users.forms import (
    UserRegisterForm,
    UserLoginForm,
)

User = get_user_model()


def register(request):

    if request.method == "POST":

        form = UserRegisterForm(
            request.POST
        )

        if form.is_valid():

            user = form.save(
                commit=False
            )

            user.set_password(
                form.cleaned_data["password"]
            )

            user.save()

            send_mail(
                subject="Добро пожаловать!",
                message="Спасибо за регистрацию в нашем магазине!",
                from_email=None,
                recipient_list=[user.email],
                fail_silently=False,
            )

            return redirect("users:login")
    else:

        form = UserRegisterForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "users/register.html",
        context,
    )


def user_login(request):

    if request.method == "POST":

        form = UserLoginForm(
            request,
            data=request.POST,
        )

        if form.is_valid():

            email = form.cleaned_data.get(
                "username"
            )

            password = form.cleaned_data.get(
                "password"
            )

            user = authenticate(
                request,
                email=email,
                password=password,
            )

            if user:

                login(
                    request,
                    user,
                )

                return redirect(
                    "catalog:home"
                )

    else:

        form = UserLoginForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "users/login.html",
        context,
    )


def user_logout(request):

    logout(request)

    return redirect(
        "catalog:home"
    )
