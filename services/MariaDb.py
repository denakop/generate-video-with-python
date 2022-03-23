from dotenv import load_dotenv
import os

class MariaDb:
    def __init__(self):
        load_dotenv()
        self.host = os.getenv("DATABASE_HOST")
        self.user = os.getenv("DATABASE_USER")
        self.password = os.getenv("DATABASE_PASSWORD")
        self.dbname = os.getenv("DATABASE_NAME")

    def get_connection_string(self):
        return "mysql+pymysql://{user}:{password}@{host}/{dbname}".format(
            user=self.user,
            password=self.password,
            host=self.host,
            dbname=self.dbname
        )
