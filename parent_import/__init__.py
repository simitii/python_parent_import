
import os,sys,inspect,glob,importlib

stack = inspect.stack()
for frame_index in range(1,len(stack)):
    caller_frame = stack[frame_index]
    caller_filename = caller_frame[0].f_code.co_filename
    if not caller_filename.startswith("<frozen"):
        caller = caller_frame[0]
        break

caller_dir = os.path.dirname(os.path.abspath(inspect.getfile(caller)))
caller_parent_dir = os.path.dirname(caller_dir)

def add_ancestor_dir_to_path(level=1):
    if level > 0: 
        parent_dir = caller_parent_dir
        for i in range(1, level):
            parent_dir = os.path.dirname(parent_dir)
        if parent_dir not in sys.path:
            sys.path.insert(0, parent_dir)

class dir_class:
    def __init__(self, dir_path=caller_parent_dir):
        self.dir_path = dir_path
        
        sys.path.insert(0, self.dir_path)

        path_len = len(self.dir_path)+1
        for d in glob.glob(self.dir_path + "/*/"):
            dir_name = d[path_len:-1]
            setattr(self, dir_name, "dir")

        for f in glob.glob(self.dir_path + "/*.py"):
            file_name = f[path_len:-3]
            setattr(self, file_name, "file")
    
    def __getattribute__(self, name):
        if name == "dir_path":
            return super(dir_class, self).__getattribute__("dir_path")
        elif name == "parentdir":
            parent_dir = os.path.dirname(self.dir_path)
            return dir_class(dir_path=parent_dir)
        elif super(dir_class, self).__getattribute__(name) == "file":
            module = importlib.import_module(name)
            return module
        else:
            return dir_class(dir_path=self.dir_path+"/"+name)
        
parentdir = dir_class()