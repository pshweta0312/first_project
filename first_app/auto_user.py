import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

from faker import Faker
from first_app.models import User

fakegen = Faker()

def add_user():
    for i in range(n):
        name = fakegen.name().split()
        first = name[0]
        last = name[1]

        email = fakegen.email()
        print(User.objects.get_or_create(first_name = first,last_name=last,email_id=email))


if __name__ == '__main__':
    add_user(25)
