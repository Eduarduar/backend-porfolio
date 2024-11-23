from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import RegexValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _


class UsuarioManager(BaseUserManager):
    def create_user(self, us_email, password=None, **extra_fields):
        if not us_email:
            raise ValueError(_("Email is required"))
        us_email = self.normalize_email(us_email)
        user = self.model(us_email=us_email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, us_email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError(_("Superuser must have is_staff=True."))
        if not extra_fields.get("is_superuser"):
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(us_email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(
        primary_key=True, verbose_name=_("ID"), help_text=_("User ID.")
    )

    us_fr_name = models.CharField(
        max_length=30,
        verbose_name=_("First Name"),
        validators=[
            RegexValidator(
                regex=r"^[a-zA-ZáéíóúÁÉÍÓÚ ]+$",
                message=_("First name can only contain letters, accents, and spaces."),
            )
        ],
        help_text=_("User's first name."),
        error_messages={
            "null": _("First name cannot be null."),
            "blank": _("First name cannot be blank."),
        },
    )

    us_ls_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name=_("Last Name"),
        validators=[
            RegexValidator(
                regex=r"^[a-zA-ZáéíóúÁÉÍÓÚ ]+$",
                message=_("Last name can only contain letters, accents, and spaces."),
            )
        ],
        help_text=_("User's last name."),
    )

    us_email = models.EmailField(
        unique=True,
        verbose_name=_("Email"),
        validators=[
            MaxLengthValidator(255, _("Email is too long.")),
            RegexValidator(r"^.+@.+\..+$", _("Invalid email address.")),
        ],
        help_text=_("User's email address."),
        error_messages={
            "null": _("Email cannot be null."),
            "blank": _("Email cannot be blank."),
        },
    )

    us_phone = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_("Phone"),
        validators=[
            RegexValidator(
                regex=r"^\+\d{1,3} \d{1,14}$",
                message=_(
                    "Phone number must be in the format '+[Prefix] [Phone number]."
                ),
            )
        ],
        help_text=_("User's phone number."),
        error_messages={
            "null": _("Phone number cannot be null."),
            "blank": _("Phone number cannot be blank."),
        },
    )

    us_br_date = models.DateField(
        verbose_name=_("Birth Date"),
        validators=[
            RegexValidator(
                regex=r"^\d{4}-\d{2}-\d{2}$",
                message=_("Birth date must be in the format 'YYYY-MM-DD'."),
            )
        ],
        help_text=_("User's birth date."),
        error_messages={
            "null": _("Birth date cannot be null."),
            "blank": _("Birth date cannot be blank."),
        },
    )
    us_photo = models.CharField(
        max_length=255,
        default="static/users/placeholder.jpg",
        null=True,
        blank=True,
        verbose_name=_("Profile Photo"),
        validators=[MaxLengthValidator(255, _("Photo URL is too long."))],
        help_text=_("URL of the user's profile photo."),
    )
    us_cr_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Creation Date"),
        validators=[
            RegexValidator(
                regex=r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$",
                message=_("Invalid date and time format. Use YYYY-MM-DD HH:MM:SS"),
            )
        ],
        help_text=_("User's creation date and time."),
    )
    us_up_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Update Date"),
        validators=[
            RegexValidator(
                regex=r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$",
                message=_("Invalid date and time format. Use YYYY-MM-DD HH:MM:SS"),
            )
        ],
        help_text=_("User's last update date and time."),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active"),
        help_text=_("Indicates if the user is active."),
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_("Staff"),
        help_text=_("Indicates if the user is a staff member."),
    )

    objects = UsuarioManager()

    USERNAME_FIELD = "us_email"
    REQUIRED_FIELDS = ["us_fr_name", "us_phone", "us_br_date"]

    class Meta:
        db_table = "USUARIOS"
        verbose_name = _("User")
        verbose_name_plural = _("Users")
