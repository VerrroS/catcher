#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
#use_plugin("python.coverage")


name = "catcher"
default_task = "publish"


@init
def set_properties(project):
    project.set_property("dir_source_main_python", "main")
    project.set_property("dir_source_unittest_python", "test")
    project.set_property("dir_source_main_scripts", ".")
    project.set_property("dir_docs", ".")
