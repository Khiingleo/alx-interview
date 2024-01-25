#!/usr/bin/python3
"""
script that reads the stdin line by line and then computes the metrics
"""
import sys


line_counted = 0
total_size = 0
status_dict = {200: 0, 301: 0, 400: 0, 401: 0,
               403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        try:
            line = line[:-1]
            parts = line.split(' ')
            total_size += int(parts[-1])
            status_code = int(parts[-2])
            if status_code in status_dict:
                status_dict[status_code] += 1
        except Exception:
            pass

        if line_counted % 10 == 0:
            print(f"File size: {total_size}")
            for code, count in sorted(status_dict.items()):
                if count > 0:
                    print(f"{code}: {count}")

except KeyboardInterrupt:
    print(f"\nFile size: {total_size}")
    for code, count in sorted(status_dict.items()):
        if count > 0:
            print(f"{code}: {count}")

print(f"\nFile size: {total_size}")
for code, count in sorted(status_dict.items()):
    if count > 0:
        print(f"{code}: {count}")
