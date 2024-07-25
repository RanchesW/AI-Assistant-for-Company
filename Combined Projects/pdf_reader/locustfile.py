import os
from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(1)
    def index(self):
        response = self.client.get("/")
        if response.status_code != 200:
            print(f"Failed to load index page: {response.status_code}")

    @task(2)
    def analyze_pdf(self):
        file_path = os.path.join(os.path.dirname(__file__), 'ВНД о парольной защите.pdf')
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return

        with open(file_path, 'rb') as f:
            files = {'file': ('ВНД о парольной защите.pdf', f, 'application/pdf')}
            data = {'query': 'Генеральный директор PetroRetail'}
            response = self.client.post("/analyze", files=files, data=data)
            if response.status_code != 200:
                print(f"Failed to analyze PDF: {response.status_code}")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
