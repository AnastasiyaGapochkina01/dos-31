```bash
praqma/network-multitool

-o=jsonpath="{range .items[*]}{.status.podIP}{end}"

kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.14.5/config/manifests/metallb-native.yaml

kubectl wait --namespace metallb-system \ --for=condition=ready pod \ --selector=app=metallb \ --timeout=90s

helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

helm install ingress-nginx ingress-nginx/ingress-nginx   --set controller.service.type=NodePort   --set controller.service.nodePorts.http=32080   --set controller.service.nodePorts.https=32443

kubectl get pods -n default -l app.kubernetes.io/name=ingress-nginx

crd.projectcalico.org/v1

```
