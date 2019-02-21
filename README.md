# api-python-behave-cucumber

Before running the project, make sure your PC should have installed below dependencies:

#Basic installations:
1. Install Python, if doesn't exists
2. Install npm, if doesn't exists
3. Install pip, if doesn't exists


#Project oriented installations:
1. Install request using the below command
pip install -U requests
2. Install json2html using the below command
pip install -U json2html
3. Install behave using the below command
pip install -U behave
4. Install beahve cucumber using the below command:
pip install -U behave2cucumber
5. Install cumber html reporter for generating reports
npm install cucumber-html-reporter --save-dev

If all above dependencies are installed then run the below commands from project root folder to run the project:

1. behave -f json -o reports/report.json #will create report.json file to reports folder
2.python -m behave2cucumber -i reports/report.json -o reports/cucumber.json -f #will create cucumber.json file from report.json file
3.node reports/html_reporter.js # will generate the report


Or simplay click on the Runner.bat file to execute the above 3 commands.
