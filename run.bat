pytest -vs -m "regression" --browser chrome
rem pytest -vs -m "sanity"--browser chrome

rem pytest -vsk log  testCases/test_login.py --browser chrome
pytest -vsk log  testCases/test_login.py --browser firefox


