# delete-files-csv
If you have a large list of files that you need to delete from a directory this simple app should do the trick.  
You will need the pyinstaller module to create an executable package.  
Install pyinstaller with the following command either in terminal or CMD (you can copy and paste it and hit enter):  

   `pip pyinstaller`  
   
You will need to edit the .py file with the location for an icon (.ico file)

Now run the following (on the command prompt):  

    pyinstaller --onefile -w delete_files.py  

You should now have an exe/dmg file in your home directory  
