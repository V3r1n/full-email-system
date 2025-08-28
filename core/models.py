from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.email


class Queue(models.Model):
    name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)
    members = models.ManyToManyField(User, related_name='queues', blank=True)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    STATUS_CHOICES = (
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets')
    queue = models.ForeignKey(Queue, on_delete=models.CASCADE, related_name='tickets')
    submitter_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.title}'
