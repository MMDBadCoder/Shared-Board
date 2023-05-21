import os
from datetime import datetime, timedelta
from threading import Thread
from time import sleep

from django.core.asgi import get_asgi_application

from post.models import MyPost

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SharedBoard.settings')

application = get_asgi_application()


def deletion_thread():
    while True:
        MyPost.objects.filter(uploaded_at__lt=datetime.now() - timedelta(days=15)).delete()
        sleep(36000)


Thread(target=deletion_thread).start()
