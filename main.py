import uvicorn
from sys import argv

if __name__ == "__main__":
    try:
        port = int(argv[1])
    except:
        port = 7154
    uvicorn.run("frontend.app:app",host="0.0.0.0", port=port, reload=True)