import requests
import json
class background():

    global_general_variables = {}
    http_request_header = {}
    http_request_body = {}
    http_request_url_query_param = {}

    def setBaseUrl(self,basic_app_url):
        self.global_general_variables['basic_application_URL'] = basic_app_url

    def getBaseUrl(self):
        return self.global_general_variables['basic_application_URL']

    def setEndPoint(self, get_api_endpoint, request_type):
        self.global_general_variables[request_type+'_api_endpoint'] = get_api_endpoint

    def getEndPoint(self,http_request_type):
        return self.global_general_variables[http_request_type+'_api_endpoint']

    def setRequestContentType(self, header_content_type):
        self.http_request_header['content-type'] = header_content_type

    def setRequestAcceptType(self, header_accept_type):
        self.http_request_header['Accept'] = header_accept_type

    def setSingleItemEndpoint(self, expected_itemid, opt):
        if (opt == 'PUT'):
            self.global_general_variables[opt+'_api_endpoint'] += str(expected_itemid)
        elif (opt == 'DELETE'):
            self.global_general_variables[opt+'_api_endpoint'] += str(expected_itemid)
        else:
            self.global_general_variables[opt+'_api_endpoint'] += str(expected_itemid)

    def setItemDetails(self, context, item_name, particular, value ):
        for row in context.table:
            temp_value = row['value']
            self.global_general_variables[row['particular']] = temp_value
            if 'empty' in temp_value:
                self.global_general_variables[row['particular']] = ''



    # This function is based on project requirement, not a generalized function...........
    def getItemDetails(self, item_name ):
        temp_request_body = {}
        if(item_name == 'Author'):
            temp_request_body = {
                "name": self.global_general_variables['name'],
                "email": self.global_general_variables['email'].replace('01', '02'),  # some random number
                "mobile": self.global_general_variables['mobile'],
                "address": self.global_general_variables['address']
            }
            return temp_request_body
        elif(item_name == 'Book'):
            temp_request_body =  {
                "title": {
                    "en": self.global_general_variables['english_name'],
                    "bn": self.global_general_variables['bangla_name']
                },
                "description": {
                    "en": self.global_general_variables['english_dsc'],
                    "bn": self.global_general_variables['bangla_dsc']
                },
                "author_id": int(self.global_general_variables['authorid']),
                "image_url": self.global_general_variables['image_link']
            }
            return temp_request_body

    def setRequestBody(self, item_name):
        if(item_name == 'Author'):
            self.http_request_body = self.getItemDetails(item_name)
        elif(item_name == 'Book'):
            self.http_request_body = self.getItemDetails(item_name)


    def updateExistingAuthor(self,new_name, new_mobile,new_email, expected_auhor_id ):
        self.global_general_variables['name'] = new_name
        self.global_general_variables['email'] = new_email
        self.global_general_variables['mobile'] = new_mobile
        self.http_request_body = {
                    "name": self.global_general_variables['name'],
                    "email": self.global_general_variables['email'],  # some random number
                    "mobile": self.global_general_variables['mobile']

                }




    #Request----------
    def handleRequestAndGetResponse(self, http_request_type):
        url_temp = self.getBaseUrl()
        if 'GET' == http_request_type:
            url_temp += self.getEndPoint(http_request_type)
            self.http_request_body.clear()
            self.global_general_variables['response_full'] = requests.get(url_temp, headers=self.http_request_header,
                                                                     params=self.http_request_url_query_param,
                                                                     data=self.http_request_body)
        elif 'POST' == http_request_type:
            url_temp += self.getEndPoint(http_request_type)
            self.http_request_url_query_param.clear()
            self.global_general_variables['response_full'] = requests.post(url_temp,
                                                                      headers=self.http_request_header,
                                                                      params=self.http_request_url_query_param,
                                                                      data=json.dumps(self.http_request_body))
        elif 'PUT' == http_request_type:
            url_temp += self.getEndPoint(http_request_type)
            self.http_request_url_query_param.clear()
            self.global_general_variables['response_full'] = requests.put(url_temp,
                                                                           headers=self.http_request_header,
                                                                           params=self.http_request_url_query_param,
                                                                           data=json.dumps(self.http_request_body))
        elif 'DELETE' == http_request_type:
            url_temp += self.getEndPoint(http_request_type)
            self.http_request_url_query_param.clear()
            self.global_general_variables['response_full'] = requests.delete(url_temp,
                                                                          headers=self.http_request_header,
                                                                          params=self.http_request_url_query_param,
                                                                          data=json.dumps(self.http_request_body))


    #validation-------------------
    def validateResponseIsRecieved(self):
        if None in self.global_general_variables['response_full']:
            assert False, 'Null response received'

    def validateCorrectResponseCodeIsReceived(self,expected_response_code):
        self.global_general_variables['expected_response_code'] = expected_response_code
        actual_response_code = self.global_general_variables['response_full'].status_code
        if str(actual_response_code) not in str(expected_response_code):
            print(str(self.global_general_variables['response_full'].json()))
            assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)

    def validateCorrectResponseContentTypeIsRecieved(self,expected_response_content_type):
        self.global_general_variables['expected_response_content_type'] = expected_response_content_type
        actual_response_content_type = self.global_general_variables['response_full'].headers['Content-Type']
        if expected_response_content_type not in actual_response_content_type:
            assert False, '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type

    def validateResponseBodyIsNotNull(self):
        if None in self.global_general_variables['response_full']:
            assert False, '***ERROR:  Null or none response body received'