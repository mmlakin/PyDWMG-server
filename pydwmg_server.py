""" pydwmg_server.py - PyDWMG Server

Does stuff...

"""
import os
import json
import logging
import boto3


SSM_REGION = "us-east-1"
SSM_PARAMETER_PREFIX = "/pydwmg/"
# Set up logging used for troubleshooting/testing.
if len(logging.getLogger().handlers) == 0:
    logging.basicConfig(
        format="%(levelname)s: %(message)s",
        level=os.getenv("LOG_LEVEL", "WARNING"),
    )
log = logging.getLogger()
log.setLevel(os.getenv("LOG_LEVEL", "WARNING"))


def get_parameters():
    ssm_parameters = [
        "token",
        "db",
    ]
    ssm_client = boto3.session.Session(region_name=SSM_REGION).client("ssm")
    for parameter_name in ssm_parameters:
        yield ssm_client.get_parameter(
            Name=f"{SSM_PARAMETER_PREFIX}{parameter_name}",
            WithDecryption=True,
        ).get("Parameter").get("Value")


def lambda_handler(event, context):
    url_parameters = event["queryStringParameters"]
    token = url_parameters["token"]
    update = url_parameters["update"]
    token, db = get_parameters()
    db = json.loads(db)
    db_version = db["v"]
    db_db = json.dumps(db["d"])
    log.info(f"{update=}")
    log.info(f"{db_version=}")
    log.info(f"{db_db=}")
