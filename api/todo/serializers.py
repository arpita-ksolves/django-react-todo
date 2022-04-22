from rest_framework import serializers
# import our models
from todo import models
from drf_writable_nested import WritableNestedModelSerializer

class ToDoListItem(serializers.ModelSerializer):

    class Meta:
        model = models.ToDoListItem
        fields = ('id', 'todo_list_id', 'title', 'created')
        # depth = 1
         

class ToDoList(WritableNestedModelSerializer,serializers.ModelSerializer):
    items = ToDoListItem(many=True, required=False)
    # items = serializers.RelatedField(source='ToDoListItem', read_only=True)

    class Meta:
        model = models.ToDoList
        fields = ('id','title', 'items','created' )
        depth = 1
    

    # def create(self,validated_data):
    #   return models.ToDoListItem.objects.create(**validated_data)


    # def create(self, validated_data):
       
    #     items_data = validated_data.pop('items')
    #     # create a new ToDoList with the validated data passed in
    #     todo_list = models.ToDoList.objects.create(**validated_data)
    #     # for each item in the 'items' validated data
    #     for item_data in items_data:
    #         # modify it's validated data to reference the ToDoList we just made
    #         item_data['todo_list_id'] = todo_list.id
    #         # Create the ToDoListItem with the item data
    #         models.ToDoListItem.objects.create(**item_data)
    #     # after this return the todo_list we made
    #     return todo_list