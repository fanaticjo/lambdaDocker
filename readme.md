**AWS LAMBDA DOCKER BASED DEPLOYMENT AND PYTHON MOCK**

Pre-requistive 
1) Docker 
2) Aws account 

**Steps**
1) Create a ecr public or private repository in the aws account 
2) Create a docker Image in your python repository
    You can use the base python image provided by aws
    Please see the Dockerfile
   
3) You must run docker build . -t <project_name>:<version-nu>

4) Give Docker push the appropriate permission 
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <accnumber>.dkr.ecr.us-east-1.amazonaws.com
   
5) Tag the docker build to the repository 
    docker tag <project-name>:<version> <acc-number>.dkr.ecr.us-east-1.amazonaws.com/python-con:latest
   
6) docker push 
    docker push <acc-number>.dkr.ecr.us-east-1.amazonaws.com/python-con:latest
   
7) create a lambda function and add the ecr repository
