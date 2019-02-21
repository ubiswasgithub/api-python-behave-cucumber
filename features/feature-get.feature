Feature: Validate API endpoints for get book and author details

Background:
	Given Set basic web application url is "http://192.168.99.100:8080/api/"


Scenario: GET authorList
  Given Set "GET" api endpoint as "authors"
  When Set HEADER param request content type as "application/json"
	And Set HEADER param response accept type as "application/json"
	And Raise "GET" HTTP request
  Then Valid HTTP response should be received
	And Response http code should be 200
	And Response HEADER content type should be "application/json"
	And Response BODY should not be null or empty


Scenario: GET bookList
  Given Set "GET" api endpoint as "books"
  When Set HEADER param request content type as "application/json"
	And Set HEADER param response accept type as "application/json"
	And Raise "GET" HTTP request
  Then Valid HTTP response should be received
	And Response http code should be 200
	And Response HEADER content type should be "application/json"
	And Response BODY should not be null or empty


Scenario: GET singleAuthorDetails
  Given Set "GET" api endpoint as "authors/"
	And Set "Author" id is 1 and operation is "GET"
  When Raise "GET" HTTP request
  Then Valid HTTP response should be received
	And Response http code should be 200
	And Response HEADER content type should be "application/json"
	And Response BODY should not be null or empty


Scenario: GET singleBookDetails
  Given Set "GET" api endpoint as "books/"
	And Set "book" id is 1 and operation is "GET"
  When Raise "GET" HTTP request
  Then Valid HTTP response should be received
	And Response http code should be 200
	And Response HEADER content type should be "application/json"
	And Response BODY should not be null or empty





