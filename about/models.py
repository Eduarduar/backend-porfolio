from django.db import models
from porfolio.models import Usuario
from django.core.validators import MaxLengthValidator, RegexValidator
from django.utils.translation import gettext_lazy as _


class About(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        db_column="abIDUs",
        error_messages={
            "unique": _("This user already has an entry in About."),
            "null": _("The user field cannot be empty."),
            "invalid": _("Invalid user."),
        },
    )
    ab_desc = models.TextField(
        max_length=1500,
        null=True,
        blank=True,
        verbose_name=_("Description"),
        help_text=_("User description."),
        error_messages={
            "null": _("The description cannot be empty."),
        },
    )

    ab_hero = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Hero"),
        help_text=_("User's hero."),
        error_messages={
            "null": _("The hero cannot be empty."),
        },
    )

    ab_wk_status = models.BooleanField(
        default=True,
        verbose_name=_("Work status"),
        help_text=_("User's work status."),
        error_messages={
            "null": _("The work status cannot be empty."),
        },
    )

    class Meta:
        db_table = "ABOUT"
        verbose_name = _("About")
        verbose_name_plural = _("About")
