Feature: Validate API endpoints for delete books, authors
Background:
	Given Set basic web application url is "http://192.168.99.100:8080/api/"
Scenario: Delete a author
  Given Set "DELETE" api endpoint as "authors/"
	And Set "Author" id is 1 and operation is "DELETE"
  When Set HEADER param request content type as "application/json"
	And Set HEADER param response accept type as "application/json"
	And Raise "DELETE" HTTP request
  Then Valid HTTP response should be received
	And Response http code should be 200
	And Response HEADER content type should be "application/json"
	And Response BODY should not be null or empty