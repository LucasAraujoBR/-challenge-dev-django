import os
import django
from retry import retry
from django.db import OperationalError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

@retry(OperationalError, delay=2, tries=30)
def create_superuser():
    # Verificar se o superusuário já existe
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser("admin", "admin@admin.com", "admin123")
    else:
        print("The superuser already exists. A new one has not been created.")

create_superuser()
