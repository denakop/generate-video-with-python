from dotenv import load_dotenv
from datetime import datetime

import os
import mariadb
import sys


class MariaDb:
    def __init__(self):
        load_dotenv()
        self.host = os.getenv("DATABASE_HOST")
        self.user = os.getenv("DATABASE_USER")
        self.password = os.getenv("DATABASE_PASSWORD")
        self.dbname = os.getenv("DATABASE_NAME")
        self.port = os.getenv("DATABASE_PORT")
        self.connection = self.connect()

    @staticmethod
    def connect():
        try:
            conn = mariadb.connect(
                user=os.getenv("DATABASE_USER"),
                password=os.getenv("DATABASE_PASSWORD"),
                host=os.getenv("DATABASE_HOST"),
                port=int(os.getenv("DATABASE_PORT")),
                database=os.getenv("DATABASE_NAME"),
                autocommit=True,

            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
        return conn.cursor()

    def get_host_names(self):
        query ="SELECT domain.url, domain.account_id, domain.id, domain.video_date FROM domain INNER JOIN auto_ad ON auto_ad.domain_id=domain.id and auto_ad.name = 'slider' GROUP BY domain.id;"
        
        if(os.getenv("ACCOUNT_ID")):
            account_id = os.getenv("ACCOUNT_ID")
            query = f"SELECT domain.url, domain.account_id, domain.id, domain.video_date FROM domain INNER JOIN auto_ad ON auto_ad.domain_id=domain.id and auto_ad.name = 'slider' WHERE domain.account_id = '{account_id}' GROUP BY domain.id;"
        
        host_names = []
        self.connection.execute(query)
        for url, account_id, id, video_date in self.connection:
            host_names.append({account_id: {'url': url, 'id': id, 'video_date': video_date}})

        return host_names

    def update_video_date_in_domain(self, hostname):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        url = "http://" + hostname
        self.connection.execute(f"UPDATE domain SET video_date = '{date}' WHERE url = '{url}'")
