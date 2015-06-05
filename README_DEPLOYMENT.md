![alt text](http://mentoki.com/static/img/mentoki_logo_untertitel.jpg "Logo Title Text 1")

# Mentoki Deployment and Environemnts

## Remote Enviroments
Remote there are 3 enviroments:

###Mentoki Live:
This is the live webplatform

###Mentoki Test:
This is a copy of the live platform for staging purposes
In the tools directory is a tool 'copy-live-to-test.sh' that copies the data from the live database to the test database.
Both Live and Test have their own environment (So far they don't share environments, but maybe they should?)
 
###Mentoki Dev:
This is the development environment. There is also a to tool to put the live data in it, but it will probably only work 
after releases when both Databases have the same structure
  
## Local Environments
On my local computer I have two environments: Live and Dev.

###Local Live:
The procedure to get the database down into my local Live Database is as follows:

1. On the remote 'bash get-live-data.sh' (in the tools directory): produces a file 'live.sql'
2. Locally 'fab livedata' : gets the the file down to the local directory 'mentoki_tools'
3. Locally run 'bash renew-local-db.sh' (in directory 'mentoki_tools'): empties the local copy of the live-database 
5. Done

###Deployment:
My deployment is as follows for the time being:
1. commit feature-branch
2. merge into git master repo
3. fab stage : deploys into the test area
4. on remote: collectsstatic, migrate
5. fab deploy: deploys the live platform
6. on remote: collectstatic, migrate

