# cu-attendance-system
206CDE - Real World Project - 1718JANMAY

[![Travis CI](https://travis-ci.com/jamesevickery/cu-attendance-system.svg?token=hXPPRPSZqxVqUVQf6s8p&branch=master)](https://travis-ci.com/jamesevickery/cu-attendance-system#)

> __Coventry University Attendance Tracker is an app that will help with attendance monitoring.__
> Students often forget their student cards, meaning they can't sign in to university lectures. Our proposed system provides an alternative method of signing in using their phone's camera for reading QR codes.

## Getting Started

### Prerequisites

#### Windows:

[Install Python 2.7](https://www.python.org/downloads) if you haven't already got it. The Python executable must be available in your PATH environment variable; if you can't already run `python` from Command Prompt, you might need to [add it yourself](https://superuser.com/a/143121/526390). Check this works but opening a Command Prompt (right click start, hit 'Command Prompt') and enter '`python`'. <kbd>Ctrl+C</kbd> closes Python.

#### The Better OS:

On Linux, in this case Ubuntu, `sudo apt-get install python python-dev python-pip` should get everything you need. Test in a shell by running `python`, with <kbd>Ctrl+D</kbd> to exit. See how much easier that was? yeah Windows sucks.

#### virtualenv

You also need Python's `virtualenv` package. Install (in an admin Command Prompt, or using sudo on Linux) using:

```sh
python -m pip install virtualenv
```

### Running the server

You've got Python set up and you can run it from a command line? It's all rainbows and blue skies from here. This bit assumes you're already in the directory you've cloned the repo to. On my Windows PC, it's this: `C:\Users\James\gitr\cu-attendance-system`.

First, hop into the server directory:

```sh
cd server
```

Then set up a Python virtual environment: Sounds scary at first, but it's just a box that Python installs packages to.

```sh
python -m virtualenv venv
```

Activate the virtualenv. This just tells the current cmd/shell session to use the virtual environment instead of the global Python packages. On Windows:

```
venv\Scripts\activate.bat
```

or on Linux/Mac:

```sh
source venv/bin/activate
```

Now you're in the venv, install all the packages the server program needs. I made this easier by supplying a magic requirements file:

```sh
python -m pip install -r requirements.txt
```

Everything is ready! Now all you have to do is run the server file: Running this file directly puts in in debug mode.

```sh
python server.py
```

To test, open to a browser and go to http://localhost:5000/api/hello. If you've got a friendly message saying "hello", the server is working! Go to http://localhost:5000 to see the site running.

As you make changes to `server.py` or any of the module files, it should automatically restart, applying the changes. Updating stuff on the site often requires a <kbd>Ctrl+F5</kbd> (hard refresh) in the browser.

_Enjoy, love James x_
