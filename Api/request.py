from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel



class SubPage(BaseModel):
    heading: str | None = "subpage of heading"
    description: str | None = "Description of SubPage"
    footer: str | None = "Footer of SubPage"
    page_no: int | None = 0
    page_dim: float | None = 0.0


app = FastAPI()


new_dict = {
    0: {
    "heading": "subpage of heading 0",
    "description": "Description of SubPage 0",
    "footer": "Footer of SubPage 0",
    "page_no": 0,
    "page_dim": 5.24
  }
}


@app.get("/")
async def getpage():
    return new_dict


@app.post("/sub")
async def subPage(sub: SubPage):
    if sub.page_no in new_dict:
        new_dict[sub.page_no] = sub
        return "already there"
    else:
        new_dict[sub.page_no] = sub
        return "succesfully inserted"
    
    
@app.put("/put/{page_no}")
async def putpage(page_no: int, sub: SubPage):
    if page_no in new_dict:
        new_dict[sub.page_no] = sub
        return "pages updated"
    else:
        return "no pages found"
        
        
@app.delete("/delete/{page_no}")
async def deletepage(page_no: int, sub: SubPage):
    if page_no in new_dict:
        del new_dict[page_no]
        return "item is deleted"
    else:
        return "no items in the page"


@app.patch("/patch/{page_no}")
async def patchpage(page_no: int, sub: SubPage):
    if new_dict.get(page_no):
        sub_copy = dict(sub)
        for key,value in sub_copy.items():
            new_dict[page_no][key] = sub_copy[key]
        return new_dict
    else:
        return "can't update"
