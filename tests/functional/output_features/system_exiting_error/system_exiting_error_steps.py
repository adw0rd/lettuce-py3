# -*- coding: utf-8 -*-
from lettuce import step

@step('a system-exiting error is raised')
def raise_system_exiting_error(step):
    raise KeyboardInterrupt
