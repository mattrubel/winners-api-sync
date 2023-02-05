import os

from endpoints.sports import Sports

API_KEY = os.environ['API_KEY']
BASE_URL = os.environ['BASE_URL']
LOGGING_TABLE_NAME = os.environ['LOGGING_TABLE_NAME']
S3_BUCKET = os.environ['S3_BUCKET']


def main():
    sports = Sports(
        API_KEY,
        BASE_URL,
        LOGGING_TABLE_NAME,
        S3_BUCKET,
    )
    payload = sports.call_endpoint()
    sports.export_to_s3(payload)


if __name__ == '__main__':
    main()
