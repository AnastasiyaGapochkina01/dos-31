```bash
kubectl create namespace argocd
kubectl apply -n argocd \ -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl port-forward svc/argocd-server -n argocd 8080:443 --address 0.0.0.0

#
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prom-stack prometheus-community/kube-prometheus-stack -n monitoring --create-namespace
kubectl -n monitoring port-forward svc/prometheus-operated 9090:9090 --address 0.0.0.0

#
monitoring.coreos.com/v1
```
