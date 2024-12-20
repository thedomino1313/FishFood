from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from contextlib import asynccontextmanager
from stepper import Stepper

class status(BaseModel):
    value: bool

class offset(BaseModel):
    offset: int 

good = status(value=True)
bad  = status(value=False)
off  = offset(offset=0)


async def not_found(*_):
    return RedirectResponse("http://domlaptop:7154/feedthe.fish/404.html")


exceptions = {
    404: not_found,
}

try:
    stepper = Stepper()
except:
    stepper = None

@asynccontextmanager
async def lifespan(_):
    yield
    if stepper:
        stepper.disconnect()
        print("Disconnected Stepper")

app = FastAPI(exception_handlers=exceptions, lifespan=lifespan)

app.mount('/feedthe.fish', StaticFiles(directory='frontend/static', html=True), name='static')


@app.get("/")
@app.get("/feedthe.fish")
async def response():
    if stepper:
        return RedirectResponse("http://domlaptop:7154/feedthe.fish/rotate.html")
    else:
        return RedirectResponse("http://domlaptop:7154/feedthe.fish/connection.html")


@app.post("/rotate", response_model=status)
async def rotate():
    try:
        stepper.rotate(0.01, int(Stepper.STEPS_PER_REVOLUTION/28) + (1 if off.offset == 0 else 0))
        off.offset = this if (this := off.offset + 1) <= 3 else 0
        return good
    except Exception as e:
        print(e)
        return bad

@app.post("/connect", response_model=status)
async def rotate():
    try:
        stepper = Stepper()
        return good
    except Exception as e:
        print(e)
        stepper = None
        return bad
    
@app.post("/stepper_diagnostic", response_model=status)
async def diag():
    return good if stepper else bad