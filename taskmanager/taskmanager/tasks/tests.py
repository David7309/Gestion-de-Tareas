from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task

class TaskAPITestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        
    def test_create_task(self):
        self.task1 = Task.objects.create(title="Tarea 1", description="Descripción de la tarea 1", completed=False, user=self.user)
        # Asegúrate de realizar las afirmaciones necesarias para verificar que la tarea se haya creado correctamente
        
    def test_delete_task(self):
        self.task1 = Task.objects.create(title="Tarea 1", description="Descripción de la tarea 1", completed=False, user=self.user)
        # Asegúrate de realizar las afirmaciones necesarias para verificar que la tarea se pueda eliminar correctamente
        
    def test_list_tasks(self):
        self.task1 = Task.objects.create(title="Tarea 1", description="Descripción de la tarea 1", completed=False, user=self.user)
        # Asegúrate de realizar las afirmaciones necesarias para verificar que las tareas se puedan listar correctamente
        
    def test_update_task(self):
        self.task1 = Task.objects.create(title="Tarea 1", description="Descripción de la tarea 1", completed=False, user=self.user)
        # Asegúrate de realizar las afirmaciones necesarias para verificar que la tarea se pueda actualizar correctamente
