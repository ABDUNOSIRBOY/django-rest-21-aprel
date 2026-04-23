from django.core.management.base import BaseCommand
from faker import Faker
from market.models import Daraxt
from random import randint
fake = Faker("uz_UZ")

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("fake Daraxt yaratilmoqda...")
        daraxts = Daraxt.objects.all()
        for _ in range(100):
            cateogry = daraxts.order_by("?").first()
            Daraxt.objects.create(
                title=fake.name(),
                price=randint(10000,99999),
                is_active=True if randint(0, 1) else False
            )
        self.stdout.write(self.style.SUCCESS("daraxtlar yaratildi!"))
