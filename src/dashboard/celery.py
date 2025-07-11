import os
from celery import Celery

# Define o settings padrão do Django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard.settings.local')

# Cria a aplicação Celery
app = Celery('dashboard')

# Carrega configurações do Django e das tasks dos apps
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')