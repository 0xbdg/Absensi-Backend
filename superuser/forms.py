from django import forms
from django.forms.widgets import *
from django.contrib.auth.forms import *
from absensi.models import *

class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=TextInput(attrs={"class":"bg-white shadow-sm ring-0 block w-full text-lg focus:outline-none focus:border-tan-500 border-tan-300 p-2 border-2"}))
    password = forms.CharField(required=True, widget=PasswordInput(attrs={"class":"bg-white shadow-sm ring-0 block w-full text-lg focus:outline-none focus:border-tan-500 border-tan-300 p-2 border-2"}))

class StudentForm(forms.ModelForm):
    uid = forms.CharField(widget=TextInput(attrs={"class":"w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"}))
    nama = forms.CharField(widget=TextInput(attrs={"class":"w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"}))
    kelas = forms.ChoiceField(choices=Siswa.KELAS,widget=Select(attrs={"class":"w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"}))
    jurusan = forms.ChoiceField(choices=Siswa.JURUSAN,widget=Select(attrs={"class":"w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"}))

    class Meta:
        model = Siswa
        fields = ["uid", "nama", "kelas" ,"jurusan"]

class SuperuserCreationForm(forms.ModelForm):
    username = forms.CharField(widget=TextInput(attrs={"class":"w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"}))
    email = forms.EmailField(widget=EmailInput(attrs={"class":"w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"}))
    password = forms.CharField(widget=PasswordInput(attrs={"class":"w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super(SuperuserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
        return user
    
class SuperuserUpdateForm(UserChangeForm):
    username = forms.CharField(widget=TextInput(attrs={"class":"w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"}))
    email = forms.EmailField(widget=EmailInput(attrs={"class":"w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"}))
    password1 = forms.CharField(widget=PasswordInput(attrs={"class":"w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"}),label='New Password')
    password2 = forms.CharField(widget=PasswordInput(attrs={"class":"w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"}),label='Confirm Password')
    class Meta:
        model = User
        fields = ['username', 'email',"password"]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match.")