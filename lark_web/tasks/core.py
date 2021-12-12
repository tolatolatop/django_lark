from time import sleep

from .models import Task


class PythonTask(object):

    @staticmethod
    def run(task_id, input_data):
        """
        运行 输出结果 修改状态

        :return:
        """
        task = Task.objects.get(pk=task_id)
        try:
            sleep_time = input_data['time']
            sleep(sleep_time)
            task.status = 'F'
            print('task', task_id, 'is finished')
        except Exception as e:
            task.status = 'E'
            print(e)
        task.save()
