# Remove original files from edited/copied ones
![Passing test](https://img.shields.io/github/checks-status/timothechauvet/remove-unsuffixed-files/main?label=passing%20test&logo=python&logoColor=white)
![Repository Size](https://img.shields.io/github/languages/code-size/timothechauvet/remove-unsuffixed-files)
![Contributors](https://img.shields.io/github/contributors-anon/timothechauvet/remove-unsuffixed-files)
![Last Commit](https://img.shields.io/github/last-commit/timothechauvet/remove-unsuffixed-files)

![Cover Remove suffix duplicates with the Python logo](./.github/gh_cover.png)

Small Python program I wrote to remove unedited files taken from the Google Photos dump of my mom, containing two copies of edited AND unedited files. Turns out it's also useful for removing originals from copied files

## Purpose
Google Takeout backups provide both edited and unedited versions of the same picture. The same picture can have a suffix "-edited" attached to it, before the .png or .jpg extension. This tools aims to remove the original versions to keep only the one with the suffix, using basic regex commands

<img src="./.github/edited_example.png" alt="Illustration of edited pictures with the unedited versions" width="300px"/>

## Setup
Edit the following lines of `unedited_removal.py` :
```python
# Configure the location of the picures
ROOTDIR = '/Users/<your name>/Pictures/'

# Configure the name of edited filed appended to their name, or 'suffix'
SUFFIX = r"-edited"

# Optional : Configure the logging level, in order of criticity
# DEBUG < INFO < WARNING < ERROR < CRITICAL
LOGGING_LEVEL = logging.INFO
```

## Run the program
On Linux or Mac, set the execution flag `chmod +x unedited_removal.py` whithin a command line, then run the program with `python3 unedited_removal.py` or simply `python unedited_removal.py` if python3 doesn't work.

If you need to install Python, [follow this link](https://www.python.org/downloads/).

## Regex
The main regexes behind the program is as follows :
```python
SUFFIX = "-edited"
BEFORE_THE_SUFFIX = r".+?(?=" + SUFFIX + r")"
AFTER_THE_SUFFIX = r".+?" + SUFFIX + r"(\..+)"
```

