from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password=None, **kwargs):
       
        kwargs.setdefault('is_super_admin', True)
        kwargs.setdefault('is_admin', True)

        user = self.create_user(
            org_id =1,
            email=email,
            password=password,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class Customers(AbstractBaseUser):
    org_id = models.PositiveIntegerField()
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_super_admin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile_number']

    class Meta:
        db_table = "Customers"

        


class Logs(models.Model):
    logid = models.BigAutoField(primary_key=True, editable=False)
    transaction_name = models.CharField(max_length=500)
    mode = models.CharField(max_length=100)
    log_message = models.TextField()
    user = models.ForeignKey(
        "Customers", 
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="log_Customer_id",
    )
    is_app = models.BooleanField(default=False)
    log_date = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "Logs"

        def __str__(self):
            return self.transaction_name