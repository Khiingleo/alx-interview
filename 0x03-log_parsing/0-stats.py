#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""
import sys


def print_stats(status_dict, total_size):
    """prints the file size and stats for every 10 loops"""

    print("File size: {}".format(total_size))
    for key, val in sorted(status_dict.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_size = 0
status_code = 0
line_count = 0
status_dict = {"200": 0, "301": 0, "400": 0, "401": 0,
               "403": 0, "404": 0, "405": 0, "500": 0}


try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            line_count += 1

            if line_count <= 10:
                total_size += int(parsed_line[0])
                status_code = parsed_line[1]

                if status_code in status_dict.keys():
                    status_dict[status_code] += 1

            if line_count == 10:
                print_stats(status_dict, total_size)
                line_count = 0

finally:
    print_stats(status_dict, total_size)
