import requests
from datetime import date
from bs4 import BeautifulSoup
from models import Ad
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
session = Session()

def parser(session:Session):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/105.0.0.0 Safari/537.36"

    }
    for page in range(0, 95):
        response = requests.get(url=f"https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273", headers=headers)
        soup = BeautifulSoup(response.content, "lxml")
        items = soup.find_all("div", class_="search-item")

        for item in items:
            date_creations = item.find("span", class_="date-posted").text.strip()
            if len(date_creations) > 10:
                date_creations = date.today()
            

            whole_info = Ad(
            apartment_name=item.find("div", class_="title").text.strip(),
            image=item.find("img").get("data-src"),
            description=item.find("div", class_="description").text.strip().split("...")[0],
            price=item.find("div", class_="price").text.strip(),
            locations=item.find("span", class_="").text.strip(),
            count_bed=item.find("span", class_="bedrooms").text.strip().split("\n")[-1].strip(),
            date_posted=date_creations
            )
            session.add(whole_info)
            session.commit()

        print(f"Обработано {page} из 94")


def main():
    parser(SessionLocal)


if __name__ == '__main__':
    main()




