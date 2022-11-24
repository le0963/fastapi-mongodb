from fastapi import FastAPI
from routes.user import user
from routes.book import book

app = FastAPI(
  title="Mongodb Fastapi",
  description="Simple REstAPI for create users and books with CRUD",
  version="0.0.1",
)


app.include_router(user) 
app.include_router(book) 
