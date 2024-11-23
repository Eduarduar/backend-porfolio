from django.db import models
from porfolio.models import Usuario
from django.core.validators import MaxLengthValidator, RegexValidator
from django.utils.translation import gettext_lazy as _


class Social(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column="scIDUs",
        verbose_name=_("User"),
        help_text=_("User to whom the social network belongs."),
        error_messages={
            "invalid": _("Invalid user."),
            "null": _("The User field cannot be empty."),
            "blank": _("The User field cannot be blank."),
        },
    )
    sc_name = models.CharField(
        max_length=250,
        unique=True,
        verbose_name=_("Social Network Name"),
        validators=[
            MaxLengthValidator(250),
            RegexValidator(
                r"^[a-zA-Z0-9().-]*$",
                _(
                    "Only letters, numbers, parentheses, hyphens, and periods are allowed"
                ),
            ),
        ],
        help_text=_("Name of the social network."),
        error_messages={
            "null": _("The Social Network Name field cannot be empty."),
            "blank": _("The Social Network Name field cannot be blank."),
        },
    )
    sc_link = models.CharField(
        max_length=250,
        unique=True,
        verbose_name=_("Social Network Link"),
        validators=[
            MaxLengthValidator(250, message=_("URL too long")),
            RegexValidator(r"^\S+$", message=_("Spaces are not allowed")),
        ],
        help_text=_("Link to the social network."),
        error_messages={
            "null": _("The Social Network Link field cannot be empty."),
            "blank": _("The Social Network Link field cannot be blank."),
        },
    )
    sc_status = models.BooleanField(
        default=True,
        verbose_name=_("Status"),
        help_text=_("Status of the social network."),
        error_messages={
            "null": _("The Status field cannot be empty."),
            "blank": _("The Status field cannot be blank."),
        },
    )

    class Meta:
        db_table = "SOCIAL"
        verbose_name = _("Social")
        verbose_name_plural = _("Socials")
