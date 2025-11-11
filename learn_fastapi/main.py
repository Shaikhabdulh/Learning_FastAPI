from fastapi import FastAPI #Import
from typing import Optional
from pydantic import BaseModel
import uvicorn

app=FastAPI() #Instance


#Make note all dynamic routing must be below and arreng
# them properly and also make sure if you have static rout
# which is related to dynamic one or prefix
# match with static route so you have to arreng it properly

# Queary peremter
# http://localhost:5010/about?limit=100

@app.get('/about')
def data(limit=10, published:bool = True, sort:Optional[str] = None):
    if published:
        return {'data':f'{limit} published blogs from db'}
    else:
        return {'data':f'{limit} blogs from db'}

@app.get('/about/{id}/info')
def id(id:int):
    if int(id)==100:
        return (f"HI Abdul your id is {id}")
    else:
        return (f"your id {id} not found")

@app.get('/') #Decorator
def index(): #Function
    return {'data':{'name':'abdul'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = None

@app.post('/blog')
def create_blog(blog:Blog):
    if blog.published:
        return {"data":f"""Blog is created with title {blog.title} & also published\n
                   Body is {blog.body} \n
            """}
    return {"data":f"""Blog is created with title {blog.title} \n {blog.body}"""}

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=5010, reload=True)