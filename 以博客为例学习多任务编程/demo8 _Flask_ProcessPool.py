from concurrent.futures import ProcessPoolExecutor
import flask
import json
import math

app = flask.Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    numbers_li = [int(u) for u in numbers.split(',')]
    results = process_pool.map(is_prime, numbers_li)
    return json.dumps(dict(zip(numbers_li, results)))

if __name__ == '__main__':
    process_pool = ProcessPoolExecutor()  # 线程之间共享全 局
    app.run()