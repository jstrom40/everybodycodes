#!/bin/bash

# Define the source folder name and the new destination folder name
SOURCE_FOLDER="/Users/josh.stromgren/repos/fun/everybodycodes/template"
DEST_FOLDER="day$1"

# Check if the source folder exists
if [ -d "$SOURCE_FOLDER" ]; then
    # Copy the source folder to the destination, creating the new folder
    cp -r "$SOURCE_FOLDER" "$DEST_FOLDER"
    echo "Folder '$SOURCE_FOLDER' copied to '$DEST_FOLDER'."
    
    # Change the current directory into the new folder
    cd "$DEST_FOLDER" || { echo "Failed to change directory."; exit 1; }
    echo "Now in directory: $(pwd)"

else
    echo "Error: Source folder '$SOURCE_FOLDER' not found."
    exit 1
fi
