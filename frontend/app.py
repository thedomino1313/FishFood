from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from contextlib import asynccontextmanager
from stepper import Stepper

class status(BaseModel):
    value: bool

good = status(value=True)
bad  = status(value=False)

async def not_found(request, exc):
    return RedirectResponse("http://domlaptop:8001/feedthe.fish/404.html")


exceptions = {
    404: not_found,
}

stepper = Stepper()

@asynccontextmanager
async def lifespan(_):
    yield
    stepper.disconnect()
    print("Disconnected Stepper")

app = FastAPI(exception_handlers=exceptions, lifespan=lifespan)

app.mount('/feedthe.fish', StaticFiles(directory='frontend/static', html=True), name='static')


@app.get("/")
@app.get("/feedthe.fish")
async def response():
    return RedirectResponse("http://domlaptop:8001/feedthe.fish/rotate.html")

# @app.get("/{value}")
# async def uhoh():
#     return RedirectResponse("http://domlaptop:8001/feedthe.fish/rotate.html")

@app.post("/rotate", response_model=status)
async def rotate():
    try:
        stepper.rotate(1, 2)
        return good
    except Exception as e:
        print(e)
        return bad