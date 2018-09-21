# test utility functions
import os

#
# Add files to directories for testing
#
# param1: the filename
# param2: the mode(write, read, append, etc.)
# param3: content for the new file to be written or appended
#
def add_file(filename, mode, content):
    fo = open(filename, mode)
    fo.write(content)
    fo.close()

#
# Create Directory structure for testing
#
# Param: the path to start creating the structure
#
def set_up_directories_files(path, levels=1):
    if not os.path.isdir(path):
        os.mkdir(path)

    os.chdir(path)
    add_file('foo.test', 'w', 'Test file to remove')
    add_file('bar.txt', 'w', 'Test file to keep')

    if not os.path.isdir(os.path.join(path, 'subfoo')):
        os.mkdir('subfoo')

    os.chdir('subfoo')
    add_file('foo.test', 'w', 'Test file to remove')
    add_file('bar.txt', 'w', 'Test file to keep')

#
# Tear down the test directoies and files
#
def tear_down_directories_files(path):
    for root, dirs, files in os.walk(path, topdown=False):
        if root == path or root == os.path.join(path, 'subfoo'):
            for file in files:
                os.remove(os.path.join(root, file))
            os.rmdir(root)
        else:
            return False;
