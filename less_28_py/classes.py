class Microsecrive:
    min_mem_limit = 128
    default_replicas = 1
    def __init__(self, name, version, replicas=None):
        self.name = name
        self.version = version
        if replicas is not None:
            self.replicas = replicas
        else:
            self.replicas = Microsecrive.default_replicas

#orders = Microsecrive("app-order", "24.5")
#payment = Microsecrive("pay-app", "4.0", replicas=2)
#print(f"Service {orders.name} with version {orders.version} has {orders.replicas} replicas")

class Server:
    def __init__(self, name, location, status):
        self.name = name
        self.location = location
        self._status = status
        self.__access_key = "secretkey"
    
    def get_status(self):
        return self._status

    def stop_server(self):
        self._status = "stopped"


#host = Server(name="dev-controller", location="MSK", status="running")
#print(host._status)
#host.stop_server()
#print(host._status)

#try:
#    print(host._Server__access_key)
#except AttributeError as err:
#    print(f"{err}")

class MonitoringTools:
    def __init__(self, name):
        self.name = name

    def collect_metrics(self):
        return "Basic metrics"
    
class Prometheus(MonitoringTools):
    def __init__(self, name, version):
        super().__init__(name)
        self.version = version

    def collect_metrics(self):
        metrics = super().collect_metrics()
        return f"{metrics} with custom prom metrics"
    
prom = Prometheus("dev-monitoring", "5")
print(prom.collect_metrics())