from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from .models import TUser
from .forms import RegisterForm, ProfileUpdateForm, TutorRegistration, TutorUserSignUpForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required


class TutorRegisterView(CreateView):
    model = TUser
    form_class = TutorUserSignUpForm
    template_name = 'FindTutors/tutor_signup.html'  # correct form HTML

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_tutor = True
        user.save()
        return redirect('/home/tutors/')  # Go back to the table of tutors


class TuteeRegisterView(CreateView):
    model = TUser
    fields = ['firstname', 'lastname', 'email', 'subjects', 'year', ]
    template_name = 'FindTutors/tutee_signup.html'  # correct form HTML

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_tutee = True
        user.save()
        return redirect('/home/tutees/')  # Go back to the table of tutors
        login(self.request, user)

        return redirect('dashboard')           # redirect to proper dashboard


def Tutors(request):
    model = TUser
    the_tutors = TUser.objects.filter(is_tutor=True)
    return render(request, 'FindTutors/tutors.html', {'tutors': the_tutors})


def Tutees(request):
    all_tutees = TUser.objects.filter(is_tutee=True)

    return render(request, 'FindTutors/tutees.html', {'tutees': all_tutees})


# registration views
class SignUpView(generic.TemplateView):
    template_name = 'registration/signup.html'


class redirectView(generic.TemplateView):
    template_name = 'registration/redirect.html'


class HomeView(generic.TemplateView):
    template_name = 'FindTutors/home.html'


def TutorRequest(request):
    model = TUser
    all_tutors = TUser.objects.filter(is_tutor=True)
    if request.user.is_authenticated:
        print('pie')
    return render(request, 'FindTutors/tutor_request.html', {'tutors': all_tutors})


class ProfileView(generic.TemplateView):
    template_name = 'FindTutors/myprofile.html'


class TutorSignUpView(generic.TemplateView):
    template_name = 'FindTutors/myprofile.html'


@login_required
def editprofile(request):
    if request.method == 'POST':
        print("--- request ----")
        print(request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('FindTutors:profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }

    return render(request, 'FindTutors/editprofile.html', context)
