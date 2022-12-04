#!/usr/bin/env python3
import os
import re
import logging
import time

###########################################
# Please configure these global variables #
###########################################

# Configure the location of the picures
ROOTDIR = '/Users/<your name>/Pictures/'

# Configure the name of edited filed appended to their name
# For example "20220101-edited.jpg"
# or "super_document - copy.pdf"
# This will only keep the copy with your suffix, not the original
# Note : it isn't necessary to append the full word,
# only the last part of the filename before the extension
# is required
SUFFIX = r"-edited"

# Configure logging level, in order : 
# DEBUG < INFO < WARNING < ERROR < CRITICAL
# Recommended : logging.INFO
LOGGING_LEVEL = logging.INFO

########################################
# The rest works without configuration #
########################################

PATTERNINIT = r".+?(?=" + SUFFIX + r")"
PATTERNEXT = r".+?" + SUFFIX + r"(\..+)"

editedFilenames = []
deletedCount = 0

# Setup logger
logging.basicConfig(
    format="%(asctime)s [%(levelname)7s] :: %(message)s",
    level=LOGGING_LEVEL,
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Searching for all files with suffix, not taking in account subdirs or dirs
for subdir, dirs, files in os.walk(ROOTDIR):
    for file in files:
        logging.info("File found : %s", file)
        if re.search(PATTERNINIT, file):
            fileTmp = re.match(PATTERNINIT, file).group(0) + re.match(PATTERNEXT, file).group(1)
            print(fileTmp)
            editedFilenames.append(fileTmp)
    break

# Confirmation
logging.warning("%s files with the '%s' suffix.", len(editedFilenames), SUFFIX)
logging.warning("Running full deletion in 4 seconds. Press CTRL+C to cancel.")
time.sleep(4)

# Deleting everything
for editedFilename in editedFilenames:
    try:
        os.remove(ROOTDIR + editedFilename)
        deletedCount += 1
        logging.debug(
            "Deleted : %s", editedFilename
        )
    except KeyboardInterrupt:
        logging.error(
            "Deletion cancelled with keyboard interrupt"
        )
        break
    except FileNotFoundError:
        logging.debug(
            "Not found : %s ", editedFilename
        )

logging.warning("%d/%d deleted files.", deletedCount, len(editedFilenames))
