# logs-analysis

Logs Analysis is an internal reporting tool of a user-facing newspaper site that will use information from the database to discover what kind of articles the site's readers like, who is the most popular author, etc.

**This project makes use of the Linux-based virtual machine (VM), you'll need VirtualBox, Vagrant installed in advance.**

## Start Guide:
* Put catalog file inside vagrant subdirectory
* From your terminal, inside the vagrant subdirectory, run the command vagrant up
* When vagrant up is finished running, run vagrant ssh to log in to your Linux VM
* Download newsdata.sql. Put this file into the vagrant directory
* To load the data, use the command psql -d news -f newsdata.sql
* Run command psql news
* Create the first view: run command CREATE VIEW temp_view AS SELECT title, count(path) AS num FROM articles, log WHERE articles.slug = substring(path from 10 for 100)GROUP BY title ORDER BY num DESC; 
* Create the second view: run another command CREATE VIEW temp_author AS SELECT author, num FROM articles, temp_view WHERE temp_view.title = articles.title;
* Inside the VM, change directory to \vagrant (cd \vagrant), and then cd catalog
* Run command python catalog.py

