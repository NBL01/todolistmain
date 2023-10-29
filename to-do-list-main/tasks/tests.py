# # from django.test import TestCase
# # from django.urls import reverse, resolve
# # from tasks.views import index, updateTask, deleteTask


# # class URLRoutingTests(TestCase):

# #     def test_list_url_resolves(self):
# #         url = reverse('list')
# #         self.assertEqual(resolve(url).func, index)

# #     def test_update_task_url_resolves(self):
# #         url = reverse('update_task', args=['1'])
# #         self.assertEqual(resolve(url).func, updateTask)

# #     def test_delete_url_resolves(self):
# #         url = reverse('delete', args=['1'])
# #         self.assertEqual(resolve(url).func, deleteTask)

# -------------------------------------------------
# from django.test import TestCase
# from .models import Task

# class SmokeTest(TestCase):
#     def test_create_task(self):
#         # Test if you can create a Task instance
#         task = Task.objects.create(title="Test Task")
#         self.assertEqual(task.title, "Test Task")

#     def test_read_task(self):
#         # Test if you can retrieve a Task instance from the database
#         task = Task.objects.create(title="Test Task")
#         retrieved_task = Task.objects.get(id=task.id)
#         self.assertEqual(retrieved_task.title, "Test Task")

#     def test_update_task(self):
#         # Test if you can update a Task instance
#         task = Task.objects.create(title="Test Task")
#         task.title = "Updated Task"
#         task.save()
#         updated_task = Task.objects.get(id=task.id)
#         self.assertEqual(updated_task.title, "Updated Task")

#     def test_delete_task(self):
#         # Test if you can delete a Task instance
#         task = Task.objects.create(title="Test Task")
#         task_id = task.id
#         task.delete()
#         with self.assertRaises(Task.DoesNotExist):
#             Task.objects.get(id=task_id)



# class TaskIntegrationTests(TestCase):

#     def test_create_and_list_tasks(self):
#         # Create a task
#         response = self.client.post(reverse('create_task'), {'title': 'Test Task'})
#         self.assertEqual(response.status_code, 302)  # Expect a redirect after successful creation

#         # Check if the task was created in the database
#         task = Task.objects.get(title='Test Task')
#         self.assertEqual(task.title, 'Test Task')

#         # List tasks and check if the created task is in the response
#         response = self.client.get(reverse('list_tasks'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Test Task')

#     def test_delete_task(self):
#         # Create a task
#         task = Task.objects.create(title='Test Task')

#         # Delete the task
#         response = self.client.post(reverse('delete_task', args=[task.id]))
#         self.assertEqual(response.status_code, 302)  # Expect a redirect after successful deletion

#         # Check if the task was deleted from the database
#         with self.assertRaises(Task.DoesNotExist):
#             Task.objects.get(id=task.id)


# ----------------Database testing-----------------------------

# from django.test import TestCase
# from .models import Task  # Import the Task model from your application

# class TaskDatabaseTests(TestCase):

#     def test_create_and_retrieve_task(self):
#         # Create a task in the database
#         Task.objects.create(title='Test Task')

#         # Retrieve the task from the database
#         saved_tasks = Task.objects.all()
#         self.assertEqual(saved_tasks.count(), 1)

#         task = saved_tasks[0]
#         self.assertEqual(task.title, 'Test Task')

#     def test_delete_task(self):
#         # Create a task in the database
#         task = Task.objects.create(title='Test Task')

#         # Delete the task
#         task.delete()

#         # Verify that the task is no longer in the database
#         saved_tasks = Task.objects.all()
#         self.assertEqual(saved_tasks.count(), 0)


from selenium import webdriver

class UITestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='path/to/chromedriver')
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_ui_workflow(self):
        # Open the web page in the browser
        self.driver.get('http://localhost:8000')  # Replace with your application's URL

        # Interact with the UI
        title_input = self.driver.find_element_by_name('title')
        title_input.send_keys('Test Task')

        description_input = self.driver.find_element_by_name('description')
        description_input.send_keys('This is a test task.')

        submit_button = self.driver.find_element_by_id('submit-button')
        submit_button.click()

        # Wait for the page to load and check the result
        task_list = self.driver.find_element_by_id('task-list')
        self.assertIn('Test Task', task_list.text)
