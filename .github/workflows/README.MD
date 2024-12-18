# What this pipeline do?
## The pipeline has 1 job and steps these are the steps:
- Start minikube - Action named medyagh/setup-minikube@latest used to install small cluster(minikube)
- Apply helm chart - Installing the helm chart from the helm directory to deploy the application
- Wating for pods to create - Sleep 40s is to wait the pods of the application to create because the tests on the step forward is depend on that(takes time to pull the image)
- Verify the pods are runing - Check the pods of the application are runing
- Run endpoints tests - check the endpoints if they runing or not

