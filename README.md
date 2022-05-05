# Edit_Pad_Selenium
Program to open Firefox browser using selenium and navigate to the editpad website.

#### Commands to get started:  
- *sudo apt install python3.8-venv* ➜ To install venv package globally.  
- *python3 -m venv ~/directory_of_project/* ➜ To create a virtual environment in the specified directory.
- *sudo apt install python3-pip* ➜ To install pip package manager globally.
- *pip install objectpath* ➜ To install objectpath package after activating venv.
- *pip install selenium* ➜ To install selenium package after activating venv.


Activating virtual environment such that the program gets executed through the environment:  
- *source "project_directory/venv/bin/activate"*

To deactivate:  
- *deactivate*

**Note:**
> Change VSCode interpreter to the version of Python in the venv.  
> Do not use sudo command to install packages after activating venv using pip.  
> Firefox webdriver i.e. *[geckodriver](https://github.com/mozilla/geckodriver/releases)* is needed in the project folder to launch an instance of the browser.
