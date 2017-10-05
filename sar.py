import os
import sys 
import re

topdir = sys.argv[1]
old_pattern = sys.argv[2].lower()
new_pattern = sys.argv[3].lower()
old_pattern_for_file_system = old_pattern.replace('/', '#')
new_pattern_for_file_system = new_pattern.replace('/', '#')

old_p_regex = re.compile(re.escape(old_pattern), re.IGNORECASE)

for dirpath, dirnames, files in os.walk(topdir, False):
  if '.git' in dirpath:
    continue
  for name in files:
    if old_pattern_for_file_system in name: #rename files in current dir if necessary
      new_file_name = name.replace(old_pattern_for_file_system, new_pattern_for_file_system)
      os.rename(os.path.join(dirpath, name), os.path.join(dirpath, new_file_name))
      name = new_file_name
    
    f = open(os.path.join(dirpath, name), 'r')
    filedata = f.read()
    f.close()

    new_file_data = old_p_regex.sub(new_pattern, filedata)

    f = open(os.path.join(dirpath, name), 'w')
    f.write(new_file_data)
    f.close()
    
  if old_pattern_for_file_system in dirpath: #rename current dir if necessary
    new_dir_path = dirpath.replace(old_pattern_for_file_system, new_pattern_for_file_system)
    os.rename(dirpath, new_dir_path)

    
