#!/bin/env python3

import os
import sys
import time
import json
import psycopg2
from flask import Flask, request, jsonify
import hvac
import logging


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

    with open('/vault-db-secrets/token', 'r') as f:
        vaultToken = f.read().strip()
    
    vclient = hvac.Client(url=os.environ['VAULT_ADDR'], token=vaultToken)
    dbPassword = vclient.read('dbs/creds/testdb')

    @app.route('/health')
    def health():
        try:
            conn = psycopg2.connect(password=dbPassword['data']['password'], port="5432", host=os.environ['DB_HOST'], dbname=os.environ['DB_NAME'], user=dbPassword['data']['username'])
            return "OK", 200
        except Exception as e:
            logging.error(e)
            return "ERROR", 500
    return app