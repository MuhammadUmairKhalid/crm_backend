from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('Agent', 'Agent'),
        ('Validator', 'Validator'),
        ('Admin', 'Admin'),
        ('PaymentChecker', 'Payment Checker'),
        ('Retentions', 'Retentions'),
        ('hr','hr')
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    password=models.CharField(max_length=8)

    def clean(self):
        if len(self.password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.role

class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    dob = models.DateField()
    height = models.FloatField()
    weight = models.FloatField()
    income_status = models.CharField(max_length=50, choices=[
        ('Disability', 'Disability'),
        ('Retirement', 'Retirement'),
        ('Employment', 'Employment'),
        ('SelfEmployed', 'Self Employed')
    ])
    smoker = models.BooleanField()


class MedicalInfo(models.Model):
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    medications = models.TextField()


class InsuranceDetail(models.Model):
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)
    carrier = models.CharField(max_length=100, choices=[
        ('AFLAC', 'AFLAC'),
        ('SBLI', 'SBLI'),
        ('RNA', 'RNA'),
        ('Mutual of Omaha', 'Mutual of Omaha'),
        ('CiCa', 'CiCa')
    ])
    plan_type = models.CharField(max_length=50, choices=[
        ('Level', 'Level'),
        ('Graded', 'Graded'),
        ('Modified', 'Modified'),
        ('Guaranteed Issue', 'Guaranteed Issue')
    ])
    coverage = models.DecimalField(max_digits=10, decimal_places=2)
    premium = models.DecimalField(max_digits=10, decimal_places=2)


class ContactDetail(models.Model):
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    state_born = models.CharField(max_length=50)
    email = models.EmailField()

class PaymentInfo(models.Model):
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)
    first_eft = models.DateField()
    eft_schedule = models.CharField(max_length=50, choices=[
        ('1st of the Month', '1st of the Month'),
        ('3rd of the Month', '3rd of the Month'),
        ('2nd Wednesday', '2nd Wednesday'),
        ('3rd Wednesday', '3rd Wednesday'),
        ('4th Wednesday', '4th Wednesday'),
        ('Other', 'Other')
    ])
    ssn = models.CharField(max_length=11)
    beneficiary_name = models.CharField(max_length=100)
    beneficiary_relation = models.CharField(max_length=50, choices=[
        ('Mother', 'Mother'),
        ('Father', 'Father'),
        ('Brother', 'Brother'),
        ('Child', 'Child'),
        ('Grandchild', 'Grandchild'),
        ('Friend', 'Friend'),
        ('State', 'State')
    ])

class BankDetail(models.Model):
    payment_info = models.OneToOneField(PaymentInfo, on_delete=models.CASCADE)
    name_on_account = models.CharField(max_length=100)
    account_type = models.CharField(max_length=20, choices=[
        ('Checking', 'Checking'),
        ('Saving', 'Saving')
    ])
    bank_name = models.CharField(max_length=100)
    routing_number = models.CharField(max_length=9)
    checking_number = models.CharField(max_length=20)
    account_info_source = models.CharField(max_length=50, choices=[
        ('Cheque Book', 'Cheque Book'),
        ('Bank Statement', 'Bank Statement'),
        ('Bank Rep', 'Bank Rep'),
        ('Online Application', 'Online Application')
    ])

class ApplicationStatus(models.Model):
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('Approved', 'Approved'),
        ('Not Approved', 'Not Approved')
    ])
    rejection_reason = models.TextField(blank=True, null=True)
    policy_number = models.CharField(max_length=50, blank=True, null=True)
    submission_status = models.CharField(max_length=20, choices=[
        ('Submitted', 'Submitted'),
        ('Submit Later', 'Submit Later')
    ])

class PaymentStatus(models.Model):
    application_status = models.OneToOneField(ApplicationStatus, on_delete=models.CASCADE)
    commission_status = models.CharField(max_length=20, choices=[
        ('Paid', 'Paid'),
        ('Not Paid', 'Not Paid')
    ])
    payment_issue = models.CharField(max_length=50, blank=True, null=True, choices=[
        ('NSF', 'NSF'),
        ('Invalid Account', 'Invalid Account'),
        ('Closed', 'Closed'),
        ('Frozen', 'Frozen'),
        ('Non-Transactional', 'Non-Transactional'),
        ('Lapsed', 'Lapsed'),
        ('Cancelled', 'Cancelled'),
        ('Declined', 'Declined')
    ])

