from threading import Thread

from rest_framework import serializers, viewsets

from .models import TaskTmpl, Task
from .core import PythonTask


# Serializers define the API representation.
class TaskTmplSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskTmpl
        fields = ['alias', 'input']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'input', 'status', 'progress', 'output', 'created_time']
        extra_kwargs = {
            'status': {'read_only': True},
            'progress': {'read_only': True},
            'id': {'read_only': True},
            'created_time': {'read_only': True},
            'output': {'read_only': True}
        }


# ViewSets define the view behavior.
class TaskTmplViewSet(viewsets.ModelViewSet):
    queryset = TaskTmpl.objects.all()
    serializer_class = TaskTmplSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        resp = super(TaskViewSet, self).create(request, *args, **kwargs)
        task_id = resp.data['id']

        t = Thread(target=PythonTask.start, args=(task_id, resp.data['input']))
        t.start()
        return resp
