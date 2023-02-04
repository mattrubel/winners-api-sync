import os

from endpoints.sports import Sports

API_KEY = os.environ['API_KEY']
BASE_URL = os.environ['BASE_URL']  # "https://api.the-odds-api.com/v4/sports/"
S3_BUCKET = os.environ['S3_BUCKET']
S3_ACCESS_KEY = os.environ['S3_ACCESS_KEY']
S3_SECRET_ACCESS_KEY = os.environ['S3_SECRET_ACCESS_KEY']


def main():
    sports = Sports(API_KEY, BASE_URL, S3_BUCKET, S3_ACCESS_KEY, S3_SECRET_ACCESS_KEY)
    payload = sports.call_endpoint()
    sports.export_to_s3(payload)


if __name__ == '__main__':
    main()
