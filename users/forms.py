from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()


class UserRegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    password_confirm = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User

        fields = (
            "email",
            "password",
            "password_confirm",
        )

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get(
            "password"
        )

        password_confirm = cleaned_data.get(
            "password_confirm"
        )

        if password != password_confirm:

            raise forms.ValidationError(
                "Пароли не совпадают"
            )

        return cleaned_data


class UserLoginForm(AuthenticationForm):

    username = forms.EmailField(
        label="Email"
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Пароль",
    )
