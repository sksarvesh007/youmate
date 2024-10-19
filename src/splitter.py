import os
import glob
if not os.path.exists("splitted"):
    os.mkdir("splitted")
if os.path.exists("splitted"):
    files = glob.glob('splitted/*')
    for f in files:
        os.remove(f)
def split_file(file_name, chunk_size=24*1024*1024):
    if os.path.getsize(file_name) > chunk_size:
        
        with open(file_name, 'rb') as f:
            data = f.read(chunk_size)
            i = 1
            while data:
                with open(f"splitted/part{i}.webm", 'wb') as f1:
                    f1.write(data)
                data = f.read(chunk_size)
                i += 1
    else:
        #just copy the file into the splitted directory
        with open(file_name, 'rb') as f:
            data = f.read()
            with open(f"splitted/part1.webm", 'wb') as f1:
                f1.write(data)
