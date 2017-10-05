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
  print('Current dirpath: ' + dirpath)
  for name in files:
    if '.pdf' in name:
      continue
    print(os.path.join(dirpath, name))
    if old_pattern_for_file_system in name: #rename files in current dir if necessary
      new_file_name = name.replace(old_pattern_for_file_system, new_pattern_for_file_system)
      os.rename(os.path.join(dirpath, name), os.path.join(dirpath, new_file_name))
      name = new_file_name
    
    f = open(os.path.join(dirpath, name), 'r', encoding='UTF8')
    filedata = f.read()
    f.close()

    new_file_data = old_p_regex.sub(new_pattern, filedata)

    f = open(os.path.join(dirpath, name), 'w', encoding='UTF8')
    f.write(new_file_data)
    f.close()
    
  basename = os.path.basename(dirpath)
  if old_pattern_for_file_system in basename: #rename current dir if necessary
    newbasename = basename.replace(old_pattern_for_file_system, new_pattern_for_file_system)
    new_dir_path = dirpath.replace(basename, newbasename)
    os.rename(dirpath, new_dir_path)