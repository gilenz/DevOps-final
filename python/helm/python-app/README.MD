# How to deploy the helm chart?
## Deploy to k8s
- Please write the following command:
```
helm install python-app -f values.yaml .
```
## Access the application using minikube
```
minikube service python-service
```
- After you will get in your web page the following line:
Not Found
The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
Thats fine because the application is configured only for the endpoints mentioned in the Docker readme file.
### Access the endpoints
write the following urls into you brower accroding to the nodeport that generated on your enviroment
```
http://127.0.0.1:<NodePort>/results
http://127.0.0.1:<NodePort>/csv
http://127.0.0.1:<NodePort>/healthcheck
```


## Access the application with other distributions of k8s
- k8s distributions runs on nodes so to access the application you will need an ip address of one of the nodes
### Access the endpoints
```
http://<NodeIP>:<NodePort>/results
http://<NodeIP>:<NodePort>/csv
http://<NodeIP>:<NodePort>/healthcheck
```
### Note that accessing via ingress not enable with the helm chart for that you will need to deploy the recommended/ folder
