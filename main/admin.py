# pyrefly: ignore [missing-import]
from django.contrib import admin
from .models import Equipment, Booking


class BookingInline(admin.StackedInline):
    """Nested bookings inside Equipment for admin detail view."""
    model = Booking
    extra = 0
    readonly_fields = ["created_at", "updated_at"]


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "is_available",
        "min_booking_time",
        "max_booking_time",
        "gap_after_booking",
        "book_ahead_limit",
        "color",
        "created_at",
    )
    list_filter = (
        "is_available",
        "color",
        "location",
    )
    search_fields = ("name", "description", "location")
    # Show bookings inside Equipment detail
    inlines = [BookingInline]
    readonly_fields = ["created_at", "updated_at"]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "equipment",
        "start_time",
        "end_time",
        "status",
    )
    list_filter = (
        "status",
        "equipment",
        "user",
        "start_time",
    )
    search_fields = (
        "user__username",
        "user__email",
        "equipment__name",
        "equipment__location",
    )
    date_hierarchy = "start_time"
    readonly_fields = ["created_at", "updated_at"]
