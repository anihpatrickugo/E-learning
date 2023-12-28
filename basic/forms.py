from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser, StudentUser

class LecturerSignUpForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','email', 'password1', 'password2']
    def save(self, commit=True):
        user =super().save(commit=False)
        user.is_lecturer = True
        user.save()
        
        return user 
    
    

class StudentSignUpForm(UserCreationForm):
    registration_number = forms.IntegerField(required=True)


    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','email', 'password1', 'password2', 'registration_number']
    
    def save(self):
        
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        
        student = StudentUser.objects.create(user=user, registration_number=self.cleaned_data['registration_number'])
        return user


    





        