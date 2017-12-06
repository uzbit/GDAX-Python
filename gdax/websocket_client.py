#
# gdax/WebsocketClient.py
# Daniel Paquin
#
# Template object to receive messages from the gdax Websocket Feed

from __future__ import print_function
import time
import json

from threading import Thread
from websocket import create_connection, WebSocketConnectionClosedException, WebSocketBadStatusException


class WebsocketClient(object):
    def __init__(self, url="wss://ws-feed.gdax.com", products=None, message_type="subscribe"):
        self.url = url
        self.products = products
        self.type = message_type
        self.stop = False
        self.ws = None
        self.thread = None

    def start(self):
        self.thread = Thread(target=self._go)
        self.thread.start()
        #self.thread.join()

    def _go(self):
        while not self._connect():
            time.sleep(10)
            print("Error: Trying to connect...")
        self._listen()

    def _connect(self):
        if self.products is None:
            self.products = ["BTC-USD"]
        elif not isinstance(self.products, list):
            self.products = [self.products]

        if self.url[-1] == "/":
            self.url = self.url[:-1]

        try:
            self.ws = create_connection(self.url)
        except Exception as e:
            print("Error connecting: %s" % str(e))
            return False

        sub_params = {'type': 'subscribe', 'product_ids': self.products}

        if self.type == "heartbeat":
            sub_params = {"type": "heartbeat", "on": True}

        self.stop = False
        self.ws.send(json.dumps(sub_params))
        self.on_open()
        return True

    def _listen(self):
        while not self.stop:
            try:
                if int(time.time() % 30) == 0:
                    # Set a 30 second ping to keep connection alive
                    self.ws.ping("keepalive")
                msg = json.loads(self.ws.recv())
            except Exception as e:
                self.on_error(e)
            else:
                self.on_message(msg)

    def close(self):
        if not self.stop:
            if self.type == "heartbeat":
                self.ws.send(json.dumps({"type": "heartbeat", "on": False}))

            try:
                if self.ws:
                    self.ws.close()
            except WebSocketConnectionClosedException:
                pass

            self.stop = True
            self.on_close()
            self.ws = None

    def on_open(self):
        print("-- Subscribed! --\n")

    def on_close(self):
        print("\n-- Socket Closed --")

    def on_message(self, msg):
        print(msg)

    def on_error(self, e):
        print("Error: " + str(e))


if __name__ == "__main__":
    import gdax
    import time

    class MyWebsocketClient(gdax.WebsocketClient):
        def on_open(self):
            self.url = "wss://ws-feed.gdax.com/"
            self.products = ["BTC-USD", "ETH-USD"]
            self.message_count = 0
            print("Let's count the messages!")

        def on_message(self, msg):
            if 'price' in msg and 'type' in msg:
                print("Message type:", msg["type"], "\t@ %.3f" % float(msg["price"]))
            self.message_count += 1

        def on_close(self):
            print("-- Goodbye! --")

    wsClient = MyWebsocketClient()
    wsClient.start()
    print(wsClient.url, wsClient.products)
    # Do some logic with the data
    while wsClient.message_count < 500:
        print("\nMessageCount =", "%i \n" % wsClient.message_count)
        time.sleep(1)

    wsClient.close()
