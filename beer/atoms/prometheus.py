from prometheus_client import Counter
from prometheus_client import Gauge

def incCounter(name):
    c = Counter(name, "no desc")
    c.inc()

def setGauge(name, val):
    g = Gauge(name, "etc")
    g.set(val)
