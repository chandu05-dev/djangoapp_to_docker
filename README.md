# djangoapp_to_docker
1. FIRST CLONE THE REPOSITORY 
2. OPEN POWERSHELL
3. GO INTO THE DIRECTORY OF CLONED  REPOSITORY(the docker file is present in this directory)
4. TYPE IN THE COMMAND "docker build -t "app:v4" ." (. indicates the current directory, if you want run from outside repository give the path to repository in place of dot)
5. ONCE THE IMAGE IS BUILT CHECK  THE IMAGE DETAILS USING THE COMMAND "docker image ls"(check for the image id and for tag)
6. NOW RUN THE COMMAND "docker run -d -p "8000:8000" -v {$CLONED REPOSITORY}:/code app:v4" (the port 8000 of docker container is allocated to the port 8000 of your computer and     the                                                                                           contents of the cloned repository is mounted from your computer to the /code of the                                                                                                 container)
7. NOW GO TO YOUR BROWSER AND IN THE ADDRESS BAR YOU CAN GO TO THE FOLLOWING URLS
 * http://localhost:8000/auth/register
 * http://localhost:8000/auth/mylogin
