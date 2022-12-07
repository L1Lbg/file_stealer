<h1>Welcome to file_stealer guide</h1>
<h4>DISCLAIMER: Please use this on people that gave you explicit permission to use this repository or on yourself. I do not claim any responsability from the usage of this repository. This was made for my Python learning and skill development.</h4>
<br>
<h2> USAGE : </h2> 
<br>
This repository is divided in two sides, the folder, script, which would go on the 'victims' computer (Please make sure that the so called victim knows what is happening at all times), so you have to make sure they execute the main.py script, which will make them send the files to your computer. The server folder is everything that needs to be on the attacker computer, which will host a django server awaiting for the HTTP request of the victim to download the files.
<h3>Victim side</h3>
Go to the main.py script in the script folder, where you will change some configurations 
<ul>
  <li>The term_searched, the script will download any file that contains the term.</li>
  <li>If you want to only scan the principal dirs, where all the personal files are supposed to be, which you can change them on line 26. This makes the    process a lot faster, and I recommend putting this to True</li>
  <li>The server IP, where the attacker server is being hosted, and below, put the port, which by default is 8000</li>
</ul>
<h3>Attacker side</h3>
On the other side, you only need to run a command, make sure that in the terminal you are in the folder  

```
 /file_steal/ 
```
and run the command 
```
python manage.py runserver YourServerIP:YourServerPort
```
<br>
You will receive the files on the folder file_stealer/server/file_receiver/files/

<h4>If you already have Python installed, you only need to download the django module</h4>
