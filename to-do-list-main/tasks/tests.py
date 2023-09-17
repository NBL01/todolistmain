from django.test import TestCase
from django.urls import reverse, resolve
from tasks.views import index, updateTask, deleteTask


class URLRoutingTests(TestCase):

    def test_list_url_resolves(self):
        url = reverse('list')
        self.assertEqual(resolve(url).func, index)

    def test_update_task_url_resolves(self):
        url = reverse('update_task', args=['1'])
        self.assertEqual(resolve(url).func, updateTask)

    def test_delete_url_resolves(self):
        url = reverse('delete', args=['1'])
        self.assertEqual(resolve(url).func, deleteTask)
