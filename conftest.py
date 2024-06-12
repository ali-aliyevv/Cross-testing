import pytest

@pytest.fixture()
def logo():
   return "div.logo__icon"

@pytest.fixture()
def login_form():
   return "div.login-form"

@pytest.fixture()
def er1():
   return "300px"

@pytest.fixture()
def er2():
   return "175px"

@pytest.fixture()
def er3():
   return "rgba(0, 0, 0, 0)"

@pytest.fixture()
def passdiv():
   return '//*[@id="app"]/div[1]/div[2]/div[4]/div/div[1]/div/div[3]/form/div[1]/div[2]'

@pytest.fixture()
def maildiv():
   return '//*[@id="app"]/div[1]/div[2]/div[4]/div/div[1]/div/div[3]/form/div[1]/div[3]/div[1]'

@pytest.fixture()
def domain():
   return '//*[@id="app"]/div[1]/div[2]/div[4]/div/div[1]/div/div[3]/form/div[1]/div[3]/div[3]'

@pytest.fixture()
def nextbtn():
   return '//*[@id="app"]/div[1]/div[2]/div[4]/div/div[1]/div/div[3]/form/div[2]/a'

@pytest.fixture()
def er4():
   return "372px"

@pytest.fixture()
def er5():
   return "40px"

@pytest.fixture()
def er6():
   return "133.688px"

@pytest.fixture()
def er7():
   return "40px"

@pytest.fixture()
def er8():
   return "133.688px"

@pytest.fixture()
def er9():
   return "40px"

@pytest.fixture()
def er10():
   return "sans-serif"

@pytest.fixture()
def er11():
   return "14.4px"