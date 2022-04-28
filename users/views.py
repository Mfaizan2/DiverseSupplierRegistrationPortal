
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
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





# def upload():
#     from azure.storage.blob import (
#         BlobServiceClient,
#         # ContainerPermissions,
#         # BlobPermissions,
#         PublicAccess,
#         ContainerClient,
#     )
#     container_client = ContainerClient.from_connection_string("BlobEndpoint=https://webappmuh.blob.core.windows.net/;QueueEndpoint=https://webappmuh.queue.core.windows.net/;FileEndpoint=https://webappmuh.file.core.windows.net/;TableEndpoint=https://webappmuh.table.core.windows.net/;SharedAccessSignature=sv=2020-08-04&ss=bfqt&srt=co&sp=rwdlacupx&se=2022-04-20T16:00:12Z&st=2022-04-20T08:00:12Z&spr=https&sig=0zI517%2F7DEGqoXN4iKmeZIHuhSDaj7cfOA3PCFoSWn4%3D","temp")
# 
#     print("Uploading files")
# 
#     blob_client = container_client.get_blob_client("salman.pdf")
#     with open("/Users/techesthete009/Downloads/salman.pdf", "rb") as data:
#         blob_client.upload_blob(data)
#         print("africa uploaded to blob")
# 
# 
#     from datetime import datetime, timedelta
#     from azure.storage.blob import BlobClient, generate_blob_sas, BlobSasPermissions
# 
#     account_name = 'webappmuh'
#     account_key = 'Ob9SQssWcPW8hAb6GEOu2xaCHiMv1Q5BV5fdHPoioUW8hktZIQIyTOjvx5gOmv7GYCSy6e9cN+RW+AStbBskSA=='
#     container_name = 'temp'
#     blob_name = 'salman.pdf'
# 
#     sas_blob = generate_blob_sas(account_name=account_name,
#                                  container_name=container_name,
#                                  blob_name=blob_name,
#                                  account_key=account_key,
#                                  permission=BlobSasPermissions(read=True),
#                                  expiry=datetime.utcnow() + timedelta(hours=1)
#                                  )
# 
#     url = 'https://'+account_name+'.blob.core.windows.net/'+container_name+'/'+blob_name+'?'+sas_blob
#     print("url", url)








# Create your views here.

def index(request):

    # upload()
    return render(request, 'index.html')

def upload_file_to_directory():
    try:

        file_system_client = service_client.get_file_system_client(file_system="my-file-system")

        directory_client = file_system_client.get_directory_client("my-directory")

        file_client = directory_client.create_file("africa.jpeg")
        local_file = open("/Users/techesthete009/PycharmProjects/DiverseSupplierRegistrationPortal/static/imgs/africa.jpeg",'r')

        file_contents = local_file.read()

        file_client.append_data(data=file_contents, offset=0, length=len(file_contents))

        file_client.flush_data(len(file_contents))

    except Exception as e:
        print(e)



# def login(request):
#     return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print("email", email)
        print("password", password)

        if email and password:
            userObj = User.objects.filter(email=email).first()
            if userObj:
                user = auth.authenticate(username=userObj.username, password=password)
                if user:
                    if user.is_active:
                        auth.login(request, user)
                        messages.success(request, 'Successfully login')
                        return JsonResponse({'data': "Successfully login.",'status':200})
                    else:
                        messages.error(request, 'User is not active')
                        return JsonResponse({'data': "User is not active.",'status':400})
                else:
                    print("In valid")
                    messages.error(request, 'Invalid credentials!!!')
                    return JsonResponse({'data': "Invalid credentials.",'status':400})
            else:
                return JsonResponse({'data': "User not found.",'status':400})

        else:
            messages.error(request, 'Provide credentials!!!')
            return JsonResponse({'data': "Provide credentials.",'status':400})

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        # context = {
        #     'fieldValues': request.POST
        # }
        #
        # if len(first_name) == 0:
        #     messages.error(request, "Please enter First Name")
        #     return render(request, 'login.html', status=400, context=context)
        # elif len(email) == 0:
        #     messages.error(request, "Please enter Email")
        #     return render(request, 'login.html', status=400, context=context)
        # elif len(password) < 4:
        #     messages.error(request, "Password too short")
        #     return JsonResponse({'data': "Password too short.",'status':200})
        #     return render(request, 'login.html', status=400, context=context)

        if not User.objects.filter(email=email).exists():
            user = User.objects.create_user(email=email, username=email.split('@')[0], first_name=first_name,
                                            last_name=last_name)
            user.set_password(password)
            user.is_active = True
            user.save()


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
            return JsonResponse({'data': "Account Successfully created.",'status':200})
        else:
            return JsonResponse({'data': "Email already exist.",'status':500})


    return render(request, 'login.html', status=400)


@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Successfully logout')
    return redirect('login')
