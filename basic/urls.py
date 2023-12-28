from django.urls import path
from allauth.account import views as auth
from . import views

app_name = 'basic'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('new/lecturer/signup/', views.LecturerCreateView.as_view(), name='lecturer_signup'),
    path('new/student/signup/', views.StudentCreateView.as_view(), name='student_signup'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('signin/', auth.login, name='login'),
    # path('elearn/signin/', LoginView.as_view(template_name="basic/login.html"), name='login'),
    path('signout/', auth.logout, name='logout'),
]