function pad(n) { return sprintf("%5s", n) }

function color(str) {
	n = strtonum(str)

	if (n < 10)
		c = green
	else if (n < 100)
		c = yellow
	else
		c = red

	return sprintf("%s%s%s", c, str, normal)
}

# Sorts a key value array by the keys
# Selection sort used, because it was easy to write.
#
# This currently both sorts and prints the array, since
# I couldn't get the external array to keep the sorted order.
function kvsort(arr) {
	# print length(arr)
	i = 0
	for (key in arr) {
		keys[i] = key
		vals[i] = arr[key]
		i++;
	}

	len = length(arr)
	for (j = 0; j < len - 1; j++) {
		imin = j
		for (i = j + 1; i < len; i++) {
			if (keys[i] < keys[imin])
				imin = i
		}

		if (imin != j) {
			# swap(arr[i], arr[imin])
			v = vals[j]
			k = keys[j]

			vals[j] = vals[imin]
			keys[j] = keys[imin]

			vals[imin] = v;
			keys[imin] = k;
		}
	}
	for (i in keys) {
		printf "%s %s\n", color(pad(vals[i])), keys[i]
		# arr[keys[i]] = vals[i]
	}
}

function plural(len) {
	if (len == 1)
		return ""
	else
		return "es"
	}

BEGIN {
	normal = "\x1b[m"
	red    = "\x1b[1;31m"
	green  = "\x1b[1;32m"
	blue   = "\x1b[1;34m"
	yellow = "\x1b[1;33m"
}

{ arr[$1]++ }

END {
	kvsort(arr)

	printf "\nNew mail in %s mailbox%s.\n", color(length(arr)), plural(length(arr)) 
}
