# -*- coding:utf-8 -*-

import sys
import re

# *******************************
# * Main
# *******************************
def main():
    # input file
    if len(sys.argv) < 2:
        print('Please input the file name: ')
        input_file_name = sys.stdin.readline().rstrip()
    else:
        input_file_name = sys.argv[1]

    # create output file
    output_file_name = re.sub(r'(\.[^\.]+$', r'_result\1', input_file_name)    # insert '_result' before the last period
    output_file = open(output_file_name, 'w')
    output_file.close()
    output_file = open(output_file_name, 'a')

    # read input file and write into output file
    print('Writing into ' + outpu_file_name)
    fp = open(input_file_name)
    for line in fp:
        tag_file_name, line_num, dummy = re.split('[\(\)]', line)
        content = get_tag_content(tag_file_name, line_num)
        output_file.write(line.rstrip('\n') + ':' + content)

    print('Complete!')
    print('Cleaning...')
    fp.close()
    output_file.close()
    print('Bye!')


# *******************************
# * Internal Functions
# *******************************
def get_tab_content(file_name, linu_num):
    ret = ''
    fp = open(file_name)
    for idx, line in enumerate(fp):
        if (idx + 1) == int(line_num):
            ret = line
            break

    fp.close()
    return ret

if __nam__='__main__':
    main()

