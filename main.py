from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return 'Funcionou'

if __name__ == '__main__':
    import uvicorn 
    uvicorn.run("main:app", host="0.0.0.0", port=10000)