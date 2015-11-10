from django.conf import settings  # noqa

from appconf import AppConf


class ExampleExtraConf(AppConf):
    MY_EXTRA_SETTING = 'foo'
