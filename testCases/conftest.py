import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
#from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
from datetime import datetime

@pytest.fixture()
def setup(browser):
    #driver = None
    if browser == "firefox":
        service_obj = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service_obj)

    elif browser == "edge":
        # service_obj = Service(EdgeChromiumDriverManager().install())
        # driver = webdriver.Edge(service=service_obj)
        ##driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge()

    else:
        #service_obj = Service(ChromeDriverManager().install())
        ##service_obj = Service(ChromeDriverManager(cache_valid_range = 0).install())
        #driver = webdriver.Chrome(service=service_obj)
        ops = webdriver.ChromeOptions()
        ops.add_argument('--disable-notifications')
        driver = webdriver.Chrome(options=ops)
    driver.implicitly_wait(10)
    return driver

# Add --browser parser and send browser name to setup() method
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

############PyTest HTML Report############

# Hook to add html report title
def pytest_html_report_title(report):
    report.title = "Automation Test Report"

# Hook to update html results summary
def pytest_html_results_summary(prefix,summary,postfix):
    prefix.extend([
        "Project Name: Test Project",
        "Module Name: Register Module",
        "Tester Name: Prashant"
    ])

# Hook to update metadata
def pytest_metadata(metadata, config):
    metadata.pop("JAVA_HOME",None)
    metadata["Project Name"] = 'Automation Exercise'
    metadata["Browser"] = config.getoption("--browser")

# Specifying html report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir+"\\reports\\"+datetime.now().strftime("%Y%m%d-%H%M%S")+".html")

