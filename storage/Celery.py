from celery import Celery
from PyChatBot import send_message
celeryName = 'bot_reminder'
celery = Celery(celeryName, broker='redis://localhost:6379/0')


@celery.task
def task_to_background(user_id, what_to_remind):
    result = send_message(user_id, what_to_remind)
    return result
