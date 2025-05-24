from locust import HttpUser, task, between

class PortfolioUser(HttpUser):
    wait_time = between(1, 3)  # seconds between tasks

    @task
    def get_portfolio(self):
        self.client.get("/api/portfolio")
