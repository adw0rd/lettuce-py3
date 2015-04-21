from lettuce import step, world

@step('this test step passes')
def this_test_step_passes(step):
    assert True

@step('(.*) squared is (.*)')
def val1_squared_is_val2(step, val1, val2):
    pass
