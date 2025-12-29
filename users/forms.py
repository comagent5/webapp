from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm



class LoginUserForm(AuthenticationForm):  # forms.Form
    '''    username = forms.CharField(
        label='Логін',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть логін'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введіть пароль'})
    )
    або перевизначаємо поля як вище з class Bootstrap
    або створюємо __init__ в якому додаємо class в поля
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Додаємо клас form-control для Bootstrap стилізації
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Перевірка паролю', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': "Ім'я",
            'last_name': 'Призвіще'
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'})
        }
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Паролі не співпадають !')
        return cd['password1']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Такий E-mail вже існує !')
        return email


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='E-mail', required=True)

    class Meta:  # (UserCreationForm.Meta)
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = {
            'username': 'Логін',
            'first_name': "Ім'я",
            'last_name': 'Прізвище',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Автоматично додаємо клас 'form-control' до всіх полів
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Користувач з таким E-mail вже існує!')
        return email


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'first_name': "Ім'я",
            'last_name': 'Призвіще'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'})
        }


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старий пароль', 
                                   widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label='Новий пароль', 
                                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label='Підтвердження паролю', 
                                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    