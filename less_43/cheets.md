## kubespray
https://github.com/kubernetes-sigs/kubespray.git
## metrics-server
https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

```bash
kubectl patch deployment metrics-server -n kube-system --type='json' -p='[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--kubelet-insecure-tls"}]'
```

## affinity
- requiredDuringSchedulingIgnoredDuringExecution
- preferredDuringSchedulingIgnoredDuringExecution
