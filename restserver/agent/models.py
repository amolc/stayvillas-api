
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid
from datetime import timedelta
from django.utils.timezone import now
class AgentManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('is_super_admin', True)
        kwargs.setdefault('is_admin', True)

        user = self.create_user(
            agency_id=1,
            email=email,
            password=password,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class Agent(AbstractBaseUser):
    org_id = models.PositiveIntegerField()
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    city = models.CharField(max_length=200)
    total_sales = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_super_admin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=True)

    reset_password_token = models.UUIDField(null=True, blank=True)
    reset_password_expiration = models.DateTimeField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)

    objects = AgentManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']
    class Meta:
        db_table = "Agents"
    def generate_reset_token(self):
        """Generate a password reset token and set its expiration."""
        self.reset_password_token = uuid.uuid4()
        self.reset_password_expiration = now() + timedelta(hours=1)  # 1-hour expiration
        self.save(update_fields=['reset_password_token', 'reset_password_expiration'])

class AgentLogs(models.Model):
    logid = models.BigAutoField(primary_key=True, editable=False)
    transaction_name = models.CharField(max_length=500)
    mode = models.CharField(max_length=100)
    log_message = models.TextField()
    agent = models.ForeignKey(
        "Agent", 
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="log_agent_id",
    )
    is_app = models.BooleanField(default=False)
    log_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "AgentLogs"

    def __str__(self):
        return self.transaction_name
