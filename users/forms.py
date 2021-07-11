from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=200, label='E-mail/ Usuário')
    password = forms.CharField(max_length=60, label='Senha', widget=forms.PasswordInput)

    def save(self):
        print(self.email)
