

from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse

from django.utils.encoding import force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import auth

from .utils import token_generator
from django.utils.encoding import force_str, force_bytes, DjangoUnicodeDecodeError

import json



def verification(self, request, uuid, token):
    try:
        id = force_str(urlsafe_base64_decode(uuid))
        user = User.objects.get(pk=id)

        if not user.is_active:
            user.is_active = True
            user.save()

        messages.success(request, 'Account activated successfully')
        return redirect('login')

    except Exception as ex:
        pass

    return redirect('login')



# Create your views here.

def index(request):
    return render(request, 'index.html')

# def login(request):
#     return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print("email", email)
        print("password", password)

        if email and password:
            username = User.objects.filter(email=email).first().username
            user = auth.authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Successfully login')
                    return redirect('leaderboard')
                else:
                    messages.error(request, 'User is not active')
            else:
                messages.error(request, 'Invalid credentials!!!')
        else:
            messages.error(request, 'Provide credentials!!!')

        return render(request, 'login.html')
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        context = {
            'fieldValues': request.POST
        }

        if len(username) == 0:
            messages.error(request, "Please enter Username")
            return render(request, 'login.html', status=400, context=context)
        elif len(email) == 0:
            messages.error(request, "Please enter Email")
            return render(request, 'login.html', status=400, context=context)
        elif len(password) == 0:
            messages.error(request, "Password too short")
            return render(request, 'login.html', status=400, context=context)

        if not User.objects.filter(email=email).exists():
            if not User.objects.filter(email=email).exists():
                user = User.objects.create_user(email=email, username=username, first_name=first_name,
                                                last_name=last_name)
                user.set_password(password)
                user.is_active = True
                user.save()
                messages.success(request, "Account successfully created")

                # domain = get_current_site(request).domain
                #
                # uuid = urlsafe_base64_encode(force_bytes(user.pk))
                #
                # link = reverse('activate', kwargs={'uuid': uuid, 'token': token_generator.make_token(user)})
                #
                # activate_url = 'http://' + domain + link
                #
                # mail_subject = 'Activate your account'
                # mail_body = 'Hi ' + user.username + ' Please use this link to activate your account \n' \
                #             + activate_url
                #
                # print("activate_url", activate_url)
                # mail_from = 'mf591108@gmail.com'
                # mail_to = email
                # send_mail(
                #     mail_subject,
                #     mail_body,
                #     mail_from,
                #     [mail_to],
                #     fail_silently=False,
                # )
                return render(request, 'login.html', status=200)
        else:
            messages.error(request, "Email already exist.")
            return render(request, 'login.html', status=200)

        return render(request, 'login.html')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Successfully logout')
    return redirect('login')
