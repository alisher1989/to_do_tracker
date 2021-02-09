from django.contrib.auth.models import User
from django import forms


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password_confirm = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}), strip=False)
    username = forms.CharField(label="Username", strip=False, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(label="First name", strip=False, widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(label="Last name", strip=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']



