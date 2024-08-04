#!/usr/bin/python3
#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics """

import sys

if __name__ == '__main__':
    filesize = 0
    count = 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats, filesize):
        print("File size: {}".format(filesize))
        for code in sorted(stats.keys()):
            if stats[code] > 0:
                print("{}: {}".format(code, stats[code]))

    try:
        for line in sys.stdin:
            count += 1
            parts = line.split()
            try:
                status_code = parts[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except IndexError:
                pass
            try:
                filesize += int(parts[-1])
            except (IndexError, ValueError):
                pass
            if count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
