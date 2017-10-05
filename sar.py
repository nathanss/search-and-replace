import os
import sys 
import re

topdir = sys.argv[1]
old_pattern = sys.argv[2].lower()
new_pattern = sys.argv[3].lower()
old_pattern_for_file_system = old_pattern.replace('/', '#')
new_pattern_for_file_system = new_pattern.replace('/', '#')
old_p_regex = re.compile(re.escape(old_pattern), re.IGNORECASE)

def rename_file(name, dirpath, old_pattern, new_pattern):
    new_file_name = name.replace(old_pattern, new_pattern)
    os.rename(os.path.join(dirpath, name), os.path.join(dirpath, new_file_name))
    return new_file_name

def replace_file_content(filepath):
    f = open(filepath, 'r', encoding='UTF8')
    filedata = f.read()
    f.close()

    new_file_data = old_p_regex.sub(new_pattern, filedata)

    f = open(filepath, 'w', encoding='UTF8')
    f.write(new_file_data)
    f.close()

def process_file(name, dirpath):
    if old_pattern_for_file_system in name:
      name = rename_file(name, dirpath, old_pattern_for_file_system, new_pattern_for_file_system)
      
    replace_file_content(os.path.join(dirpath, name))

def process_dir(dirpath):
  basename = os.path.basename(dirpath)
  if old_pattern_for_file_system in basename: #rename current dir if necessary
    newbasename = basename.replace(old_pattern_for_file_system, new_pattern_for_file_system)
    new_dir_path = dirpath.replace(basename, newbasename)
    os.rename(dirpath, new_dir_path)
    
for dirpath, dirnames, files in os.walk(topdir, False):
  if '.git' in dirpath:
    continue
  for name in files:
      if '.pdf' in name:
        continue
      process_file(name, dirpath)
  process_dir(dirpath)
    