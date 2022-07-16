# Deploy FastAPI JWT Microservice on AWS EC2

**install dependencies Python**

    $ python -m venv venv
    $ source venv/scripts/activate | ./venv/scripts/activate
    $ pip install -r dashboard_user/requirements.txt
    $ pip install -r register_user/requirements.txt

**testing run server on localhost dashboard port 8001**

    $ cd dashbard_user
    $ uvicorn app.main:app --port 8001 --reload

**testing run server on localhost register port 8002**

    $ cd dashbard_user
    $ uvicorn app.main:app --port 8002 --reload

**Run docker container swarm**

    $ docker compose up -d

**You can run reverse proxy this url**

    https://localhost:8080/api/v1/register/docs
    https://localhost:8080/api/v1/dashboard/docs

**Access to SSH Client EC2**

    1. Open an SSH client.
    2. Locate your private key file. The key used to launch this instance is nginx_key.pem
    3. Run this command, if necessary, to ensure your key is not publicly viewable.
        chmod 400 [you key pair accss]
    4. Connect to your instance using its Public DNS:
        [your public DNS]

    Example:
     ssh -i "fastapi_key.pem" ubuntu@123-456.987.compute-1.amazonaws.com

**Setup install dependencies instance**
    
    $ sudo apt-get update
    $ sudo apt install -y python3-pip nginx
    $ sudo apt install docker.io
    $ sudo apt install docker-compose

**Setup Nginx**
    
    $ sudo /etc/nginx/sites-enabled/fastapi_nginx.conf

```nginx
server {
  listen 8080;
   server_name [your domain];

  location / {
    proxy_pass http://127.0.0.1:8001;
  }

  location /api/v1/dashboard {
    proxy_pass http://127.0.0.1:8001/api/v1/dashboard;
  }

  location /api/v1/register {
    proxy_pass http://127.0.0.1:8002/api/v1/register;
  }

  location /api/v1/user {
    proxy_pass http://127.0.0.1:8001/api/v1/user;
  }

  location /api/v1/authenticate {
    proxy_pass http://127.0.0.1:8002/api/v1/authenticate;
  }

}
```
    






