from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.views.decorators.http import require_POST
# from django.utils.decorators import method_decorator

from .models import Task

# Create your views here.

class LogIn(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    


class LogOut(LogoutView):
    template_name = 'todo/logout.html'
    fields = '__all__'
    


class TaskView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "todo/home.html"
    context_object_name = "tasks"

    # Make suere the user can only get their tasks

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['tasks'] = contex['tasks'].filter(user=self.request.user)
        contex['count'] = contex['tasks'].filter(complete=False).count()
        return contex



class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'todo/task_detail.html'
    context_object_name = 'tasks'

    

class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'todo/form.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super(CreateTask, self).form_valid(form)

class EditTask(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'todo/form.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'todo/delete_task.html'
    success_url = reverse_lazy('tasks')