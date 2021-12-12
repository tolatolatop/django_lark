from time import sleep

from .models import Task


class TaskWorker(object):
    model = Task

    @classmethod
    def load_task(cls, task_id):
        return cls.model.objects.get(pk=task_id)

    @staticmethod
    def write_result(task, result):
        task.status = 'F'
        task.progress = 100
        task.output = result
        task.save()

    @staticmethod
    def write_expect(task, e):
        task.status = 'E'
        task.progress = 100
        task.output = {'expect': str(e)}
        task.save()

    @classmethod
    def run(cls, *args, **kwargs):
        return {'msg': 'abs task'}

    @classmethod
    def start(cls, task_id, input_data):
        """
        运行 输出结果 修改状态

        :return:
        """
        task = cls.load_task(task_id)
        try:
            result = cls.run(task_id, input_data)
            cls.write_result(task, result)
        except Exception as e:
            cls.write_expect(task, e)


class PythonTask(TaskWorker):

    @classmethod
    def run(cls, task_id, input_data):
        """
        运行 输出结果 修改状态

        :return:
        """
        sleep_time = input_data['time']
        sleep(sleep_time)
        return {'msg': 'ok!'}
