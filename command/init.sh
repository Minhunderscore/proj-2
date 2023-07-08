kubectl create namespace app-demo
kubectl config set-context --current --namespace=app-demo
kubectl create deployment python-app-deployment --replicas 1 -o yaml --port 8000 --image jup1t3r3rd/proj-2:v3 > ~/python-app.yaml
kubectl create service nodeport -o yaml python --tcp 8000:8000 --node-port 30080 > ~/python-service.yaml


kubectl autoscale deploy/python-app --cpu-percent=95 --min=1 --max=10
kubectl get hpa/python-app -owide
kubectl describe hpa/python-app
