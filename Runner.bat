behave -f json -o reports/report.json &
python -m behave2cucumber -i reports/report.json -o reports/cucumber.json -f &
node reports/html_reporter.js &
pause