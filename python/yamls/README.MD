# How to deploy manifests to k8s?
## Deploy to minikube
- The yamls contain deployment,service,ingress(if you want to access the application with external ip you need to deploy the recommended folder)
```
kubectl apply -f .
```
## Access the application
```
minikube service python-service
```


## Deploy to other k8s disturbutions
- Please make sure that Docker engine is runing
- To build this application please run the following command
```

```

```
