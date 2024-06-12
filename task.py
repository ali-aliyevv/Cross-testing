import pytest
import yaml
from selenium.webdriver.support.color  import Color
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])


def test_logo_width(logo, er1):
    assert site.get_element_property("css", logo, "width") == er1, "Test 1 fail"

def test_logo_height(logo, er2):
    assert site.get_element_property("css", logo, "height") == er2, "Test 2 fail"

def test_form_color(login_form, er3):
    assert site.get_element_property("css", login_form, "background-color") == er3, "Test 3 fail"

def test_pass_width(passdiv, er4):
    assert site.get_element_property("xpath", passdiv, "width") == er4, "Test 4 fail"

def test_pass_height(passdiv, er5):
    assert site.get_element_property("xpath", passdiv, "height") == er5, "Test 5 fail"

def test_email_width(maildiv, er6):
    assert site.get_element_property("xpath", maildiv, "width") == er6, "Test 6 fail"

def test_email_height(maildiv, er7):
    assert site.get_element_property("xpath", maildiv, "height") == er7, "Test 7 fail"

def test_domain_width(domain, er8):
     assert site.get_element_property("xpath", domain, "width") == er8, "Test 8 fail"

def test_domain_height(domain, er9):
     assert site.get_element_property("xpath", domain, "height") == er9, "Test 9 fail"

def test_font_family(nextbtn, er10):
    assert site.get_element_property("xpath", nextbtn, "fontFamily") == er10, "Test 10 fail"

def test_font_size(nextbtn, er11):
    assert site.get_element_property("xpath", nextbtn, "fontSize") == er11, "Test 11 fail"

def teardown():
    site.close()