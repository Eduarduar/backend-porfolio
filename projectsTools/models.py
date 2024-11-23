from django.db import models
from tools.models import Tool
from projects.models import Project
from django.utils.translation import gettext_lazy as _


class ProjectTool(models.Model):
    tool = models.ForeignKey(
        Tool,
        on_delete=models.CASCADE,
        db_column="ptIDTl",
        verbose_name=_("Tool"),
        help_text=_("Tool used in the project."),
        error_messages={
            "invalid": _("The selected tool is not valid."),
            "null": _("This field cannot be empty."),
            "blank": _("This field cannot be blank."),
        },
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        db_column="ptIDPro",
        verbose_name=_("Project"),
        help_text=_("Project to which the tool belongs."),
        error_messages={
            "invalid": _("The selected project is not valid."),
            "null": _("This field cannot be empty."),
            "blank": _("This field cannot be blank."),
        },
    )

    class Meta:
        db_table = "PROJECT_TOOLS"
        verbose_name = _("Project Tool")
        verbose_name_plural = _("Project Tools")
        unique_together = (("tool", "project"),)
