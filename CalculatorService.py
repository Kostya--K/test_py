import requests
import json


def add(url, x, y, precision):
    temp = {
        "expr": "{}+{}".format(x, y),
        "precision": precision
    }
    js = json.dumps(temp, ensure_ascii=False)
    return requests.post(url, data=js).json()


def divide(url, x, y, precision):
    temp = {
        "expr": "{}/{}".format(x, y),
        "precision": precision
    }
    js = json.dumps(temp, ensure_ascii=False)
    return requests.post(url, data=js).json()


def multiply(url, x, y, precision):
    temp = {
        "expr": "{}*{}".format(x, y),
        "precision": precision
    }
    js = json.dumps(temp, ensure_ascii=False)
    return requests.post(url, data=js).json()


def subtract(url, x, y, precision):
    temp = {
        "expr": "{}-{}".format(x, y),
        "precision": precision
    }
    js = json.dumps(temp, ensure_ascii=False)
    return requests.post(url, data=js).json()


def sqrt(url, x):
    return requests.get(url + '?expr=sqrt({})'.format(x)).text


