from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route with a path parameter
@app.get("/hello/{name}")
async def read_item(name: str):
    return {"Hello": name}
