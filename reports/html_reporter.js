var reporter = require('cucumber-html-reporter');
 
var options = {
        theme: 'bootstrap',
        jsonFile: 'reports/cucumber.json',
        output: 'reports/cucumber_report.html',
        reportSuiteAsScenarios: true,
        launchReport: true,
        screenshotsDirectory: 'screenshots/',
        storeScreenshots: true,
        brandTitle:'api-python-cucumber-behave-test',
        name:'Api-acceptance-test-report',
        metadata: {
            "App Version":"0.3.2",
            "Test Environment": "STAGING",
            "Browser": "Chrome  54.0.2840.98",
            "Platform": "Windows 10",
            "Parallel": "Scenarios",
            "Executed": "Remote"
        }
    };
 
    reporter.generate(options);