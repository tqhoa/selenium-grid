import os


class Config(object):
    HUB_PORT_4444_TCP_ADDR = os.getenv("HUB_PORT_4444_TCP_ADDR", "ADDR:NAME")
    HUB_PORT_4444_TCP_PORT = os.getenv("HUB_PORT_4444_TCP_PORT", "PORT:NUMBER")
