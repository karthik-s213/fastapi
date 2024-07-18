from sqlalchemy import Column, Boolean, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from sql.settings import Base


#class Page()


class SubPage(Base):
    __tablename__ = "subpage"
    id = Column(Integer, primary_key=True)
    heading = Column(String, default="This is SubPage Heading")
    description = Column(String, default="This is Subpage Description")
    footer = Column(String, default="This is Subpage Footer")
    page_no = Column(Integer, default=1)
    page_dim = Column(Float, default=0.0)
    