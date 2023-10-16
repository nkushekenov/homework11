from django.urls import path
from . import views  # Убедитесь, что импортируете свои представления здесь

urlpatterns = [
    # Главная страница со списком всех задач
    path('', views.task_list, name='task-list'),  # Здесь будет отображаться список всех задач

    # Страница детализации задачи, где <int:pk> является первичным ключом задачи
    path('task/<int:pk>/', views.task_detail, name='task-detail'),  # Показывает детали отдельной задачи

    # Страницы для создания, обновления и удаления задач
    path('task/create/', views.task_create, name='task-create'),  # Создание новой задачи
    path('task/<int:pk>/update/', views.task_update, name='task-update'),  # Обновление существующей задачи
    path('task/<int:pk>/delete/', views.task_delete, name='task-delete'),  # Удаление задачи
]
