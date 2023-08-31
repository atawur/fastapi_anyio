from .async_task import AsyncTask
from fastapi import Depends
class TaskManager():

    def __init__(self,async_task: AsyncTask = Depends(AsyncTask) ):
        self.async_task = async_task

    def start_task(self, job_cls, *args, **kwargs):
            task = job_cls(*args, **kwargs)
            print("Task  starting from Task Manager")
            return self.async_task.create_async_task(task)
