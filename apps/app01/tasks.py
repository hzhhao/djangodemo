from djangodemo.celery import app
from .models import Type1
from datetime import datetime
@app.task()
def say_hello():
    Type1.objects.create(
        name="hello",
        add_time=datetime.now
    )
    print("hello world")
    return "成功添加数据"
