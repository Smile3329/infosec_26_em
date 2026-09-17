#!/bin/sh

if [ "$#" -ne 1 ]; then
    echo "Error: Command accepts 1 argument!"
    echo "Usage: $0 <target_dir>"
fi

echo "Successfully deleted: $(find $1 -type f -empty -print -delete | wc -l)"
