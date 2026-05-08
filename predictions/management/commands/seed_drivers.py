from django.core.management.base import BaseCommand
from predictions.models import Driver

DRIVERS = [
    {"name": "Max Verstappen", "team": "Red Bull", "number": 3},
    {"name": "Isack Hadjar", "team": "Red Bull", "number": 6},
    {"name": "Lewis Hamilton", "team": "Ferrari", "number": 44},
    {"name": "Charles Leclerc", "team": "Ferrari", "number": 16},
    {"name": "George Russell", "team": "Mercedes", "number": 63},
    {"name": "Kimi Antonelli", "team": "Mercedes", "number": 12},
    {"name": "Lando Norris", "team": "McLaren", "number": 1},
    {"name": "Oscar Piastri", "team": "McLaren", "number": 81},
    {"name": "Fernando Alonso", "team": "Aston Martin", "number": 14},
    {"name": "Lance Stroll", "team": "Aston Martin", "number": 18},
    {"name": "Pierre Gasly", "team": "Alpine", "number": 10},
    {"name": "Franco Colapinto", "team": "Alpine", "number": 43},
    {"name": "Carlos Sainz", "team": "Williams", "number": 55},
    {"name": "Alex Albon", "team": "Williams", "number": 23},
    {"name": "Arvid Lindblad", "team": "Racing Bulls", "number": 41},
    {"name": "Liam Lawson", "team": "Racing Bulls", "number": 30},
    {"name": "Esteban Ocon", "team": "Haas", "number": 31},
    {"name": "Oliver Bearman", "team": "Haas", "number": 87},
    {"name": "Nico Hulkenberg", "team": "Audi", "number": 27},
    {"name": "Gabriel Bortoleto", "team": "Audi", "number": 5},
    {"name": "Sergio Perez", "team": "Cadillac", "number": 11},
    {"name": "Valtteri Bottas", "team": "Cadillac", "number": 77},
]


class Command(BaseCommand):
    help = "Seed the database with 2026 F1 drivers"

    def handle(self, *args, **options):
        created_count = 0
        for driver_data in DRIVERS:
            _, created = Driver.objects.get_or_create(
                name=driver_data["name"],
                defaults={
                    "team": driver_data["team"],
                    "number": driver_data["number"],
                },
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"Created: {driver_data['name']}"))
            else:
                self.stdout.write(f"Already exists: {driver_data['name']}")

        self.stdout.write(self.style.SUCCESS(f"\nDone! {created_count} new drivers created."))