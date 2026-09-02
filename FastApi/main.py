from fastapi import FastAPI


## To host the server
app = FastAPI()

@app.get("/")
async def root():
    return {"Message":"Hello World!"}

