from abc import ABC
from typing import Callable, Coroutine,Any

from .async_task import AsyncTask

from .task import Task
from anyio import sleep

class OpsTask(Task):
   
   
    def __init__(self,task_name='', **kwargs) -> None:
        super().__init__()
        self.task_name = task_name    
 

    async def sometask(self):
       
        #print(f"{self.task_name} ")
        i=0
        while(True):
            await sleep(1)
            i+=1
            print(f"processing:{i}")
        
        print(f"========task ({self.task_name}) finished==========")
        return 

    def before(self):
        print("before is calling")    

    def after(self):
        print("after is calling")