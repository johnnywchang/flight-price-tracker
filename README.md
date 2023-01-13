These are files created for purposes of setting up a Flask webserver to read in and update JSON data about historical flight information.

For getting the Flask environment up and running, within the Windows command line:

    cd\
    cd "git_repos\flight_price_tracker"
    set FLASK_APP=appfile.py #updated file reference for running flask server
    set FLASK_DEBUG=1 #set Flask environment to debug/development
    flask run

After flask webserver set up, open another Anaconda command line window to interact with the webserver:

    cd\
    cd "git_repos\flight_price_tracker"

        To update the list of countries in the \countries path via json file:
            curl -X POST -H "Content-type:application/json" -d "@skyscanner_dallas.json" http://127.0.0.1:5000/countries
        
        To update the json file "allcountries.json":
            curl -X POST -H "Content-type:application/json" -d "@skyscanner_dallas.json" http://127.0.0.1:5000/data
