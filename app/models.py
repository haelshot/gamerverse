import uuid
from ninja_jwt.tokens import RefreshToken
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)

        username = email
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    ROLE_CHOICES = [
        ("creator", "creator"),
        ("business", "business"),
        ("user", "user"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.TextField(blank=True, null=True)
    first_name = models.TextField(null=False)
    last_name = models.TextField(null=False)
    phone_number = models.TextField(null=True)
    email = models.EmailField(unique=True, null=False)
    role = models.TextField(choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey("Creator", null=True, on_delete=models.PROTECT) # Todo: create a model for creator and a seller
    business = models.ForeignKey("Business", null=True, on_delete=models.PROTECT)
    is_email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

    class Meta:
        ordering = ["-created_at"]


class Creator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name


class UserCreator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("User", on_delete=models.PROTECT)
    creator = models.ForeignKey(Creator, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.creator.name} - {self.user.first_name} - {self.user.last_name}"


class Business(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.TextField()

    def __str__(self):
        return self.name


class UserBusiness(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("User", on_delete=models.PROTECT)
    business = models.ForeignKey("Business", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.business.name}-{self.user.first_name} {self.user.last_name}"


class RefreshTokenStorage(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    token = models.TextField(null=True)


class UserVerificationToken(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, related_name="users_tokens", on_delete=models.PROTECT
    )
    token = models.TextField(null=False)


class WagerBids(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    wager_bidder = models.ForeignKey(User, on_delete=models.PROTECT)
    wager_accepter = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    wager_amount = models.DecimalField()
    is_accepted = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)


