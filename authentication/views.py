from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
# from .utils import account_activation_token
from django.urls import reverse
from django.contrib import auth


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Недопустимые значения в имени'}, status=400)
        return JsonResponse({'username_valid': True})

class UsersurnameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        usersurname = data['usersurname']
        if not str(usersurname).isalnum():
            return JsonResponse({'usersurname_error': 'Недопустимые значения в фамилии'}, status=400)
        return JsonResponse({'usersurname_valid': True})

class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Проверьте написание Email'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Почта привязана к другому аккаутну'}, status=409)
        return JsonResponse({'email_valid': True})

class RegistrationView(View):
	def get(self, request):
		return render(request, 'authentication/register.html')

	def post(self, request):

		username = request.POST['username']
		#usersurname = request.POST['usersurname']
		email = request.POST['email']
		password = request.POST['password']

		context = {
			'fieldValues': request.POST
		}

		if not User.objects.filter(username=username).exists():
		# if not User.objects.filter(Q(username=username) | Q(usersurname=usersurname)).exists():
			if not User.objects.filter(email=email).exists():

				if len(password) < 6:
					messages.error(request, 'Пароль слишком короткий')
					return render(request, 'authentication/register.html', context)

				user = User.objects.create_user(username=username, email=email)
				user.set_password(password)
				user.is_active = False
				user.save()
		# 				current_site = get_current_site(request)
		# 				email_body = {
		# 						'user': user,
		# 						'domain': current_site.domain,
		# 						'uid': urlsafe_base64_encode(force_bytes(user.pk)),
		# 						'token': account_activation_token.make_token(user),
		# 				}

		# 				link = reverse('activate', kwargs={
		# 												'uidb64': email_body['uid'], 'token': email_body['token']})

		# 		email_subject = 'Активируйте свой аккаунт'

		# # 				activate_url = 'http://'+current_site.domain+link

		# 		email = EmailMessage(
		# 			email_subject,
		# 			'Здравствуйте, '+user.username + '. Пожалуйста, активируйте свою учетную запись \n',
		# 			'noreply@semycolon.com',
		#  			[email],
		# 		)
		# 		email.send(fail_silently=False)
		# 		messages.success(request, 'Аккаунт успешно создан')
		# 		return render(request, 'authentication/register.html')
				messages.success(request, 'Аккаунт успешно создан')
				return render(request, 'authentication/login.html')


class LoginView(View):
	def get(self, request):
		return render(request, 'authentication/login.html')

		def post(self, request):
			email = request.POST['email']
			password = request.POST['password']

			if email and password:
				user = authentication(email=email, password=password)

				if user:
					# if user.is_active:
						auth.login(request, user)
						messages.success(request, 'Добро пожаловать, ' + user.username)
					
					# messages.error(request, 'Аккаунт не активен. Пожалуйста, проверьте свою почту')
					# return render(request, 'authentication/login.html')
				messages.error(request, 'Пожалуйста, попробуйте снова')
				return render(request, 'authentication/login.html')
			messages.error(request, 'Пожалуйста, заполните все поля')
			return render(request, 'authentication/login.html')