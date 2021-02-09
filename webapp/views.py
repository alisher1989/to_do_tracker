from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from webapp.forms import TaskForm, CategoryForm
from webapp.models import Task, Category


class ToDoListView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'tasks'
    model = Task
    # ordering = ['-created_at']
    # paginate_by = 4
    # paginate_orphans = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Task.objects.filter(assigned_to=self.request.user, complete=False)
        return queryset


class DetailTaskView(DetailView):
    template_name = 'detail.html'
    context_object_name = 'task'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['parent_tasks'] = Task.objects.filter(parent_task=self.get_object())
        return context


class CompletedTasksView(LoginRequiredMixin, ListView):
    template_name = 'completed_tasks.html'
    context_object_name = 'tasks'
    model = Task

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Task.objects.filter(assigned_to=self.request.user, complete=True)
        return queryset


class TaskCreateView(View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(assigned_to=self.request.user)
        category_count = Category.objects.filter(assigned_to=self.request.user)
        print(category_count)
        context = {'form': TaskForm, 'task': tasks, 'category_count': category_count}
        return render(request, 'create.html', context)

    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_parent')
        category_id = request.POST.get('category')
        if task_id and category_id:
            task = Task.objects.get(pk=int(task_id))
            category = Category.objects.get(pk=int(category_id))
        else:
            task = None
            category = None
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(
                assigned_to=request.user,
                title=form.cleaned_data['title'],
                category=category,
                parent_task=task
            )

            return redirect('/')
        tasks = Task.objects.filter(assigned_to=request.user)
        context = {'tasks': tasks, 'form': form}
        return render(request, 'index.html', context)


class CreateCategoryView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.filter(assigned_to=self.request.user)
        context = {'form': CategoryForm, 'categories': categories}
        return render(request, 'category_create.html', context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            Category.objects.create(assigned_to=self.request.user, category=form.cleaned_data['category'])
            form.save()
            return redirect('/')
        # tasks = Task.objects.filter(assigned_to=request.user)
        context = {'form': form}
        return render(request, 'index.html', context)


class TaskDeleteView(DeleteView):
    model = Task
    pk_kwargs_url = 'pk'
    template_name = 'complete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('list')

    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=self.kwargs['pk'])
        task.complete = True
        task.save()
        tasks = Task.objects.filter(assigned_to=self.request.user, complete=False)
        return render(request, 'index.html', context={'tasks': tasks})

    def get_success_url(self):
        return reverse('list')


class TaskReallyDelete(DeleteView):
    model = Task
    pk_kwargs_url = 'pk'
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('list')