#!/bin/sh

if [ "$#" -ne 2 ]; then
   echo "Error: Missing Expected Arguments!"
   echo "Usage: $0 <target_file> <target_word>"
   exit 1
fi

target_file=$1
target_word=$2

echo "Word \"$target_word\" appears in \"$target_file\" $(grep -c $target_word $target_file) times."
