from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import CreateView, View, ListView
from django.core.mail import send_mail
from .forms import UserForm, ProjectForm, SendEmailForm
from .models import Proyectos, Tags, User
from portfolio.settings import EMAIL_HOST_USER
# Create your views here.

# class Index(ListView):
#     template_name = "index.html"
#     paginate_by = 6
#     model = Proyectos
#     ordering = ["id"]

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["tags"] = Tags.objects.all()
#         return context

def Index(request):
    if request.user.is_authenticated:
        projects_list = Proyectos.objects.filter(user_id=request.user.id)
        paginator = Paginator(projects_list[0], 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'index.html', {'page_obj': page_obj, 'tags':Tags.objects.all()})

    projects_list = Proyectos.objects.all()
    paginator = Paginator(projects_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj, 'tags':Tags.objects.all()})

class RegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = UserForm
    
    def form_valid(self, form):
        form.save()
        return redirect('login')

class RegisterProjectView(View):
    def get(self, request):
        context= {"form": ProjectForm}
        return render(request, "projects/register.html", context)
    
    def post(self, request):
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.cleaned_data["user_id"] = request.user.id
            Proyectos.objects.create(**form.cleaned_data)
            return redirect('index')
        else:
            return redirect('index')

class Email(View):
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

class DetailsOneProject(View):

    def get(self, request, id):
        proyecto = Proyectos.objects.get(pk=id)
        tags = Tags.objects.get(pk=proyecto.tags_id)
        user = User.objects.get(pk=proyecto.user_id)
        context = {
            "proyecto": proyecto,
            "tags": tags,
            "user": user
        }
        return render(request, "projects/details.html", context)

class EditProject(View):

    def get(self, request, id):
        proyecto = Proyectos.objects.get(pk=id)
        context = {
            "proyecto": proyecto,
            "form": ProjectForm
            }
        return render(request, "projects/edit.html", context)
    
    def post(self, request, id):
        form = ProjectForm(request.POST)

        if form.is_valid():
            proyecto = Proyectos.objects.filter(pk=id)
            form.cleaned_data["user_id"] = proyecto[0].user_id
            proyecto.update(**form.cleaned_data)
            return redirect('detailsOne', id)
        else:
            return redirect('editProject',id)