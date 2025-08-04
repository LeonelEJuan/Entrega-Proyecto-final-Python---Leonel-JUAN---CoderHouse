from django import forms
from .models import CustomUser, RecruitmentRequest, Page
from django.contrib.auth.forms import UserCreationForm

# Formulario de registro para CEOs / empresas
class CEORegisterForm(UserCreationForm):
    company = forms.CharField(max_length=100, required=True, label="Empresa")
    position = forms.CharField(max_length=100, required=True, label="Cargo")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'company', 'position', 'password1', 'password2']


# Formulario para crear una página de blog
class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'subtitle', 'body', 'image']


# Formulario para solicitudes de reclutamiento
class RecruitmentRequestForm(forms.ModelForm):
    class Meta:
        model = RecruitmentRequest
        fields = ['role', 'experience_years', 'modality', 'description']
        labels = {
            'role': 'Perfil IT que necesita contratar',
            'experience_years': 'Años de experiencia requeridos',
            'modality': 'Modalidad de trabajo',
            'description': 'Descripción detallada del perfil o necesidades',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
