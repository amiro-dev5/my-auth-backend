import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings') # የፕሮጀክትህን settings ስም ተካ
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

ADMIN_EMAIL = "admin@gmail.com"
ADMIN_PASSWORD = "YourStrongPassword123"  # የምታስታውሰውን አዲስ ፓስወርድ እዚህ ጻፍ

if not User.objects.filter(email=ADMIN_EMAIL).exists():
    # Email-based User Model ስለሆነ በ email ይፈጠራል
    User.objects.create_superuser(email=ADMIN_EMAIL, password=ADMIN_PASSWORD)
    print(f"Superuser with email '{ADMIN_EMAIL}' created successfully!")
else:
    # ቀደም ሲል በዚሁ ኢሜይል ከተፈጠረ ፓስወርዱን ብቻ ያድሰዋል
    user = User.objects.get(email=ADMIN_EMAIL)
    user.set_password(ADMIN_PASSWORD)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print(f"Superuser '{ADMIN_EMAIL}' password updated successfully!")