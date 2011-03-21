================
python-smartpass
================

 This is a Python library to interact with Trapeze Smart Pass. 

 Example of use::
	smartpass = SmartPass(SMARTPASS_USERNAME, SMARTPASS_PASSWORD, SMARTPASS_URL)
        smartpass.add_guest(username, password = password, person_name = name)

 Right now all it can do is add a guest. A fuller support of the API should follow in the future.
