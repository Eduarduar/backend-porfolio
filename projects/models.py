from django.db import models
from django.core.exceptions import ValidationError
from porfolio.models import Usuario
from django.core.validators import MaxLengthValidator, RegexValidator
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column="proIDUs",
        error_messages={
            "invalid": _("Invalid user."),
            "null": _("The user field cannot be null."),
            "blank": _("The user field cannot be blank."),
        },
    )
    id_pro = models.AutoField(primary_key=True)
    pro_name = models.CharField(
        max_length=100,
        verbose_name=_("Project name"),
        validators=[
            MaxLengthValidator(100, message=_("Name too long")),
            RegexValidator(
                r"^[a-zA-Z0-9.\-() ]*$",
                _(
                    "Only letters, numbers, hyphens, periods, parentheses, and spaces are allowed"
                ),
            ),
        ],
        help_text=_("Project name."),
        error_messages={
            "null": _("The project name field cannot be null."),
        },
    )
    pro_desc = models.TextField(
        max_length=1500,
        verbose_name=_("Description"),
        validators=[MaxLengthValidator(1500, message=_("Description too long"))],
        help_text=_("Project description."),
        error_messages={
            "null": _("The description field cannot be null."),
        },
    )
    pro_img = models.CharField(
        max_length=255,
        verbose_name=_("Image"),
        validators=[
            RegexValidator(regex=r"^\S+$", message=_("No spaces allowed")),
            MaxLengthValidator(255, message=_("URL too long")),
        ],
        help_text=_("Project image."),
        error_messages={
            "null": _("The image field cannot be null."),
        },
    )
    pro_rep = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Repository"),
        validators=[
            RegexValidator(regex=r"^\S+$", message=_("No spaces allowed")),
            MaxLengthValidator(255, message=_("URL too long")),
        ],
        help_text=_("Project repository."),
    )
    pro_link = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Link"),
        validators=[
            MaxLengthValidator(255, message=_("URL too long")),
            RegexValidator(regex=r"^\S+$", message=_("No spaces allowed")),
        ],
        help_text=_("Project link."),
    )
    pined = models.BooleanField(
        default=False,
        verbose_name=_("Pined"),
        help_text=_("Project pined."),
    )
    pro_cr_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Creation Date"),
        help_text=_("Project creation date and time."),
    )
    pro_up_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Update Date"),
        help_text=_("Project last update date and time."),
    )

    def save(self, *args, **kwargs):
        if self.pined:
            pined_count = Project.objects.filter(pined=True).count()
            if pined_count >= 3 and not self.pk:
                raise ValidationError(
                    _("No more than 3 projects can be pined at the same time.")
                )
        super().save(*args, **kwargs)

    class Meta:
        db_table = "PROJECTS"
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
