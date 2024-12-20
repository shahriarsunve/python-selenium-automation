from behave import given, when, then


@given('Open Target App page')
def open_target_app(context):
    context.app.target_app_page.open_target_app()


@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.target_app_page.get_current_window_handle()


@when('Click Privacy Policy link')
def click_pp_link(context):
    context.app.target_app_page.click_pp_link()


@when('Switch to new window')
def switch_window(context):
    # print('All windows', context.driver.window_handles) # [Win1, Win2, ...]
    # context.driver.switch_to.window(context.driver.window_handles[1])
    context.app.target_app_page.switch_to_new_window()


@then('Verify Privacy Policy page opened')
def verify_pp_opened(context):
    context.app.privacy_policy_page.verify_pp_opened()


@then('Close current page')
def close_page(context):
    context.app.privacy_policy_page.close()


@then('Return to original window')
def return_to_window(context):
    context.app.privacy_policy_page.switch_to_window_by_id(context.original_window)