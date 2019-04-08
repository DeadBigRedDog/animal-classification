Initial Setup
-------------

To read this document in html, `CMD + Shift + P` > `Markdown: Open Preview`.

* Create the virtual environment: `python3 -m venv .pyenv`
* Activate the virtual environment: `source commands/activate`
* Install dependencies: `pip install -r requirements/base.txt`


Visual Studio Code
------------------
Install the python extension.

Next you should set up your Visual Studio Code to recognize the virtual environment:

* `Cmd + Shift + P > Python: Select Interpreter`. Choose the `python` that's in your `.pyenv` folder.

Pylint is a little bit fussy with Django. I've found some workarounds. It's probably a good idea to 
enable linting.


