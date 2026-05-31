import os
import django
from django.test import Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wordhunt.settings')
django.setup()

client = Client()

urls_to_test = [
    '/',
    '/register/',
    '/login/',
    '/create/',
    '/api/leaderboard/',
]

for url in urls_to_test:
    try:
        response = client.get(url)
        print(f"URL {url} - Status Code: {response.status_code}")
    except Exception as e:
        print(f"URL {url} - Exception: {e}")
