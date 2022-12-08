from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, View
from django.core.mail import send_mail
from .forms import NewUserForm, NewProject, SendEmailForm
from .models import Proyectos
from portfolio.settings import EMAIL_HOST_USER
# Create your views here.

class index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["proyectos"] = Proyectos.objects.all()
        return context

class RegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = NewUserForm
    
    def form_valid(self, form):
        form.save()
        return redirect('login')

class RegisterProjectView(View):
    def get(self, request):
        context= {"form": NewProject}
        return render(request, "projects/register.html", context)
    
    def post(self, request):
        form = NewProject(request.POST)

        if form.is_valid():
            Proyectos.objects.create(**form.cleaned_data)
            return redirect('index')
        else:
            return redirect('index')

class email(View):
    def get(self, request):
        context= {"form": SendEmailForm}
        return render(request, "contact.html", context)
    
    def post(self, request):
        form = SendEmailForm(request.POST)

        if form.is_valid():
            send_mail(form.cleaned_data["asunto"], "Saludos, soy "+form.cleaned_data["nombre"]+". Este es mi mensaje:\n"+form.cleaned_data["mensaje"],form.cleaned_data["email"], [EMAIL_HOST_USER], fail_silently = False)
            return redirect('index')
        else:
            return redirect('email')
