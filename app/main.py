from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_test():
    return "CI/CD success"