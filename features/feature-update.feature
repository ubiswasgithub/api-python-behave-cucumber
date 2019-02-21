Feature: Validate API endpoints for update books, authors
Scenario: Update a Author details
  Given Set "PUT" api endpoint as "authors/"
	And Set "Author" id is 69 and operation is "PUT"
  When Set HEADER param request content type as "application/json"
	And Set HEADER param response accept type as "application/json"
	And Modify Author name as "Rai", email as "test6@gmail.com" and mobile as "12357464747" and author id is 69
	And Raise "PUT" HTTP request
  Then Valid HTTP response should be received
	And Response http code should be 200
	And Response HEADER content type should be "application/json"
	And Response BODY should not be null or empty