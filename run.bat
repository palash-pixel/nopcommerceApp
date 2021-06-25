rem rerem pytest -vs -m "regression" --browser chrome
pytest -vs -m "sanity"--browser chrome

rem pytest -vsk log  testCases/test_login.py --browser chrome
rem pytest -vsk log  testCases/test_login.py --browser firefox


