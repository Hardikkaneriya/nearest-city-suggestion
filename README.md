# nearest-city-suggestion

clone this repo into the local using git clone command

1. build docker image using below command
# docker build -t app .

2. Run docker container with interactive shell .
# docker run -it --rm app /bin/bash
above command will open terminal in docker container

3. run python main script with city name and duration as input
# python3 srs/main.py --city_name=Berlin --duration=10

above command will display the output as well as create json file inside ouput folder
