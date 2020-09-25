#!/bin/sh




while getopts ":a:e:pt" opt; do
  case $opt in
    a) algo="$OPTARG"
    ;;
    e) path="$OPTARG"
    ;;
    p) distance="True"
    ;;
    t) time="True"
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
    ;;
  esac
done

python3 ./main.py --path "$path" --time "$time" --algo "$algo" --distance "$distance"


#printf "%s\n" "$distance"