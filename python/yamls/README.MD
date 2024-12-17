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


## Deploy to other k8s disturbutions
- k8s disturbutions runs on nodes so to access the application you will need an ip address of one of the nodes
### Access the endpoints
```
http://<NodeIP>:<NodePort>/results
http://<NodeIP>:<NodePort>/csv
http://<NodeIP>:<NodePort>/healthcheck
```
## Access the application using external ip
- for that you will need to deploy the recommened folder
- dont deploy the metallelb-pool.yaml until all the pods related to the namespace metallb-system are up you can check that by using the following command:
```
kubectl get all -n metallb-system
```
- before deploying the metallelb-pool.yaml please open the file and change the line 8 with your external ip address range accroding to your network
- after deploying the pool write the following command:
```
kubectl get svc -n ingress-nginx
```
- copy the external ip written on the ingress-nginx-controller service
- go to your hosts file on your computer(Windows - C:\Windows\System32\drivers\etc) (Mac\Linux - /etc/hosts)
- add the follwing line
```
<external-ip>   app.python.com
```
## Access the endpoints
Write the following urls in your brower:
```
app.python.com/results
app.python.com/csv
app.python.com/healthcheck
```
