# the process
1. navigate to page.html and enter the code and select format from dropdown
2. code is submitted to code.php which will save it in a .txt file and make a database entry
3. (currently) manually call marker.py to auto compile and run the code
4. (currently) manually update database with marks

# improvments
- covnert code.php to python flask
- allow for code output to be matched against a defined input
- allow for python to auto update the database with result
- allow python to check for new submissions and auto mark
- allow for python the check the filetype and select appropiate marking system

# system Service
The script can be added as a system service to auto mark tests every 60 seconds by following the steps
1. enter the absolute path to marker.py and optionally log files in the automark.service
2. copy automark.service to /etc/systemd/system/multi-user.target.wants/
3. start the service with: systemctl start automark.service
4. have the service load on boot with: systemctl enable automark.service
