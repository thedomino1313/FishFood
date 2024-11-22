from fastapi import FastAPI
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount('/frontend/static', StaticFiles(directory='frontend/static', html=True), name='static')

@app.get("/")
@app.get("/test")
async def response():
    return RedirectResponse("http://127.0.0.1:8000/frontend/static/test.html")
