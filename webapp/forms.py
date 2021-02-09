from django import forms

from webapp.models import Task, Category


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))

    class Meta:
        model = Task
        fields = ['title']


class CategoryForm(forms.ModelForm):
    category = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new category...'}))

    class Meta:
        model = Category
        fields = ['category']