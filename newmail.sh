#!/bin/bash

# TODO re-add support for these flags 

info="1"
totalonly=""

while [ "$1" ]; do
	case $1 in
		-s|--silent) info="" ;;
		-h|--help)
			cat <<- EOF
			Source located at $(realpath $0), read that.
			EOF
			exit
			;;
		-t|--total)
			totalonly="1"
			info=""
			;;
	esac;
	shift
done

find ~/mail -type f \
	| grep -oP '(?<=mail/)[^/]+/[^/]+(?=/new/)' \
	| awk -f $(dirname $(realpath $0))/newmail.awk
