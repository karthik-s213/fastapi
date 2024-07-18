from fastapi import FastAPI

app = FastAPI()


new_dict = {
    1: "value1",
    2.7: "value2",
    "key3": "value3",
}


@app.get("/")
async def root():
    return "This is karthik"


@app.get("/sub")
async def subPage(sub_page: int = 1, query: int = 5):
    
    if new_dict.get(sub_page):
        return new_dict.get(sub_page)
    else:
        return "Vlaue not found in the new_dict"
# @app.get("/sub")
# async def subPage(sub_page:float =2.7 , query:int = 5):
#     return new_dict.get(sub_page)

# Request URL  : http://127.0.0.1:8000/sub?sub_page=2.7&query=5

# @app.get("/sub")
# async def subPage(sub_page:str = "key3", query:int = 5):
#     return new_dict.get(sub_page)


@app.get("/tree")
async def subPage(sub_page: int = 1, query: int | None = 5):
    if new_dict.get(sub_page):
        return new_dict.get(sub_page)
    else:
        return "Value not found in the new_dict"