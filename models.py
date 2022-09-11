from database import Base, engine
from sqlalchemy.orm import Session
from sqlalchemy import Column, String, Integer, Date


class Ad(Base):
    __tablename__ = "kijiji"

    id = Column(Integer, primary_key=True)
    image = Column("image", String)
    apartment_name = Column("apart_name", String)
    date_posted = Column("date_publication", String)
    locations = Column("location", String)
    count_bed = Column("bed_count", String)
    description = Column("description", String)
    price = Column("price", String)


