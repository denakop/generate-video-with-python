import requests
import os


class Jenkins:
    def __init__(self):
        self.url = os.getenv("JENKINS_URL")
        self.username = os.getenv("JENKINS_USERNAME")
        self.password = os.getenv("JENKINS_PASSWORD")

    def send_request_to_jenkins(self, account_id):
        requests.post(self.url, auth=(self.username, self.password), json={"CLIENT_ID": account_id})
