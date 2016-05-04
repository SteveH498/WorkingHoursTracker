# Working Hours Tracker
Python script for automatic logging of working start and end times on OS startup and shutdown.
The stored time stamps can then be used to calculate the total working time.

Prerequisite for using the script is the presence of a locally installed sqlite database and at least Python 3.5.0 |Anaconda 2.4.0 (64-bit):
https://www.sqlite.org/index.html
http://www.tutorialspoint.com/sqlite/sqlite_installation.htm


On startup:
```
cd <location of the script>
python working_hours_tracker.py --startup --http_proxy HTTP_PROXY --https_proxy HTTPS_PROXY
```

On shutdown:
```
cd <location of the script>
python working_hours_tracker.py --shutdown --http_proxy HTTP_PROXY --https_proxy HTTPS_PROXY
```

Probably the easiest way to schedule the script for execution on startup and shutdown on Windows is to register it within the Task Scheduler.

How to execute scripts on startup and shutdown on windows: 
http://www.howtogeek.com/138159/how-to-enable-programs-and-custom-scripts-to-run-at-boot/
http://superuser.com/questions/165142/using-task-scheduler-to-run-a-task-before-shutdown
