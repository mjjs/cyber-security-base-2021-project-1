# Cyber Security Base 2021 Project 1

This is a simple project for the University of Helsinki's Cyber Security Base 2021 Project 1.
The application is a simple messaging wall that supports:
* Registering
* Logging in/out
* Posting a message to the wall
* Handling users via the /admin endpoint

The idea of the project is to incorporate five different security flaws from the [OWASP Top Ten](https://owasp.org/www-project-top-ten/) list.

## Running
Here we assume the user has `python3` and `pip3` installed and in their path.

```sh
# 1. Clone the repository
$ git clone https://github.com/mjjs/cyber-security-base-2021-project-1

# 2. Create a veirtual environment.
# This step is not mandatory, but recommended not to pollute the global environment with packages.
$ python3 -m venv name-for-virtual-env && source name-for-virtual-env/bin/activate

# 3. Inside the project folder, install the dependencies.
$ pip3 install -r requirements.txt

# 4. Inside the src folder, run the application.
$ python3 app.py
```

## Flaws
The flaws implemented in this project are described in the [essay.txt](essay.txt) file.
