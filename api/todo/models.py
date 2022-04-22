from django.db import models

class ToDoList(models.Model): 
    title = models.CharField("title",max_length=240)
    created = models.DateField(auto_now_add= True)
    def __str__(self):
        return self.title


class ToDoListItem(models.Model):
    todo_list = models.ForeignKey(
        ToDoList,
        related_name='items', on_delete=models.CASCADE , default=None,
        blank=True, null=True
    )
    title = models.CharField("title",max_length=240)
    created = models.DateField(auto_now_add= True)


    def __str__(self):
        return self.title
