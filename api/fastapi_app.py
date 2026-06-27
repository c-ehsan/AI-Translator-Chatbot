from fastapi import FastAPI 


class API:
    def __init__(self) -> None:
        self.app=FastAPI()
        self.regists_roots()

    def regists_roots(self):
        @self.app.get("/")
        async def root():
            return {"message":"Hello World"}


api=API()
app=api.app