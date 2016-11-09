****
Nombre | Código
--- | --- | ---
Esteban Durán | 12103025 
****

##Jenkins

Instalacion de dependencias requeridas para usar jenkins
```sh
# yum install java-1.7.0-openjdk
# yum install wget -y
# yum install git -y
# sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo
# sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
# sudo yum install jenkins
```
Iniciar el servicio de Jenkins y habilitar su respectivo puerto
```sh
# chkconfig jenkins on
# service jenkins start
# iptables -I INPUT 5 -p tcp -m state --state NEW -m tcp --dport 8080 -j ACCEPT
# service iptables save
```
Se crea el usuario y ambiente virtual para Jenkins
```sh
# useradd jenkins
# passwd jenkins
# su jenkins
$ mkdir /var/lib/jenkins/.virtualenvs
$ cd /var/lib/jenkins/.virtualenvs
$ virtualenv testproject
$ . testproject/bin/activate
```
Se instalan las herramientas requeridas para trabajar con pruebas en jenkins
```sh
$ pip install xmlrunner
$ pip install unittest2
$ pip install pytest
$ pip install pytest-cov
$ pip install flask

$ pip freeze > requirements.txt

##Configuracion de jenkins con github

![alt text](link)

##Creacion de las pruebas
Cree un archivo de nombre **test_files.py**

```sh
import pytest
import json, files

@pytest.fixture
def client(request):
    client = files.app.test_client()
    return client


@pytest.mark.order1
def test_create(client):
  
        testFile3 = {'filename': 'testFile3', 'content': 'This is a test file'}
        testFile4 = {'filename': 'testFile4', 'content': 'This is a test file'}
        testFile5 = {'filename': 'testFile5', 'content': 'This is a test file'}

        execute3 = client.post('/files', data = json.dumps(testFile3), content_type='application/json')
        execute4 = client.post('/files', data = json.dumps(testFile4), content_type='application/json')
        execute5 = client.post('/files', data = json.dumps(testFile5), content_type='application/json')

        assert execute3.status == '201 CREATED'
        assert execute4.status == '201 CREATED'
        assert execute5.status == '201 CREATED'

        #assert get_content("testFile3") == "This is a test file"
        #assert get_content("testFile4") == "This is a test file"
        #assert get_content("testFile5") == "This is a test file"


@pytest.mark.order2
def test_recent_file(client):

        execute1 = client.get('/files/recently_created',follow_redirects=True)

        assert "testFile3" in execute1.data
        assert "testFile4" in execute1.data
        assert "testFile5" in execute1.data

@pytest.mark.order3
def test_get_all_files(client):

        execute1 = client.get('/files',follow_redirects=True)

        assert "testFile3" in execute1.data
        assert "testFile4" in execute1.data
        assert "testFile5" in execute1.data

@pytest.mark.order4
def test_remove_files(client):

        client.delete('/files', follow_redirects=True)

        execute1 = client.get('/files',follow_redirects=True)

        assert "testFile3" not in execute1.data
        assert "testFile4" not in execute1.data
        assert "testFile5" not in execute1.data
```

##Pruebas locales


Ejecutar las pruebas con pytest
```sh
py.test
```
Ejecutar pruebas de cobertura desde la terminal

```sh
py.test --cov-report term --cov=../testproject
```

![alt text](link)

#Dirección al github de la soluciónn
https://github.com/esteban-duran/testproject
