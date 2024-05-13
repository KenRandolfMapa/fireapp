from django.core.management.base import BaseCommand
from faker import Faker
from fire.models import Locations, Incident, FireStation, Firefighters, FireTruck, WeatherConditions

class Command(BaseCommand):
    help = 'Populate database with initial data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        self.create_locations(fake, 10)
        self.create_fire_stations(fake, 5)
        self.create_firefighters(fake, 20)
        self.create_incidents(fake, 50)
        self.create_fire_trucks(fake, 10)
        self.create_weather_conditions(fake, 50)

    def create_locations(self, fake, num_records):
        for _ in range(num_records):
            Locations.objects.create(
                name=fake.company(),
                latitude=fake.latitude(),
                longitude=fake.longitude(),
                address=fake.address(),
                city=fake.city(),
                country=fake.country()
            )

    def create_incidents(self, fake, num_records):
        locations = Locations.objects.all()
        for _ in range(num_records):
            incident_location = fake.random_element(locations)
            Incident.objects.create(
                location=incident_location,
                date_time=fake.date_time_this_year(),
                severity_level=fake.random_element(Incident.SEVERITY_CHOICES)[0],
                description=fake.text(max_nb_chars=250)
            )

    def create_fire_stations(self, fake, num_records):
        for _ in range(num_records):
            FireStation.objects.create(
                name=fake.company(),
                latitude=fake.latitude(),
                longitude=fake.longitude(),
                address=fake.address(),
                city=fake.city(),
                country=fake.country()
            )

    def create_firefighters(self, fake, num_records):
        fire_stations = FireStation.objects.all()
        for _ in range(num_records):
            fire_station = fake.random_element(fire_stations)
            Firefighters.objects.create(
                name=fake.name(),
                rank=fake.random_element(Firefighters.XP_CHOICES)[0],
                experience_level=fake.random_int(min=1, max=30),
                station=fire_station
            )

    def create_fire_trucks(self, fake, num_records):
        fire_stations = FireStation.objects.all()
        for _ in range(num_records):
            fire_station = fake.random_element(fire_stations)
            FireTruck.objects.create(
                truck_number=fake.random_int(min=100, max=999),
                model=fake.word(),
                capacity=fake.random_int(min=1000, max=5000),
                station=fire_station
            )

    def create_weather_conditions(self, fake, num_records):
        incidents = Incident.objects.all()
        for _ in range(num_records):
            incident = fake.random_element(incidents)
            WeatherConditions.objects.create(
                incident=incident,
                temperature=fake.random_int(min=-20, max=50),
                humidity=fake.random_int(min=0, max=100),
                wind_speed=fake.random_int(min=0, max=50),
                weather_description=fake.sentence()
            )
