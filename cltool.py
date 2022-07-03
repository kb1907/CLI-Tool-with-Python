import os
import sys
import subprocess


def main(file):
    gb_size = round((os.stat(file).st_size/1024**3), 2)
    rows = int(subprocess.check_output(['wc', '-l', file]).split()[0])
    print(
        f'Size of the {file} : {gb_size} GB\n{file} contains {rows} number of rows')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(
            """
            This command line tool takes
            file name as an argument !
            """
        )
        sys.exit(0)
    file = sys.argv[1]
    main(file)
