from behave import *

use_step_matcher("re")


@when("I open the register website")
def step_impl(context):
    context.driver.get('https://login.taobao.com/member/login.jhtml')


@then('I expect that the title is "([^"]*)"')
def step_impl1(context, title_name):
    title = context.driver.title
    assert title_name in title

# @when("I click with jump_button")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: When I click with jump_button')
#
#
# @step("I set with username '18771917218'")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: And I set with username \'18771917218\'')
#
#
# @step("I set with password 'laobalaoma7272'")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: And I set with password \'laobalaoma7272\'')
#
#
# @step("I click with login_button")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: And I click with login_button')
#
#
# @then("I expect that text '待定'")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: Then I expect that text \'待定\'')
