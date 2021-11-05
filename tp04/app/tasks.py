from celery import Celery

app = Celery('hello', broker='pyamqp://admin:12345@rabbit//')

@app.task
def hello():
    return 'hello world'
