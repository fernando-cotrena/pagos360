<p align="center">
 <img src="https://i.imgur.com/rSyq3MW.png" alt="Readme Forward QA"></a>
</p>

<h3 align="center">QA - Pagos 360</h3>


# Organization

> How we will name the suites?
 
test -to identify the file- + _ + login -name of the suite- +  type of file. Ex: test_login.py

> How we pull togheter the suites with the same type -integration, e2e-?

we have the suites separate among files; each file have a name representative of the suites types contained.

> **Let's continue with the important **
# Requirements (Prerequisites)

  [Python](https://www.python.org/downloads/)
  
  [Pip](https://pypi.org/project/pip/)
  
  [Pytest](https://docs.pytest.org/en/6.2.x/getting-started.html)
  
  [Requests](https://docs.python-requests.org/en/master/)
  
  [Reports with pytest](https://pytest-html.readthedocs.io/en/latest/user_guide.html)
 

# How to run tests?


1. Clone the project:
- git clone git@github.com:fernando-cotrena/pagos360.git (ssh)

<hr>

2.  Create the ".env" file use the ".env_template" file as an example

    2.a Load the environment data in the .env file

3. Running test from Console

  2.a Open the terminal from the root of the project

	2.b If not have the pre-requirements installed run:
     xs
  
	2.c Run test: 
	 - python -m pytest . -to run all suites-
	 - python -m pytest test_.py -to run a specific suite-
	 - python -m pytest --template=html1/index.html --report=report.html

<hr>
