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

# @app.get("/sub/{sub_page}")
# async def subPage(sub_page:int):
    
#     return new_dict.get(sub_page)

# @app.get("/sub/{sub_page}")
# async def subPage(sub_page:float):
    
#     return new_dict.get(sub_page)

@app.get("/sub/fixed")
async def subPage():
    
    return "Page fixed"

# @app.get("/sub/{sub_page}/{query}")
# async def subPage(sub_page:str,query:int):
    
#     return new_dict.get(sub_page)

@app.get("/sub/{sub_page}")
async def subPage(sub_page: str):
    
    return new_dict.get(sub_page)