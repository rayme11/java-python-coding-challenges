from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)  # Users wait between 1 and 2 seconds between tasks

    @task
    def get_posts(self):
        # Simulate fetching posts from a placeholder API
        self.client.get("/posts/1", name="/posts/[id]")

    @task(3) # This task will be called 3 times more often than other tasks
    def create_post(self):
        # Simulate creating a new post
        headers = {'Content-type': 'application/json; charset=UTF-8'}
        payload = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        self.client.post("/posts", json=payload, headers=headers)

if __name__ == "__main__":
    # In a real CI/CD setup, Locust would be run via command line
    # Example: locust -f api_performance_test.py --host=https://jsonplaceholder.typicode.com
    print("This script defines Locust performance tests.")
    print("To run: pip install locust && locust -f api_performance_test.py --host=https://jsonplaceholder.typicode.com")
    print("Open http://localhost:8089 in browser after running to see results.")