# FDP
Github page for my praticle examples implementation of alternative methods for user authentication. This is part of my final degree project titled: Alternative methods of user authentication and development of practical examples. It contains a two implementation of alternative methods for user authentication: a graphical implementation and a biometric implementation.

# Graphical implemetation

This implementation can be found in the following [folder](https://github.com/Gustav-Magnussen/FDP/tree/main/graphical) and includes the necessary files to run the a program that showcases a practicle [example] of user authentication by utilizing a graphical password.

### Features

* A graphical password implementation
* sqlite3 database of users
* Ability to add aditional users
* A example of graphical user authentication for educational purposes

### Dependencies

In order for the attached [program](https://raw.githubusercontent.com/Gustav-Magnussen/FDP/main/graphical/graphicalPassword_3.py) to function proparly a number of python packages has to be installed. The program uses the following packages that come with a default installation of python:

* Os
* sys
* sqlite3

Attached is a scripted called [dependencies.sh](https://raw.githubusercontent.com/Gustav-Magnussen/FDP/main/dependencies.sh), this can be used to install the other necessary packages on a Linux Ubuntu enviroment. The other packages that are necessary to run the program are:

* argon2-cffi
* python3-tk

These packages can be installed using the following format:

```
>>>pip install [package]
```

### Installation using script

In order to install features for an ubuntu enviorment the follow commands below can be used on the [dependencies.sh](https://raw.githubusercontent.com/Gustav-Magnussen/FDP/main/dependencies.sh) file:

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
![User entry for account john](https://github.com/Gustav-Magnussen/FDP/blob/main/graphical/images/bob.png)




