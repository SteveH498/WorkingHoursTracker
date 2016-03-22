# WorkingHoursTracker
Python script for automatic logging of working start and end times on OS startup and shutdown.
The stored time stamps can then be used to calculate the total working time.

Prerequisite for using the script is the presence of a locally installed sqlite database:
https://www.sqlite.org/index.html
http://www.tutorialspoint.com/sqlite/sqlite_installation.htm

On startup:
```
python working_hours_tracker.py --startup
```

On shutdown:
```
python working_hours_tracker.py --shutdown
```
