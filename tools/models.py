from django.db import models
from django.core.validators import MaxLengthValidator, RegexValidator
from django.utils.translation import gettext_lazy as _


class Tool(models.Model):
    id_tl = models.AutoField(primary_key=True)
    tl_name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name=_("Tool name"),
        validators=[
            MaxLengthValidator(50, message=_("Name too long")),
            RegexValidator(
                r"^[a-zA-Z0-9.-]*$",
                _("Only letters, numbers, hyphens, and periods are allowed"),
            ),
        ],
        help_text=_("Tool name."),
        null=False,
        blank=False,
        error_messages={
            "null": _("This field cannot be null."),
            "blank": _("This field cannot be blank."),
        },
    )
    tl_tool = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Tool link"),
        validators=[
            MaxLengthValidator(255, message=_("URL too long")),
            RegexValidator(r"^\S+$", _("No spaces allowed")),
        ],
        help_text=_("Tool link."),
        null=False,
        blank=False,
        error_messages={
            "null": _("This field cannot be null."),
            "blank": _("This field cannot be blank."),
        },
    )

    class Meta:
        db_table = "TOOLS"
        verbose_name = _("Tool")
        verbose_name_plural = _("Tools")
