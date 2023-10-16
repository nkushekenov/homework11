from django import forms
from .models import Task  # Импортируйте модели, которые вы используете

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'  # или перечислите поля, которые вы хотите включить
