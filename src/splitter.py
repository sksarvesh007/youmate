import os

file_name = "Advanced Algorithms (COMPSCI 224), Lecture 1 [0JUN9aDxVmI].webm"
if os.path.getsize(file_name) > 24*1024*1024:
    os.mkdir("splitted")
    with open(file_name, 'rb') as f:
        data = f.read(24*1024*1024)
        i = 1
        while data:
            with open(f"splitted/part{i}.webm", 'wb') as f1:
                f1.write(data)
            data = f.read(24*1024*1024)
            i += 1