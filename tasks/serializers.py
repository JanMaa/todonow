from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'

	# def create(self, user, user_data):
	# 	task = Task(
	# 		user=user,
	# 		title=user_data['title'],
	# 	)

	# 	task.save()

	# 	return task

class CustomTaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user')
		super().__init__(*args, **kwargs)

	def validate(self, data):
		user = self.user

		data['user'] = user
		return data
