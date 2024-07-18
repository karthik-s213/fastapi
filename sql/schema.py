from pydantic import BaseModel


class SubPageBase(BaseModel):
    heading: str
    description: str
    footer: str
    page_no: int
    page_dim: float


class SubPageCreate(SubPageBase):
    pass


class SubPage(SubPageBase):
    id: int

    class Config:
        orm_mode = True
