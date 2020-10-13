from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View

from django.http import JsonResponse

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User

from .forms import UserRegisterForm, ImageUploadForm, UserLoginForm
from .decorators import unauthenticated_user

from .models import Profile


@method_decorator(unauthenticated_user, name='dispatch')
class IndexView(View):

    template_name = 'todofront/home.html'

    def get_context_data(self, **kwargs):

        if 'register_form' not in kwargs:
            kwargs['register_form'] = UserRegisterForm()
            kwargs['login_form'] = UserLoginForm()

        return kwargs

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, self.get_context_data())


    def post(self, request, *args, **kwargs):

        if 'login_submit' in request.POST:
            form = UserLoginForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request,'username or password is incorrect')
                return redirect('index')

        elif 'register_submit' in request.POST:
            reg_form = UserRegisterForm(request.POST)

            if User.objects.filter(username=request.POST.get('username')).exists():
                    messages.info(request, "Username already exist")
                    return redirect('index')
            
            if User.objects.filter(email=request.POST.get('email')).exists():
                    messages.info(request, "Email already exist")
                    return redirect('index')

            if reg_form.is_valid():

                username = reg_form.cleaned_data.get("username")

                # group = Group.objects.get(name='user')
                # user.groups.add(group)

                user = reg_form.save()

                Profile.objects.create(user=user)

                messages.success(request, username + ' created successfully!')

                return redirect('index')

            else:
                err_msg = ""

                for msg in reg_form.error_messages:
                    err_msg += reg_form.error_messages[msg] + "\n"

                messages.info(request, err_msg)
                print(err_msg)
                return redirect('index')

@login_required(login_url='index')
def createTask(request):

    if request.method == 'POST':

        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            profile = request.user.profile
            profile.profile_pic = form.cleaned_data['image']
            profile.save()

            return redirect('home')

    context = {}

    return render(request, 'todofront/create_task.html')