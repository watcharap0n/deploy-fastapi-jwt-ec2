# FastAPI JWT Microservice by MongoDB

**install dependencies Python**

    $ python -m venv venv
    $ source venv/scripts/activate | ./venv/scripts/activate
    $ pip install -r dashboard_user/requirements.txt
    $ pip install -r register_user/requirements.txt

**testing run server dashboard port 8001**

    $ cd dashbard_user
    $ uvicorn app.main:app --port 8001 --reload

**testing run server register port 8002**

    $ cd dashbard_user
    $ uvicorn app.main:app --port 8002 --reload

**Run docker container swarm**

    $ docker compose up -d

**You can run reverse proxy this url**

    https://localhost:8080/api/v1/register/docs
    https://localhost:8080/api/v1/dashboard/docs







