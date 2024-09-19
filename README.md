
<h1 align="center">A Basic Clock/Timer App</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/mitchellkolb/clock-timer?color=3776AB">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/mitchellkolb/clock-timer?color=3776AB">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/mitchellkolb/clock-timer?color=3776AB">

  <img alt="Github stars" src="https://img.shields.io/github/stars/mitchellkolb/clock-timer?color=3776AB" />
</p>

<p align="center">
<img
    src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"
    alt="Website Badge" />
<img
    src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=Windows 10&logoColor=white"
    alt="Website Badge" />
</p>

This is a Linux designed clock app that combines two features that other clock apps on MacOS and Windows have like custom timer alert sounds and break spaces. Other flathub clock apps have these feature but there is none that have it all in one. That is what this app plans to deliver.

---


# Table of Contents
- [What I Learned](#what-i-learned-in-this-project)
- [Tools Used / Development Environment](#tools-used--development-environment)
- [How to Set Up](#how-to-set-up)
- [Project Overview](#project-overview)


---

# What I Learned in this Project
- How to publish compiled GTK python apps on Flathub
- Programming with a new UI library PyGObject that uses GTK
- Planning and execution of an app from start to finish



# Tools Used / Development Environment
- Python
- PyGObject/GTK
- VS Code
- Terminal
- Linux Mint







# How to Set Up
This project was implemented on my Linux desktop using information from the [PyGOject site](https://pygobject.gnome.org/getting_started.html#ubuntu-getting-started) and this [GTK YouTube Video.](https://youtu.be/Yu2EBmeCpJw?si=1T4h0TMkTJBPFGvC)
- Clone this repository 
- `sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-4.0`
- In the codebase that was cloned create a virtual environment: `python3 -m venv .venv`
- Activate the virtual environment: `source .venv/bin/activate`
- Download External Python Libraries: `pip install -r requirements.txt`
- The program should begin to run: `python3 main.py`






# Project Overview
This project utilizes 



## Project Details


## Technical Plan
The project employs a 


## Files and Structure
- `main.py`: Contains the code


## Future Work
Future improvements could include






--- 
