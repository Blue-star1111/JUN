# FastAPI - YOLOv5 Inference

## 1. FastAPI Install
  - pip install fastapi
  - pip install uvicorn
## 2. YOLOv5 Install
  - git clone https://github.com/ultralytics/yolov5  # clone
  - cd yolov5
  - pip install -r requirements.txt  # install
## 3. python-multipart Install(Image File Upload)
  - pip install python-multipart
## 4. Server(uvicorn) Start
  - uvicorn main:app --reload --host 127.0.0.1 --port 8001

## 5. Inference Test
  - http://127.0.0.1:8001/docs

# VueJs in Grafana Dashboard

## 1. Grafana(8.2.7) Install
  - https://grafana.com/grafana/download/8.2.7?platform=linux
  - sudo apt-get install -y adduser libfontconfig1
  - wget https://dl.grafana.com/enterprise/release/grafana-enterprise_8.2.7_amd64.deb
  - sudo dpkg -i grafana-enterprise_8.2.7_amd64.deb

## 2. Grafana Start/Stop
  - Start: service grafana-server start
  - Stop: service grafana-server stop

## 3. PostgreSQL Install
  - sudo apt-get install postgresql postgresql-contrib

## 4. PostgreSQL Setting
  - sudo -u postgres psql
  - CREATE USER {user} WITH PASSWORD {password}
  - ALTER ROLE {user} CREATEDB REPLICATION;
  - CREATE DATABASE {database} OWNER {user};

## 5. pgAdmin4 Install
  - sudo curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add
  - sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
  - sudo apt install pgadmin4

## 6. pgAdmin Start
  - sudo /usr/pgadmin4/bin/setup-web.sh
  - http://localhost/pgadmin4 

## 7. PostgreSQL 외부 접속 허용
  - https://tbmaster.tistory.com/89 참조
  - sudo nano /etc/postgresql/10/main/postgresql.conf 
    * listen_addresses = '*' 추가
  - sudo nano /etc/postgresql/10/main/pg_hba.conf
    * IPv4 local connections 에서 Address를 0.0.0.0/0으로 변경
  - sudo service postgresql restart

## 8. Grafana-PostgreSQL Connect
  - Configuration - Data sources
  - Add data source: PostgreSQL 선택
  - Host(localhost), Port(5432), Database, User, Password 입력

## 9. Grafana Client 공유 설정
  - sudo nano /etc/grafana/grafana.ini
  - sudo nano /usr/share/grafana/conf/defaults.ini
    * allow_embedding = true
    * auth.anonymous = true

## 10. Vue.js(+Node.js) Install
  - nodejs, npm > vuejs, vue/cli Install
  - curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
  - sudo apt install -y nodejs
  - npm install vue@next
  - sudo npm install -g @vue/cli
  - create vue-app: vue create {app_name}

## 11. Vue add Package
  - vuetify: vue add vuetify
  - vue-router: npm i vue-router --save
  - vue-friendly-iframe: npm i vue-friendly-iframe

