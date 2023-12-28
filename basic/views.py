from typing import Any
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import StudentSignUpForm, LecturerSignUpForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.



class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'basic/index.html'
    
    

class LecturerCreateView(CreateView):
    form_class = LecturerSignUpForm
    template_name = 'basic/registration.html'
    success_url = reverse_lazy('basic:success')

    def get_context_data(self, **kwargs: Any):
        data = super().get_context_data(**kwargs)
        data['lecturer'] = True
        return data
    


class StudentCreateView(CreateView):
    form_class = StudentSignUpForm
    template_name = 'basic/registration.html'
    success_url = reverse_lazy('basic:success')
    

    def get_context_data(self, **kwargs: Any):
        data = super().get_context_data(**kwargs)
        data['lecturer'] = False
        return data
    

class SuccessView(TemplateView):
    template_name = 'basic/success.html'



def sayConnected(request):
    return HttpResponse('Connected')
