import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings') # የፕሮጀክትህን ስም ተካ
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@gmail.com", "YourNewPassword123")
    print("Admin ተፈጥሯል!")