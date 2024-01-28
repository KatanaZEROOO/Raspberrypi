#!/bin/bash

REPO_DIR="/home/katana/Raspberrypi"
FILE_NAME="blockpost.py"

{
    echo "Starting update: $(date)"

    check_internet() {
        wget -q --spider http://google.com
        return $?
    }

    cd "$REPO_DIR"

    if check_internet; then
        echo "Internet is available, updating file $FILE_NAME..."
        git fetch
        git checkout origin/main -- "$FILE_NAME"
    else
        echo "Internet is not available."
    fi

    echo "Update finished: $(date)"
}
