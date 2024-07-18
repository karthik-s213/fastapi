from fastapi import FastAPI

app = FastAPI()

# CRUD APIS :
# C - Create (Post)
# R - Read   (Get)
# U - Update (Put/Patch)
# D - Delete (Delete)

@app.get("/")
async def root():
    # return {"message" : "This is karthik home page"}
    return "This is karthik home page"

@app.get("/sub")
async def subPage():
    return "This is subpage"

"""
ORM - Object Relational Mappers
Sql Alchemy
"""