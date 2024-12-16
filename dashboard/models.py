from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class User(AbstractUser):
    ROLE_CHOICES = [
        ('superuser', 'Super User'),
        ('admin', 'Admin'),
        ('agent', 'Agent'),
        ('validator', 'Validator'),
        ('account', 'Account'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def is_admin(self):
        return self.role == 'admin'

    def is_custom_superuser(self):
        return self.role == 'superuser'

class Company(models.Model):
    name = models.CharField(max_length=255)
    bonus_formula = models.TextField()

class Form(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    agent = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='forms',
        limit_choices_to={'role': 'agent'}
    )
    validator = models.ForeignKey(
        'User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_forms',
        limit_choices_to={'role': 'validator'}
    )
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE
    )
    future_draft_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    rejection_reason = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Form #{self.id} by {self.agent.username} for {self.company.name}"

    def clean(self):
        """Custom validation logic."""
        if self.status == 'rejected' and not self.rejection_reason:
            raise ValidationError("Rejection reason is required when rejecting a form.")

        if self.validator and self.status != 'pending':
            raise ValidationError("Only pending forms can be assigned to a validator.")




class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
