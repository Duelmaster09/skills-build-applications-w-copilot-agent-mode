from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor', 'Hulk'])
        dc = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman', 'Flash'])

        # Users
        User.objects.create(username='ironman', email='ironman@marvel.com', team=marvel.name)
        User.objects.create(username='captainamerica', email='cap@marvel.com', team=marvel.name)
        User.objects.create(username='thor', email='thor@marvel.com', team=marvel.name)
        User.objects.create(username='hulk', email='hulk@marvel.com', team=marvel.name)
        User.objects.create(username='superman', email='superman@dc.com', team=dc.name)
        User.objects.create(username='batman', email='batman@dc.com', team=dc.name)
        User.objects.create(username='wonderwoman', email='wonderwoman@dc.com', team=dc.name)
        User.objects.create(username='flash', email='flash@dc.com', team=dc.name)

        # Activities
        Activity.objects.create(user='ironman', type='run', duration=30, calories=300, date='2025-11-09')
        Activity.objects.create(user='superman', type='swim', duration=45, calories=400, date='2025-11-09')
        Activity.objects.create(user='batman', type='cycle', duration=60, calories=500, date='2025-11-09')
        Activity.objects.create(user='thor', type='lift', duration=20, calories=250, date='2025-11-09')

        # Leaderboard
        Leaderboard.objects.create(team=marvel.name, points=1200)
        Leaderboard.objects.create(team=dc.name, points=1100)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='Easy')
        Workout.objects.create(name='Sprints', description='Run 5 sprints', difficulty='Medium')
        Workout.objects.create(name='Deadlift', description='Deadlift 100kg', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
