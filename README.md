# Disclaimer!
This project is currently not at a fully functional state and contains all kinds of bugs nor might not work at all.
Do not try to use it yet unless you know exactly what you are doing!

---

# split-safe

--- 
A file backup CLI tool for small amount of important files to eliminate the need for an additional backup device or 
cloud service.

Instead of having a specified backup device or cloud service, split-safe utilizes normal drives on the computer.
It keeps track of user defined important files and distributes them to ordinary drives as hidden ZIP archives.
In case any of the drive fails, split-safe makes sure that the important files are always already backupped on another 
drive.

### Example (planning):
You have tagged ```C:/foo.txt, D/:bar.py, E:/baz.jpg``` as important files via split-safe, these files are then
automatically copied and distributed to another drives into a ZIP archives (to reduce the size).  

```C:/foo.txt -> D:/splits_impo.zip/foo.txt```  
```D:/bar.py -> E:/splits_impo.zip/bar.py```  
```E:/baz.jpg -> C:/splits_impo.zip/baz.jpg```  

Let's say your drive D:/ fails, in order to retrieve the original ```D:/bar.py```, you can just either manually extract
it from ```E:/splits_impo.zip/bar.py``` or run ```splits retrieve <failed drive> <new drive>``` to automatically 
extract and move it to otherwise the original file path except for the drive it is located.