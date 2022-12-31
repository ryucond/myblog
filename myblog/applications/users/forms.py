from django import forms
from django.contrib.auth import authenticate

from .models import User


class UserRegisterForm(forms.ModelForm):
    
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )
    
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Contraseña'
            }
        )
    )
    
    class Meta:
        model = User
        fields = (
            'email',
            'full_name',
            'ocupacion',
            'genero',
            'date_birth'
        )
        widgets = {
            'email': forms.EmailInput(
                attrs= {
                    'type': 'email',
                    'placeholder': 'Ingresa correo electronico...'
                }
            ),
            'full_name': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingresa nombre completo...'
                }
            ),
            'ocupacion': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingresa tu ocupacion...'
                }
            ),
            'date_birth': forms.DateInput(
                attrs= {
                    'type': 'date',
                    'placeholder': 'Cuando naciste...'
                }
            ),
        }
        
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2','No coinciden las contraseñas...')
            
class LoginForm(forms.Form):
    
    email = forms.EmailField(
        #label='Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Email...',
                'style': '{ margin: 10px }',
            }
        )
    )
    
    password = forms.CharField(
        #label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña...'
            }
        )
    )
    
    def clean(self):
        cleaned_data = super(LoginForm,self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email,password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        
        
        return self.cleaned_data
    
class UpdatePasswordForm(forms.Form):
        
    password1 = forms.CharField(
        label='Contraseña Actual',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Ingresa Contraseña Actual...'
            }
        )
    )
    
    password2 = forms.CharField(
        label='Contraseña Nueva',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Ingresa Nueva Contraseña...'
            }
        )
    )
    
class VerificationForm(forms.Form):
    codregistro = forms.CharField(
        label='Codigo',
        required=True,
        max_length=6,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Ingresa codigo...'
            }
        )
    )
    
    def __init__(self,pk, *args, **kwargs):
            self.id_user = pk
            super(VerificationForm, self).__init__(*args, **kwargs)
    
    def clean_codregistro(self):
        codigo = self.cleaned_data['codregistro']
        
        if len(codigo) == 6:
            activo = User.objects.cod_validation(
                self.id_user,
                codigo
            )
            if not activo:
                raise forms.ValidationError('Codigo invalido...')
        
        else:
            raise forms.ValidationError('Codigo invalido...')
        