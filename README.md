# prometheus-grafana-production-stack
Description:Observability stack with Prometheus, Grafana, and custom Python metrics exporter (Docker Compose)
Topics: prometheus grafana observability monitoring python docker prometheus

# Observability Platform Reference Implementation

Production-ready observability stack featuring:
- Prometheus with custom scrape configurations  
- Grafana with pre-provisioned dashboards  
- Custom Python metrics exporter (HTTP + system metrics)  
- Fully containerized using Docker Compose

Perfect baseline for SRE, Platform Engineering, and Backend roles.

![Dashboard Overview](screenshots/dashboard-overview.png)

## Stack
- Prometheus 
- Grafana 
- Python 
- Docker Compose

# Access
 Grafana → http://localhost:3000 (admin / admin)
 Prometheus → http://localhost:9090
 Custom Exporter → http://localhost:8000/metrics
 Targets status → http://localhost:9090/targets

# Features
 Real-time CPU, memory, and process metrics
 Custom HTTP request counters with labels
 Auto-provisioned Grafana dashboards
 Clean Prometheus configuration with relabeling ready

# Screenshots
 CPU & Memory
 Custom HTTP Metrics
 Prometheus Targets
