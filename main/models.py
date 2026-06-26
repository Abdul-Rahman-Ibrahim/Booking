# pyrefly: ignore [missing-import]
from django.db import models
# pyrefly: ignore [missing-import]
from django.contrib.auth.models import User
# pyrefly: ignore [missing-import]
from django.utils.text import slugify
from datetime import timedelta


class Equipment(models.Model):

    name        = models.CharField(max_length=255)
    slug        = models.SlugField(max_length=255, unique=True, blank=True)
    location    = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    capabilities = models.TextField(blank=True)

    image     = models.ImageField(upload_to='equipment/images/', blank=True, null=True)
    documents = models.FileField(upload_to='equipment/documents/', blank=True, null=True)

    is_available = models.BooleanField(default=True)

    min_booking_time = models.DurationField(default=timedelta(minutes=30))
    max_booking_time = models.DurationField(blank=True, null=True)
    gap_after_booking = models.DurationField(blank=True, null=True)
    book_ahead_limit  = models.DurationField(blank=True, null=True)

    COLOR_CHOICES = [
        ('purple', 'Purple'),
        ('teal',   'Teal'),
        ('blue',   'Blue'),
        ('pink',   'Pink'),
        ('tan',    'Tan'),
        ('peach',  'Peach'),
        ('green',  'Green'),
        ('rose',   'Rose'),
    ]
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='blue')

    followers = models.ManyToManyField(
        User,
        related_name='followed_equipment',
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        # Auto-generate slug from name if not set
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Booking(models.Model):

    STATUS_UPCOMING   = 'upcoming'
    STATUS_PAST       = 'past'
    STATUS_CANCELLED  = 'cancelled'
    STATUS_CHOICES = [
        (STATUS_UPCOMING,  'Upcoming'),
        (STATUS_PAST,      'Past'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    user      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='bookings')
    start_time = models.DateTimeField()
    end_time   = models.DateTimeField()
    status     = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_UPCOMING)
    notes      = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['start_time']

    def __str__(self):
        return f"{self.user} booked {self.equipment} from {self.start_time} to {self.end_time}"