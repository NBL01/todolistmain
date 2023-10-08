from locust import HttpUser, task, between, TaskSet
class TodoListUser(HttpUser):
    wait_time = between(2, 5)
    
    @task(1)
    def view_tasks(self):
        self.client.get("/")
    
    @task(2)
    def update_task(self):
        self.client.get("/update_task/5/")
    
    @task(3)
    def delete_task(self):
        self.client.get("/delete_task/5/")