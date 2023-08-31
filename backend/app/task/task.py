from abc import ABC
from typing import Callable, Coroutine,Any

from .async_task import AsyncTask


class Task(ABC):
    def __init__(self):
        # self.before()
        # self.callble()
        # self.after()
        pass

    async def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.before()
        await self.sometask()   
        self.after()  

    # def __call__(self, *args: Any, **kwds: Any) -> Any:
    #     print("call method called")
    #     self.before()
    #     self.callble()
    #     self.after()

    def sometask(self):
        pass

    def before(self):
        pass    

    def after(self):
        pass

