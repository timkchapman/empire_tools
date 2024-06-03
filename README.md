# empire_tools
A set of tools for the Empire Live Action Role Playing game run by Profound Decisions in the UK.

# requirements
all requirements for the project are listed in the accompanying requirements.txt. They need to be installed as standard to the virtual environment. using:

    pip install -r requirements.txt

With that working, the project can now be run.

# running the project
Empire tools can be run by first exporting the flask app using:

    export FLASK_APP=app

and then:

    flask run

after this is achieved, navigate to localhost:5000 to be shown to the initial page. You can either navigate to the different tools using the toolbar or you can navigate directly using the following urls:

    localhost:5000/calculator