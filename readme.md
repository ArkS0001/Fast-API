![images](https://github.com/ArkS0001/Fast-API/assets/113760964/097c8ecd-b9b3-44c3-bd45-71ea020e7027)


Documentation: https://fastapi.tiangolo.com

Source Code: https://github.com/tiangolo/fastapi

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.

![fastapi](https://github.com/ArkS0001/Fast-API/assets/113760964/ad704768-d413-4c3a-a031-99c094ffa092)


The key features are:

    Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
    Fast to code: Increase the speed to develop features by about 200% to 300%. *
    Fewer bugs: Reduce about 40% of human (developer) induced errors. *
    Intuitive: Great editor support. Completion everywhere. Less time debugging.
    Easy: Designed to be easy to use and learn. Less time reading docs.
    Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
    Robust: Get production-ready code. With automatic interactive documentation.
    Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.


To create a FastAPI application that serves HTML content for display in a web browser, you can use FastAPI's HTMLResponse class to return HTML content as a response. Here's an example:

python

from fastapi import FastAPI, HTMLResponse

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route to serve HTML content
@app.get("/")
async def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FastAPI HTML Example</title>
    </head>
    <body>
        <h1>Hello, FastAPI!</h1>
        <p>This is an example of serving HTML content with FastAPI.</p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

In this code:

    The / route is defined to serve HTML content.
    The HTMLResponse class is used to return the HTML content as a response.
    The HTML content is stored as a multi-line string within the html_content variable.

To run this FastAPI application, follow the same steps as before:

    Install FastAPI and Uvicorn if you haven't already:

pip install fastapi uvicorn

    Save the code above in a Python file (e.g., main.py).

    Run the application using Uvicorn:

css

uvicorn main:app --reload

Now, you can access the application in your browser at http://localhost:8000, and you'll see the HTML content displayed.
