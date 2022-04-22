from django.test import TestCase
from django.test import TestCase
from todo.models import ToDoList, ToDoListItem

class ToDoListTestCase(TestCase):
    """Tests for the todo list models"""

    def test_todo_list(self): 
        """Test creating a todo list with no items"""
        # create a todo list object (this saves it to the database)
        ToDoList.objects.create(title="Test List")
        # verify the object was saved
        todo_list = ToDoList.objects.get(title="Test List")
        # verify the data is accurate and exists
        self.assertEqual(todo_list.title, "Test List")
        # delete the list 
        todo_list.delete()
        # try to retrieve the todo list and make sure it's not there
        try: 
            retrieved_list = ToDoList.objects.get(title="Test List")
        # catch the DoesNotExist error that we're hoping to get
        except ToDoList.DoesNotExist: 
            retrieved_list = None
        self.assertEqual(retrieved_list, None)
