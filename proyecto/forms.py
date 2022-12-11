from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tags

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        """ Vamos a indicar que este formulario pertenece a un modelo """
        model = User
        """ Podemos definir que campos seran los que mostremos usando el atributo fields """
        fields = ("username", "first_name", "last_name", "email",  "password1", "password2")

    """ Vamos a sobreescribir el metodo save """
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        # colocamos el email
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ProjectForm(forms.Form):
    url_foto = forms.CharField(max_length=300)
    proyecto = forms.CharField(max_length=200)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    tags = forms.ModelChoiceField(queryset=Tags.objects.all(), empty_label=None)
    github = forms.CharField(max_length=200)

class SendEmailForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    asunto = forms.CharField(max_length=100)
    mensaje = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))