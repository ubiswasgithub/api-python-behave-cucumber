from behave import given,when, then, step
from steps.BaseAction import *


obj = background()

@given(u'Set basic web application url is "{basic_app_url}"')
def step_impl(context, basic_app_url):
    obj.setBaseUrl(basic_app_url)

@given(u'Set "{request_type}" api endpoint as "{get_api_endpoint}"')
def step_impl(context, get_api_endpoint, request_type):
    obj.setEndPoint(get_api_endpoint,request_type)

@given(u'Set "{item}" id is {expected_itemid:d} and operation is "{opt}"')
def step_impl(context,item, expected_itemid, opt):
    obj.setSingleItemEndpoint(expected_itemid, opt)

@given(u'Set basic "{item_name}" details as "{particular}" and "{value}" below')
def step_impl(context, item_name, particular, value):
    obj.setItemDetails(context, item_name, particular, value)


@when(u'Set HEADER param request content type as "{content_type}"')
def step_impl(context, content_type):
    obj.setRequestContentType(content_type)

@when(u'Set HEADER param response accept type as "{accept_type}"')
def step_impl(context, accept_type):
    obj.setRequestAcceptType(accept_type)

@when(u'Raise "{request_type}" HTTP request')
def step_impl(context, request_type):
    obj.handleRequestAndGetResponse(request_type)


@when(u'Set BODY form param using basic "{item_name}" details')
def step_impl(context, item_name):
    obj.setRequestBody(item_name)

@when(u'Modify Author name as "{new_name}", email as "{new_email}" and mobile as "{new_mobile}" and author id is {expected_auhor_id:d}')
def step_impl(context, new_name, new_mobile,new_email,expected_auhor_id):
    obj.updateExistingAuthor(new_name, new_mobile,new_email, expected_auhor_id)


@then(u'Valid HTTP response should be received')
def step_impl(context):
    obj.validateResponseIsRecieved()



@then(u'Response http code should be {expected_response_code:d}')
def step_impl(context, expected_response_code):
    obj.validateCorrectResponseCodeIsReceived(expected_response_code)


@then(u'Response HEADER content type should be "{expected_response_content_type}"')
def step_impl(context, expected_response_content_type):
    obj.validateCorrectResponseContentTypeIsRecieved(expected_response_content_type)


@then(u'Response BODY should not be null or empty')
def step_impl(context):
    obj.validateResponseBodyIsNotNull()
