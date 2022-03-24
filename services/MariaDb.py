from dotenv import load_dotenv
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

            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
        return conn.cursor()

    def get_host_names(self):
        host_names = {}
        self.connection.execute("SELECT domain.url, domain.account_id, domain.id FROM domain INNER JOIN auto_ad ON auto_ad.domain_id=domain.id and auto_ad.name = 'slider' GROUP BY domain.id;")
        for url, account_id, id in self.connection:
            host_names[account_id] = url

        return host_names