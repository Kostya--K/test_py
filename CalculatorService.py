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


if __name__ == "__main__":
    URL = 'http://api.mathjs.org/v1/'
    # print add(URL, 100, 10, 2)
    print divide(URL, "bg", 0, 5)
    print multiply(URL, 10.356, 10.2, 5)
    # print subtract(URL, 100, 10)
    # print sqrt(URL, 100)
    print sqrt(URL, -6)
