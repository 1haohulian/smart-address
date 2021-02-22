import re

a_file = open(r'../datas/a1.py', 'w')
with open(r'a1.php') as f_obj:
    for line in f_obj.readlines():
        new_line = re.sub(r"'(\d+?)' => array\('name' => (.*?), 'pid' => (\d+)\)", r"\1: {'name': \2, 'pid': \3}", line)
        a_file.write(new_line)
a_file.close()