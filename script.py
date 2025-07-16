rom flask import Flask
from prometheus_client import Counter,generate_latest

app=Flask(_name_)
REQUEST_COUNT=Counter('web_requests_total','Total number of web requests')
@app.route('/')
def index():
    REQUEST_COUNT.inc()
    return "Hello from monoitring"

@app.rote('/metrics')
def metrics():
    return generate_latest()
if _name_ ==='__main':
    app.run(host='0.0.0.0')

