from django.core.management.base import BaseCommand
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from core.tasks import update_silo_resources


class Command(BaseCommand):
    help = "Add update_silo_resources task to Celery Beat"

    def handle(self, *args, **options):
        # Create a 10 seconds interval schedule
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=10, period=IntervalSchedule.SECONDS
        )

        # Add the update_silo_resources task as a periodic task
        PeriodicTask.objects.get_or_create(
            name="Update Silo Resources",
            interval=schedule,
            task="core.tasks.update_silo_resources",
        )

        self.stdout.write(
            self.style.SUCCESS("Successfully added update_silo_resources periodic task")
        )
