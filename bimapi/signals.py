from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
from .models import Policy, Reminder

@receiver(post_save, sender=Policy)
def create_policy_reminder(sender, instance,created, **kwargs):
    if created:
        # Calculate the reminder date as five days before the policy's end date
        reminder_date = instance.end_date - timedelta(days=5)
        
        # Create a reminder object for the new policy
        Reminder.objects.create(
            policy=instance,
            reminder_date=reminder_date,
            message=f"Renew policy for {instance.client}",
            client=instance.client 
        )
