## Run tests

* install docker 

    https://docs.docker.com/get-docker/

* clone project 
        
        git clone https://github.com/drewkarpov/python_pytest.git

* move to project directory:

        $ cd /{project_root}

* prepare virtual environment and install requirements

        $ python -m venv hc-venv
        $ pip install -r requirements.txt

* pull browser image for selenoid

        $ docker pull selenoid/chrome:84.0
        
* run tests
    
        $ HOST={your_local_ip} make run_tests
        
* host allure_reports

        $ make hosting_allure_report


host app : http://localhost:8000
host allure : http://localhost:8085
        



