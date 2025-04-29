from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import *
from .forms import *
from absensi.models import *
# Create your views here.

class DashboardPage(LoginRequiredMixin,TemplateView):
    template_name = "admin/pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_user"] = User.objects.count()
        context["total_student"] = Siswa.objects.count()
        return context
    

class LoginPage(LoginView):
    template_name = "login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True

class UserPage(LoginRequiredMixin,ListView):
    model = User
    template_name = "admin/pages/superuser.html"
    context_object_name = "Users"
    paginate_by = 10

    def get_queryset(self):
        query = super().get_queryset()
        search = self.request.GET.get("search")

        if search:
            query = User.objects.filter(username=search)

        return query
    

class StudentPage(LoginRequiredMixin,ListView):
    model = Siswa
    template_name = "admin/pages/student.html"
    context_object_name = "Students"
    paginate_by = 10

    def get_queryset(self):
        queryset= super().get_queryset()

        jurusan = self.request.GET.get("jurusan")
        kelas = self.request.GET.get("kelas")

        if jurusan:
            queryset = queryset.filter(jurusan=jurusan)
        if kelas:
            queryset = queryset.filter(kelas=kelas)

        return queryset
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["jurusan"] = Siswa.objects.values_list("jurusan", flat=True).distinct()
        context["kelas"] = Siswa.objects.values_list("kelas", flat=True).distinct()
        return context

class CreateSuperuserPage(LoginRequiredMixin,CreateView):
    model = User
    form_class=SuperuserCreationForm
    template_name = "admin/pages/superuser-crud/add_superuser.html"
    success_url = reverse_lazy("superuser")

class UpdateSuperuserPage(LoginRequiredMixin,UpdateView):
    model = User
    form_class=SuperuserUpdateForm
    template_name = "admin/pages/superuser-crud/update_account.html"
    success_url = reverse_lazy("superuser")  

class DeleteSuperuser(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("superuser")

    def get(self, request,*args, **kwargs):
        return self.post(request, *args, **kwargs)

class CreateStudentPage(LoginRequiredMixin, CreateView):
    model = Siswa
    fields= ["uid", "nama", "kelas", "jurusan"]
    template_name = "admin/pages/student-crud/add_student.html"
    success_url = reverse_lazy("student")

class UpdateStudentPage(LoginRequiredMixin, UpdateView):
    model = Siswa 
    fields = ["uid", "nama", "kelas", "jurusan"]
    template_name = "admin/pages/student-crud/update_student.html"
    success_url = reverse_lazy("student")

class DeleteStudent(LoginRequiredMixin, DeleteView):
    model = Siswa
    success_url = reverse_lazy("student")

    def get(self, request,*args, **kwargs):
        return self.post(request, *args, **kwargs)