#i have an audio file ,print the size of the file 
import os

file_name = "Advanced Algorithms (COMPSCI 224), Lecture 1 [0JUN9aDxVmI].webm"

#i want you to check if the file size is more than 24MB , then make a folder and split into size of 24MB each and name part 1 , part 2 etc
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