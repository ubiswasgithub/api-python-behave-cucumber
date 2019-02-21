Feature: Validate API endpoints for add books, add authors
Background:
	Given Set basic web application url is "http://192.168.99.100:8080/api/"
Scenario: Add Author
  Given Set "POST" api endpoint as "authors"
	And Set basic "Author" details as "<particular>" and "<value>" below
	|particular|value|
	|name|Martin|
	|email|martin@telenorhealth.com|
	|mobile|01793456745|
	|address|test address for tester|
  When Set HEADER param request content type as "application/json"
	And Set HEADER param response accept type as "application/json"
	And Set BODY form param using basic "Author" details
	And Raise "POST" HTTP request
  Then Valid HTTP response should be received
	And Response http code should be 200
	And Response HEADER content type should be "application/json"
	And Response BODY should not be null or empty


Scenario: Add book
  Given Set "POST" api endpoint as "books"
	And Set basic "Book" details as "<particular>" and "<value>" below
	|particular|value|
	|english_name|The bengal tiger history|
	|bangla_name|The bengal bag history|
	|english_dsc|nature of english|
	|bangla_dsc|nature of bangla    |
	|authorid|1|
	|image_link|test.jpg |
  When Set HEADER param request content type as "application/json"
	And Set HEADER param response accept type as "application/json"
	And Set BODY form param using basic "Book" details
	And Raise "POST" HTTP request
  Then Valid HTTP response should be received
	And Response http code should be 200
	And Response HEADER content type should be "application/json"
	And Response BODY should not be null or empty