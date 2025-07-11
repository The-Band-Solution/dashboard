from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.db.utils import OperationalError, ProgrammingError
import json

def setup_periodic_tasks():
    try:
        # Cria o intervalo de 30 segundos
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=30,
            period=IntervalSchedule.SECONDS,
        )

        # Cria a tarefa periódica
        PeriodicTask.objects.update_or_create(
            name="Say Hello every 30s",
            defaults={
                "interval": schedule,
                "task": "apps.core.tasks.print_hello",
                "args": json.dumps([]),
            },
        )

    except (OperationalError, ProgrammingError):
        # Ignora erros caso o banco ainda não esteja pronto
        pass

# Executa a configuração quando o app estiver pronto
setup_periodic_tasks()
