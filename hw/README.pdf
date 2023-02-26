1) What is Docker and how does it differ from a virtual machine?

    - Docker is a platform that allows users to ship and run applications within containers. Containers are lightweight
    since they operate on the host's operating system's kernel, allowing them to be much faster to start and shut down
    when compared to VM's. 

2) How does Docker ensure that containers are isolated from each other and the host
system?

    - There are several ways that containers are isolated from one another:
    1) Containers are read-only, therefore they are isolated from altering other containers and the host
    2) Uses cgroups (Control Groups) to control/limit the resources that each container is entitled to,
    such as CPU
    3) Each container has it's own namspace, such as the PID namespace
    4) Network isolation, which ensures that containers have no way of communicating with one another without permisison

    Reference: https://snyk.io/blog/best-practices-for-container-isolation/#:~:text=Docker%20containers%20achieve%20isolation%20by,virtualized%20containers%20%E2%80%94%20like%20AWS%20Firecracker.

3) What is the purpose of a Dockerfile?

    - The purpose of the Dockerfile 
    is to have a lightweight way of providing instructions on how to build a Docker image by defining the required
    configurations/requirements in order to build your program so that it can be successfully run on multiple different
    environments

4) What is the purpose of a requirements.txt file?

    - This file is used by the dockerfile when building the Docker image. The text file holds all required dependencies
    that are used in your code. Incorporating this file and building it into the Docker image allows for the code to be 
    run on systems other than the one used for development

5) How can you mount a host directory as a volume in a container?

    - You can mount a host directory as a volume in a container by using the -v or --mount flags. Using the -v flag 
    allows the combination of all the options together into one filed, whereas --mount seperates them.
    Here's an example:
        docker run -v /path example-image, or
        docker run --mount type=bind,source=/path,target=/target example-image

    Reference: https://docs.docker.com/storage/bind-mounts/

6) What is the difference between a docker image and a docker container?

    - Docker images allow for the code in a Docker container to be run, therefore the container is an instance of that
    image. When a container is run, an isolated environment is created based off of the image.
    To better understand this, here is an Images analogy in one of the slide decks:
    "If MSOffice is an image, then to create a word doc you need to launch MSWord, which would make it the container".
    One other import factor between Docker images and container is that images are read only, therefore they cannot be
    modified, whereas containers have both read and write permisisons

7) What command can be used to create an image from a Dockerfile? [

    - To create an image from a Dockerfile you can use the docker build command:
    docker build /path

8) What command will start a docker container?

    - To start a container you can use the docker run command:
    docker run IMAGE

9) What command will stop a docker container?

    - To stop a Docker container you can use the docker stop command:
    docker stop CONTAINER

10) What command will remove a docker container? Image?

    - To remove Docker containers and images, you can use the follow commands:
    Remove container: docker rm CONTAINER
    Remove image: docker rm IMAGE

11) What command will list all running docker containers? all containers?

    - To see all containers you can use the following command:
    docker ps -a
    
    To see only the running containers you can use a filter on only the running containers:
    docker ps -f status=running

    -f indicates a filter and status=running indicates our criteria

    Reference: https://docs.docker.com/engine/reference/commandline/ps/

12) What command will list all docker images?

    - To list all docker images you can use the following command:
    docker images

13) What command do you use to deploy docker containers using the information in the
dockercompose.yml file?

    - To deploy docker containers using the dockercompose.yml you can use the following command to build then run:
    docker-compose up --build

14) How can you specify in the docker-compose.yml file that you want docker containers
to use the hosts' network?

    - To specify that you want docker containers to use the hosts' network you need to provide this in your
    docker-compose.yml file:
    network_mode: "host"

    Reference: https://docs.docker.com/compose/compose-file/compose-file-v3/#network_mode

15) How can you specify in the docker-compose.yml file where the Dockerfile for a
particular container is found?

    - To specify where the Dockerfile for a container is found you can provide this in your docker-compose.yml:
    build: /path


