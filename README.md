# CALICO Lab Equipment Booking

A Django-based equipment booking dashboard for managing lab instruments, calendar reservations, and booking-related settings.

## Overview

This project provides a clean booking UI for a lab environment with:

- A calendar view that displays existing bookings
- An equipment directory with availability, locations, and booking rules
- A personal bookings page
- A settings page for profile and notification preferences
- Django models for equipment, bookings, and equipment followers

The current codebase is structured as a front-end heavy booking dashboard backed by Django templates and models.

## Features

- Calendar dashboard powered by FullCalendar assets in `static/js`
- Equipment catalog with images, documents, availability, and booking constraints
- Booking records with status tracking: upcoming, past, cancelled
- Equipment filtering endpoint at `/filter-equipment/`
- Admin-ready Django apps for `main` and `authentication`
- Static file handling configured for WhiteNoise

## Project Structure

- `_booking/` - Django project settings, URLs, ASGI/WSGI configuration
- `main/` - Core booking app with models, views, URLs, and migrations
- `authentication/` - Authentication app scaffold
- `templates/` - Shared and page templates
- `static/` - CSS and JavaScript assets
- `build_files.sh` - Deployment helper script for static files and migrations
- `vercel.json` - Vercel deployment config

## Requirements

The project dependencies are listed in `requirements.txt` and include:

- Django 6.0.6
- `dj-database-url`
- `python-dotenv`
- `whitenoise`
- `gunicorn`
- `psycopg2-binary`
- `pillow`

## Local Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with the required environment variables:

```env
SECRET_KEY=your-secret-key
DEBUG=1
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
```

Note: `DATABASE_URL` is parsed through `dj-database-url`. If you want to use SQLite locally, make sure the value is supported by your installed version of `dj-database-url`.

4. Run migrations:

```bash
python manage.py migrate
```

5. Create a superuser if needed:

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

## Environment Variables

The project expects these variables:

- `SECRET_KEY` - Django secret key
- `DEBUG` - Enables debug mode when set to a non-empty value
- `ALLOWED_HOSTS` - Comma-separated host list
- `DATABASE_URL` - Database connection string

## Database Models

### `Equipment`

Stores lab equipment metadata:

- `name`
- `slug`
- `location`
- `description`
- `capabilities`
- `image`
- `documents`
- `is_available`
- booking rules such as minimum time, maximum time, gap after booking, and how far ahead users can book
- `color`
- followers via a many-to-many relation to Django `User`

### `Booking`

Stores reservations:

- `user`
- `equipment`
- `start_time`
- `end_time`
- `status`
- `notes`

## Available Routes

- `/` - Calendar dashboard
- `/equipment/` - Equipment listing
- `/bookings/` - My bookings page
- `/settings/` - Settings page
- `/filter-equipment/` - Equipment filter POST endpoint
- `/admin/` - Django admin

## Deployment

The repository includes a simple deployment flow:

- `build_files.sh` runs `collectstatic` and `migrate`
- `vercel.json` routes requests to `_booking/wsgi.py`
- WhiteNoise is configured for static file serving

### Vercel

The included `vercel.json` uses Django's WSGI entry point. If deploying to Vercel, make sure the environment variables above are configured in the project settings.

## Notes

- The `authentication` app is currently a scaffold and does not yet expose routes.
- Several pages are currently template-driven and may rely on additional JavaScript for full interactivity.
- The calendar page passes booking data into `window` via a `BOOKINGS` global in the template.
