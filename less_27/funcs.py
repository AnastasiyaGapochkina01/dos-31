def simple_hello(name):
    print(f"Hello, {name}")

def simple_summ(a, b):
    return a + b

def summarize(*args):
    print(f"{args} with type {type(args)}")
    sum_numbers = 0
    for num in args:
        sum_numbers += num
    return sum_numbers


def send_message(recepient, subject="Empty"):
    msg = "ALERT: dev-compute-5 is down"
    print(f"Sending message about {subject} message: {msg} to {recepient}")


def db_connect(host, user, passwd="SuPeRsEcReT!23", **connection_params):
    print(f"Connecting to {host} with user {user}")
    print(f"Additional params: {connection_params}")


simple_sum_lambda = lambda a, b: a + b

logs = [
    ("INFO", "Service started on port 8080"),
    ("ERROR", "Database coonect failed"),
    ("WARNING", "High memory usage"),
    ("ERROR", "Server is down")
]

error_logs = list(filter(lambda log: log[0] == "ERROR", logs))
print(error_logs)

