# FDP
GitHub page for my practical examples implementation of alternative methods for user authentication. This is part of my final degree project titled: Alternative methods of user authentication and development of practical examples. It contains a two implementation of alternative methods for user authentication: a graphical implementation and a biometric implementation.

## Graphical implementation

This implementation can be found in the following [folder](https://github.com/Gustav-Magnussen/FDP/tree/main/graphical) and includes the necessary files to run the program that showcases a practical [example](https://github.com/Gustav-Magnussen/FDP/blob/main/graphical/graphicalPassword_3.py) of user authentication by utilizing a graphical password. This program is designed for python 3.7.

### Features

* A graphical password implementation
* sqlite3 database of users
* Ability to add additional users
* A example of graphical user authentication for educational purposes

### Dependencies

In order for the attached [program](https://raw.githubusercontent.com/Gustav-Magnussen/FDP/main/graphical/graphicalPassword_3.py) to function properly python 3.7 has to be installed  and a number of python packages has to be acquired. The program uses the following packages that come with a default installation of python:

* Os
* sys
* sqlite3

Attached is a scripted called [dependencies.sh](https://raw.githubusercontent.com/Gustav-Magnussen/FDP/main/dependencies.sh), this can be used to install the other necessary packages on a Linux Ubuntu environment. The other packages that are included  in this script and necessary to run the program are:

* argon2-cffi
* python3-tk

The [argon2-cffi](https://pypi.org/project/argon2-cffi/) package is used in order to hash the graphical passwords. [Python3-tk](https://docs.python.org/3/library/tkinter.html) is used as to display graphical elements in the program.  These packages can be installed using the following command in a python environment:

```
>>>pip install [package]
```

### Installation using script

In order to install features for an Ubuntu environment the follow commands below can be used on the [dependencies.sh](https://raw.githubusercontent.com/Gustav-Magnussen/FDP/main/dependencies.sh) file:

Making the file executable:
```
$ chmod +x dependencies.sh
```
Running the script:
```
$ sudo ./dependencies.sh
```
### Attached test data

Within the program [grapicalPassword.py](https://raw.githubusercontent.com/Gustav-Magnussen/FDP/main/graphical/graphicalPassword_3.py) the lines 25-27 can be uncommented to fill the database that is created with test data for two users: bob and john. This data includes the two accounts with their usernames and argon2 hashed password combinations as seen below:

![User entry for account bob](https://github.com/Gustav-Magnussen/FDP/blob/main/graphical/images/bob.png)
![User entry for account john](https://github.com/Gustav-Magnussen/FDP/blob/main/graphical/images/john.png)

If this feature is to be used these lines also needs to be removed from the program after the first execution of the program in order to not create duplicate entries.

### Register program

The file [register.py](https://github.com/Gustav-Magnussen/FDP/blob/main/graphical/register_2.py) is invoked within the main program when clicking the register user button. It can also be used as a execute on its own and is capable of adding user accounts. 

## Biometric implementation

### Author
* [Gustav Martin Kvilhaug Magnussen](https://github.com/Gustav-Magnussen)
