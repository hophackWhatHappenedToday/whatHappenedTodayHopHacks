# create an mysql engine
from sqlalchemy import create_engine

def get_mysql_eng():
    mysql_url = "mysql+pymysql://root:hophacks12345@34.121.253.129:3306/whatHappenedToday?charset=utf8"

    engine = create_engine(mysql_url, echo=False, pool_size=20, max_overflow=100)
    
    return engine