import os, logging, time, json
import boto3

logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(name)s - %(funcName)s - %(message)s")
LOGGER = logging.getLogger(__name__)


############################################

AWS_SERVER_PUBLIC_KEY = '**'
AWS_SERVER_SECRET_KEY = '**'
REGION_NAME = '**'
DEFAULT_OUTPUT_FORMAT = '**'
STREAM_NAME = '**'
DATA ={
        "Data":"hello~from~the~other~side~i~must~have~called~thousands~times",
        }

############################################

try:
    session = boto3.Session(
        aws_access_key_id = AWS_SERVER_PUBLIC_KEY,
        aws_secret_access_key = AWS_SERVER_SECRET_KEY,
        region_name = REGION_NAME
    )
except Exception:
    print(str(Exception))
else:
    LOGGER.warning('AWS authentication was successfully established')

kinesis = session.client('kinesis')

# Send data
response = kinesis.put_record(
                StreamName=STREAM_NAME,
                Data=json.dumps(DATA),
                PartitionKey="1"
            )
time.sleep(1)

LOGGER.warning('pushing has done ! ! !')







