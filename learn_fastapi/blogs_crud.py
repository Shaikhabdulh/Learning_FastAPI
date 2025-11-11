from fastapi import FastAPI
from schema import schemas
import uvicorn

app=FastAPI()

@app.post("/blog")
def create(request: schemas.Blog):
    return request

if __name__ == "__main__":
    uvicorn.run ('blogs_crud:app', host="0.0.0.0", port=5010, reload=True)