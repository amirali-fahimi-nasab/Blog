from celery import shared_task

from time import sleep

from .models import Blog


app = Celery('tasks', broker='amqp://guest@localhost//')

@app.task
def  send_view_blog(user , blog , text ):
    blogs = Blog.objects.create(user = user , blog = blog , text = text )
    sleep(60)
    return blogs

