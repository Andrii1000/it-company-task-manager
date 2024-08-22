from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import (
    TaskType,
    Position,
    Worker,
    Task
)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "priority",
        "deadline",
        "task_type",
        "is_completed"
    )
    search_fields = ("name",)
    list_filter = ("is_completed", "task_type", "priority",)


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("position",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                    )
                },
            ),
        )
    )


admin.site.register(TaskType)
admin.site.register(Position)
