from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the MongoDB database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']

        # Insert test users
        users = db.users
        users.insert_many([
            {"email": "john.doe@example.com", "name": "John Doe", "age": 16},
            {"email": "jane.smith@example.com", "name": "Jane Smith", "age": 17}
        ])

        # Insert test teams
        teams = db.teams
        teams.insert_one({"name": "Team Alpha", "members": ["john.doe@example.com", "jane.smith@example.com"]})

        # Insert test activities
        activities = db.activities
        activities.insert_many([
            {"user": "john.doe@example.com", "type": "Running", "duration": 30, "date": "2025-04-01"},
            {"user": "jane.smith@example.com", "type": "Walking", "duration": 45, "date": "2025-04-02"}
        ])

        # Insert test leaderboard entries
        leaderboard = db.leaderboard
        leaderboard.insert_one({"user": "jane.smith@example.com", "points": 150})

        # Insert test workouts
        workouts = db.workouts
        workouts.insert_many([
            {"name": "Morning Yoga", "description": "A relaxing yoga session", "duration": 60},
            {"name": "HIIT", "description": "High-intensity interval training", "duration": 30}
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated the MongoDB database with test data'))
