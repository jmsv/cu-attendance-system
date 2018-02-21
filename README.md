# cu-attendance-system
206CDE - Real World Project - 1718JANMAY - Presentation: 2018-03-05 12:00

[![Travis CI](https://travis-ci.com/jamesevickery/cu-attendance-system.svg?token=hXPPRPSZqxVqUVQf6s8p&branch=master)](https://travis-ci.com/jamesevickery/cu-attendance-system#)
[![Discord](https://img.shields.io/discord/405022428905996288.svg)](https://discordapp.com/channels/405022428905996288/405022428905996290)


> __Coventry University Attendance System (cuas) is an alternative attendance management system.__
> Students often forget their student cards, meaning they can't sign in to university lectures. Our proposed system provides an alternative/additional method of signing in using the students' phone cameras for reading QR codes, via the Tracker app. A webapp can also be used by lecturers for monitoring attendance.

---

## Links

- [Google Slides presentation](https://docs.google.com/presentation/d/1FJRiusDUBAOPlAZsN0xIQXuhGP8kQTZpb0YXy6KX1Ec/edit?usp=sharing)
- [Trello](https://trello.com/invite/b/t01Y0sO0/ff42bf7f4e8d08d8d0b28925fed4be98/206cde-8b)
- [Colour scheme](https://material.io/color/#!/?primary.color=007bff&secondary.color=6c757d)

---

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

### Running the Server

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

### Resetting the Database

What was that? You fucked up the database? You fool. Fortunately I do this too tbh and made a script to reset it.

From the `server` directory, run this:

```sh
python database/database_create.py
```

This just drops all the tables and recreates them and adds a bit of example data.

### Running the Android App

To run the Android app, install [Android Studio](https://developer.android.com/studio/index.html). Start Android Studio, and open the `cu-attendance-system/app` project. As the project loads, it prompts you to install all the necassary components.

Build the project, and then run on an emulator or a physical Android device via adb. To run on a physical device, you must first [enable USB debugging](https://developer.android.com/studio/debug/dev-options.html) in the device's settings.
