from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def func():
    return {"message":"v2 testing cicd",
            "message2": "test message"}