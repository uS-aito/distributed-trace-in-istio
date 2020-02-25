from flask import Flask
from flask import request, abort
import os
import requests
import socket
import sys
import logging
import time

app = Flask(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

TRACE_HEADERS_TO_PROPAGATE = [
    'X-Ot-Span-Context',
    'X-Request-Id',

    # Zipkin headers
    'X-B3-TraceId',
    'X-B3-SpanId',
    'X-B3-ParentSpanId',
    'X-B3-Sampled',
    'X-B3-Flags',

    # Jaeger header (for native client)
    "uber-trace-id"
]

@app.route('/')
def root():
    return "I am service2. Please request to /trace/2."

@app.route('/trace/<service_number>')
def trace(service_number):

    # リクエストヘッダをログに保存
    # B3系のヘッダが入っていると思われるので、それを確認する
    logging.info("Recieved header is below.")
    logging.info(str(request.headers))

    # servicenumberを確認して1ならリクエストを行う、異なっているならInvalid Requestを返す
    headers = {}
    if int(service_number) == 2:
        # 分散トレーシング系のヘッダがあれば、次に伝播させるためにリクエストヘッダに入れる
        for header in TRACE_HEADERS_TO_PROPAGATE:
            if header in request.headers:
                headers[header] = request.headers[header]

        # 自分が送信するヘッダをログに保存
        logging.info("Sending header is below.")
        logging.info(str(headers))

        time.sleep(2)

        res = requests.get("http://service3:8082/trace/3", headers=headers, timeout=10.0)
        if res.status_code == 200:
            return res.text
    else:
        abort(400, "Invalid service number")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error("usage: %s port" % (sys.argv[0]))
        sys.exit(-1)

    p = int(sys.argv[1])
    logging.info("start at port %s" % (p))
    app.run(host='0.0.0.0', port=p, debug=True, threaded=True)
