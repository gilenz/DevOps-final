# How to deploy manifests to k8s?
## Deploy to k8s
- The yamls contain deployment,service,ingress(if you want to access the application with external ip you need to deploy the recommended folder-written in the end of the file)
```
kubectl apply -f .
```
## Access the application using minikube
```
minikube service python-service
```
After you will get in your web page the following line:
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


## Deploy to other k8s disturbutions
- Please make sure that Docker engine is runing
- To build this application please run the following command
```

```

```
