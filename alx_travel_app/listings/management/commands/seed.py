from django.core.management.base import BaseCommand
from listings.models import Listing


class Command(BaseCommand):
    help = "Seed the database with sample listings data"

    def handle(self, *args, **kwargs):
        sample_data = [
            {
                "title": "Beach Resort",
                "description": "Beautiful view of the ocean.",
                "location": "Cape Coast",
                "price_per_night": 450.00
            },
            {
                "title": "Mountain Cabin",
                "description": "Quiet stay with a mountain view.",
                "location": "Aburi",
                "price_per_night": 300.00
            },
            {
                "title": "City Apartment",
                "description": "Modern apartment in the city center.",
                "location": "Accra",
                "price_per_night": 550.00
            },
        ]

        for item in sample_data:
            Listing.objects.get_or_create(**item)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully with sample listings."))
