import os
from flask import Flask, jsonify, Response, g, request
import uuid
import config
import json
import time


def create_app():
  app = Flask(__name__)
  
  @app.route("/")
  def hello_world():
     return "Hello World"
  
  return app
  
app = create_app()


@app.before_request
def before_request_func():
    execution_id = uuid.uuid4()
    g.start_time = time.time()
    g.execution_id = execution_id

    print(g.execution_id, "ROUTE CALLED ", request.url)

if __name__ == "__main__":
  #    app = create_app()
  print(" Starting app...")
  app.run(host="0.0.0.0", port=5000)