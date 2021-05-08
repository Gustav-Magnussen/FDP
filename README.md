# FDP
GitHub page for my practical examples implementation of alternative methods for user authentication. This is part of my final degree project titled: Alternative methods of user authentication and development of practical examples. It contains a two implementation of alternative methods for user authentication: a graphical implementation and a biometric implementation.

## General Dependencies

In order for the two implementations to function properly python 3.7 has to be installed and a number of python packages has to be acquired. The program uses the following packages that come with a default installation of python:

* Os
* sys
* sqlite3

## Graphical Implementation

This implementation can be found in the following [folder](https://github.com/Gustav-Magnussen/FDP/tree/main/graphical) and includes the necessary files to run the [program](https://github.com/Gustav-Magnussen/FDP/blob/main/graphical/graphicalPassword_3.py) that showcases a practical example of user authentication by utilizing a graphical password. This program is designed for python 3.7.

### Features

* A graphical password implementation.
* sqlite3 database of users.
* Ability to add additional users.
* A example of graphical user authentication for educational purposes.

### Dependencies

Attached is a scripted called [dependencies.sh](https://raw.githubusercontent.com/Gustav-Magnussen/FDP/main/dependencies.sh), this can be used to install the necessary python packages on a Linux Ubuntu environment. These are:

* argon2-cffi
* python3-tk

The [argon2-cffi](https://pypi.org/project/argon2-cffi/) package is used in order to hash the graphical passwords. [Python3-tk](https://docs.python.org/3/library/tkinter.html) is used as to display graphical elements in the program. These packages can be installed using the following command in a python environment:

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

This implementation can be found in the following [folder](https://github.com/Gustav-Magnussen/FDP/tree/main/biometric), it includes the program [biometric.py](https://github.com/Gustav-Magnussen/FDP/blob/main/biometric/biometric.py) that showcases a practical example of user authentication using fingerprint scans. This program is designed for python 3.7 on a Windows 10 machine.

### Features

* A fingerprint scann implementation.
* A example of biometric user authentication for educational purposed.

### Dependencies 

In order for the attached [program](https://github.com/Gustav-Magnussen/FDP/blob/main/biometric/biometric.py) to function properly it needs to be execute on a Windows 10 machine where Windows Hello Fingerprint is implemented. For this project testing has been done using the fingerprint scanner [Kensington verimark](https://www.kensington.com/software/verimark-setup/verimark-setup-guide/). However, most fingerprint scanners that are able to be used in accordance with Windows Hello Fingerprint is compatible. 

The [Python3-tk](https://docs.python.org/3/library/tkinter.html) is used as to display graphical elements in the program and can be installed using this command in a python enviroment:

```
>>>import tkinter
```

For compatability with Windows Hello Fingerprint iuspock's [script](https://github.com/luspock/FingerPrint) is used. This can be downloaded from the [GitHub page](https://github.com/luspock/FingerPrint/blob/master/fingerprint.py). The fingerprint.py file has to be located in the same folder as the [program](https://github.com/Gustav-Magnussen/FDP/blob/main/biometric/biometric.py) or the line that imports the fingerprint modules has to be alter to match the correct path. This file also has to be alterd in order to function with the implementation. This can be done by either removing or commenting out the following lines from the fingerprint.py program:

```python
225 if __name__ == '__main__':
226    myFP = FingerPrint()
227    try:
228        myFP.open()
229        # myFP.identify()
230        print("Please touch the fingerprint sensor")
231        if myFP.verify():
232            print("Hello! Master")
233        else:
234            print("Sorry! Man")
235    finally:
236        myFP.close()
```

### Author
* [Gustav Martin Kvilhaug Magnussen](https://github.com/Gustav-Magnussen)
