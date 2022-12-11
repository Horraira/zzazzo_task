from django.apps import AppConfig
from oscar.core.application import OscarConfig
from django.urls import path, re_path
from oscar.core.loading import get_class


# class TaskConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'task'


class TaskConfig(OscarConfig):
    name = 'task'
    namespace = 'task'

    def ready(self):
        super().ready()
        self.data_list_view = get_class(
            'task.views', 'TaskListView')
        self.data_input_view = get_class(
            'task.views', 'PurchaseDetailsAddView')

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('', self.data_list_view.as_view(), name='index'),
            path('addReport/', self.data_input_view.as_view(), name='addData'),
        ]
        return self.post_process_urls(urls)
