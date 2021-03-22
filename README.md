
The app runs on django backend with react front end for displaying a list of phone numbers with a fuzzy search implemented.


<h4>Usage</h4>


<h5>Docker-compose</h4>
 If using docker compose just run <code>docker-compose up</code> to run the app. It will be running on
 <link>http://localhost:8000</link>

<br>
<br>
<h4>Docker</h4>
 If using docker,
get the image from dockerhub at
<br>
<link>https://hub.docker.com/r/thedoodler/qure_assignment</link>
<br>
here the ports need to be mapped so use
<br>
<br>
<code>docker run -t -p 8000:8000 thedoodler/qure_assignment:latest</code>

after pulling the image from hub.
<br>
<br>

<h4>Shell</h4>
to just run the application without dependancies, get into the project folder and run the "run.sh" file as
<br>
<br>
 <code>sh run.sh</code>
<br>
<br>

<h3>Signup</h3>
signup with valid username and password to see the phone number list.
If you have already signed up just login
