from sse.sse import Publisher
import json

publisher = Publisher()


def deneme_function():


    print("buradayım")

    publisher.publish(json.dumps([{"success": True}]))
