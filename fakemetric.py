from prometheus_client import start_http_server, Gauge, Counter
import random
import time


cpu = Gauge('fake_server_cpu_percent', 'Fake CPU usage')
mem = Gauge('fake_server_memory_gb', 'Fake memory usage in GB')
requests = Counter('fake_http_requests_total', 'Total requests', ['code'])
errors = Counter('fake_http_errors_total', 'Total errors')


start_http_server(8000)
print("Fake metrics live at http://localhost:8000/metrics")
print("Updating every 15 seconds...")

while True:
    cpu.set(random.uniform(5, 95))                    
    mem.set(round(random.uniform(0.5, 7.5), 2))       
    requests.labels(code="200").inc(random.randint(5, 30))
    if random.random() < 0.05:                        
        requests.labels(code="500").inc()
        errors.inc()
    time.sleep(15)