
# OTEL Collector example

This repo contains a minimal example for to set up monitoring with Opentelemetry. In this example, there's a barebones Flask application, a "sidecar" collector, and a terminal collector. In prod, you would forward traffic from the terminal collector to whatever backend system you want to use.

```
┌───┐   ┌────────────┐   ┌──────────────┐
│app│──►│otel-sidecar│──►│otel-collector│
└───┘   └────────────┘   └──────────────┘
```
