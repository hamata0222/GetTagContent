# -*- coding:utf-8 -*-

import sys
import re
import os

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
    output_file_name = re.sub(r'(\.[^\.]+)$', r'_result\1', input_file_name)    # insert '_result' before the last period
    output_file = open(output_file_name, 'w')
    output_file.close()
    output_file = open(output_file_name, 'a')

    # read input file and write into output file
    print('Writing into ' + output_file_name)
    fp = open(input_file_name)
    for line in fp:
        tag_file_name, line_num = get_jump_point(line)
        if tag_file_name is not None:
            content = get_tag_content(tag_file_name, line_num)
            output_file.write(line.rstrip('\n') + ':' + content)
        else:
            output_file.write(line)

    print('Complete!')
    print('Cleaning...')
    fp.close()
    output_file.close()
    print('Bye!')


# *******************************
# * Internal Functions
# *******************************
def get_tag_content(file_name, line_num):
    ret = ''
    fp = open(os.path.abspath(file_name))
    for idx, line in enumerate(fp):
        if (idx + 1) == int(line_num):
            ret = line
            break

    fp.close()
    return ret

def get_jump_point(line):
    """The function gets file name and line number
    to jump to obtain content.
    """
    tag_file_name = None
    line_num = None

    result = re.split('[\(\)]', line)

    if len(result) >= 2:
        tag_file_name = result[0].rstrip()
        line_num = result[1]

    return (tag_file_name, line_num)

if __name__=='__main__':
    main()

