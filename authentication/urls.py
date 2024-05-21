from .views import RegistrationView, UsernameValidationView, UsersurnameValidationView, LoginView, EmailValidationView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


urlpatterns =[
	path('register', RegistrationView.as_view(), name="register"),
	path('login', LoginView.as_view(), name="login"),
  # path('logout', LogoutView.as_view(), name="logout"),
	path('validate-username', csrf_exempt(UsernameValidationView.as_view()),
         name="validate-username"),
	path('validate-usersurname', csrf_exempt(UsersurnameValidationView.as_view()),
         name="validate-usersurname"),
	 path('validate-email', csrf_exempt(EmailValidationView.as_view()),
         name='validate_email'),
	
]