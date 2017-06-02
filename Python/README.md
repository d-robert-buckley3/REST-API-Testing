# Set up
##Create a virtual environment to work in, add these files, activate the environment, then:

pip install -r requirements.txt

##Launch the student app on port 8085:

java -jar studentApp.jar --server.port=8085

##Run the tests:

python test_restapi_cmds.py
