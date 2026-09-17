#!/bin/sh

current_h=$(date "+%H")
current_m=$(date "+%M")

remaining_h=$((18 - current_h))
remaining_m=$((60 - current_m))

if [ "$remaining_m" -ne 0 ]; then
  remaining_h=$((remaining_h - 1))
fi

printf "E.g. Current time: $current_h:$current_m."

if [ $((remaining_h > 0)) -eq 1 ]; then
    printf " Work day ends after $remaining_h hours and $remaining_m minutes."
fi

printf "\n"
