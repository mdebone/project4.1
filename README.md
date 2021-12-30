# project4.1

Okay, to get this to work, we need to import ###'conda install -c conda-forge pydrive'

From there you need to go to ##Google Cloud Platform, and create a project in ## Google Developer Console. 

You have '20 units' of whatever, the old APIs we called count against that number. 
You can't pause them, you have to kill them, which isn't a problem because there did;t really just a hands-on experience, so no loss. 

	↪ The trouble is that it takes two days to delete, so if anyone has spare resources I say we use their colab.

1.   If you have the spare resources, you can 'create a new project', You include the 3 of us, not names, just the number of people working on it.

2.  Then you go to the right drop-down menu and 'Enable Service API'
	↪ its a menu in the 'API & Services, click on the 'Library in the middle.


We probably want 'Google Drive API' but you don have the option to pick it, there are others
	↪ Click enable to enable the Google Drive API

3.   Need to make a Client ID credential, which basically just means using ' Client ID'
	↪ If you get an error, you need to confgure the consent page before moving to this step

	** As long as your application name doesn’t contain “Google” or other sensitive word, it will be passed.**

4.   From there download the JSON file
	↪ need to select for "Desktop App

5. Download the JSON file and we are good to go

# needs pip install pydrive

# Got PyDrive to work, use this article, https://towardsdatascience.com/how-to-manage-files-in-google-drive-with-python-d26471d91ecd
it runs on like 20 lines of code
I added all of the files to the .gitignore cause I figure they are a security risk, but not sure?

The other one was giving me a hard time, long story short, poor user interface.



## Getting the camera to work: conda install -c conda-forge aiosmtplib
but its imported as smtplib

Okay got detect_camera.py or ipynb to work, actually it said py, but my ipynb ran.
Things to note, you need to 'sender gmail' with password so somebody remind me how to do that with the gitignore please.

It also needs another gmail, the receiver gmail address, no password. It runs as long as you want and then you have to kill the terminal, 
the conn.quit doesn't seem to work in a reasonable amount of time, I think I ran it for a minute.




