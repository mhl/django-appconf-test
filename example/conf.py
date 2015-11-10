from django.conf import settings  # noqa

from appconf import AppConf


class ExampleExtraConf(AppConf):

    print "importing ExampleExtraConf"

    MY_EXTRA_SETTING = 'foo'
