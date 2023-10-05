import json
from sqlquery import listToProcess
from producer import streamTable
from time import time

# import requests


def lambda_handler(event, context):
    print('calling listToProcess')
    records = listToProcess()
    streamTable(recordList=records)
    # for r in records:
    #     # print(f"{r['rowguid']}\t{r['PasswordHash']}\t{r['BusinessEntityID']}")
    #     msg = {
    #         'skq': str(r['rowguid']),
    #         'WarehouseId': r['PasswordHash'],
    #         'BackorderQuantity': r['BusinessEntityID']}
    #     print(json.dumps(msg))
    #     # print(msg)
    print('done')
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
