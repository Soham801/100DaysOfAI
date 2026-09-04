from fastapi import FastAPI


## To host the server
app = FastAPI()

## Server 
#http://127.0.0.1:8000/redoc
#http://127.0.0.1:8000/docs

@app.get("/")
async def root():
    return {"message":"Hello World!"}

@app.get("/about")
def about():
    return {'message': "CampusX is an education platform where you can learn AI"}