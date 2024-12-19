from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from enum import Enum
class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'

    @classmethod
    def choices(cls):
        return [(gender.value, gender.name.capitalize()) for gender in cls]
    
class underwriting_status(Enum):
    DhurbaPokhrel = 'Dhurba Pokhrel'
    SantoshDevkota = 'SantoshDevkota'
    ShoaibAkram = 'ShoaibAkram'
    SureshMahato = 'SureshMahato'

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]

# class InsuranceCompany(Enum):
#     MUTUAL_OF_OMAHA = 'Mutual Of Omaha'
#     AFLAC = 'Aflac'
#     COREBRIDGE_FINANCIAL = 'Corebridge Financial'
#     SBLI = 'SBLI'
#     ROYAL_NEIGHBORS_OF_AMERICA = 'Royal Neighbors Of America'
#     GTL = 'GTL'

#     @classmethod
#     def choices(cls):
#         return [(company.value, company.value) for company in cls]
    
class InsuranceType(Enum):
    Level = 'Level'
    Standard = "Standard"
    Graded = "Graded"
    Modified = "Modified"
    GuaranteedIssue = "GuaranteedIssue"

    @classmethod
    def choices(cls):
        return [(type.name, type.value) for type in cls]

class SmokerType(Enum):
    Smoker = 'Smoker'
    Non_Smoker = 'Non-Smoker'

    @classmethod
    def choices(cls):
        return [(smoker.value, smoker.name.capitalize()) for smoker in cls]
    
class AccountType(Enum):
    CheckingAccount = "CheckingAccount"
    SavingsAccount = "SavingsAccount"
    DirectExpressCard = "DirectExpressCard"

    @classmethod
    def choices(cls):
        return [(account.name, account.value) for account in cls]
    

# class ScheduleOption(Enum):
#     FIRST_OF_MONTH = "1stofeachmonth"
#     THIRD_OF_MONTH = "3rd of each month"
#     SECOND_WEDNESDAY = "2nd Wednesday of each month"
#     THIRD_WEDNESDAY = "3rd Wednesday of each month"
#     FOURTH_WEDNESDAY = "4th Wednesday of each month"

    @classmethod
    def choices(cls):
        return [(schedule.name, schedule.value) for schedule in cls]

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
    bonus_formula = models.TextField(null=True, blank=True)

class Form(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    SCHEDULE_CHOICES = [
    ("1st of each month", "1st of each month"),
    ("3rd of each month", "3rd of each month"),
    ("2nd Wednesday of each month", "2nd Wednesday of each month"), 
    ("3rd Wednesday of each month", "3rd Wednesday of each month"),
    ("4th Wednesday of each month", "4th Wednesday of each month")
    ]
    ROLE_CHOICES = [
    ('Mutual Of Omaha', 'Mutual Of Omaha'),
    ('Aflac', 'Aflac'),
    ('Corebridge Financial', 'Corebridge Financial'),
    ('SBLI', 'SBLI'),
    ('Royal Neighbors Of America', 'Royal Neighbors Of America'),
    ('GTL', 'GTL'),]

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
    birth_state = models.CharField(max_length=26, null=True)
    phone_number = models.CharField(max_length=11)
    name = models.CharField(max_length=26)
    gender = models.CharField(max_length=26, choices=Gender.choices, default=Gender.MALE.value)
    address = models.CharField(max_length=26, null=True)
    city = models.CharField(max_length=26, null=True)
    zip_code = models.CharField(max_length=26, null=True)
    dob = models.DateField(null=True)
    age = models.IntegerField(null=True)
    height = models.CharField(max_length=26, null=True)
    weight = models.CharField(max_length=26, null=True)
    insurance_company = models.CharField(max_length=26, choices=ROLE_CHOICES ,null=True)
    type_of_coverage = models.CharField(max_length=26, choices=InsuranceType.choices, default=InsuranceType.Modified.value, null=True)
    coverage_amount = models.CharField(max_length=26, null=True)
    monthly_premium = models.CharField(max_length=26, null=True)
    social_security_number = models.CharField(max_length=26)
    beneficary = models.CharField(max_length=26, null=True)
    tobacco = models.CharField(max_length=26, choices=SmokerType.choices, default=SmokerType.Smoker.value, null=True)
    health_condition = models.CharField(max_length=26, null=True)
    medication = models.CharField(max_length=26, null=True)
    doctors_name = models.CharField(max_length=26, null=True)
    doctors_address = models.CharField(max_length=26, null=True)
    bank_name = models.CharField(max_length=26, null=True)
    account_type = models.CharField(max_length=26, choices=AccountType.choices, default=AccountType.SavingsAccount.value, null=True)
    routing_number = models.CharField(max_length=26, null=True)
    account_number = models.CharField(max_length=26, null=True)
    initial_draft_date = models.DateField(null=True)
    future_draft_date = models.CharField(max_length=27,choices=SCHEDULE_CHOICES,null=True)
    email = models.CharField(max_length=26)
    comments = models.CharField(max_length=26, null=True)
    # closers_name = models.CharField(max_length=26, null=True)
    policy_number = models.CharField(max_length=26,null=True)
    data_of_submission = models.DateField(null=True)
    drivers_license = models.CharField(max_length=26,null=True)
    under_written_by = models.CharField(max_length=26,choices=underwriting_status.choices, default=underwriting_status.SureshMahato.value, null=True)
    jornaya_lead_id = models.CharField(max_length=26, null=True)
    note = models.TextField(null=True, blank=True) 


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

