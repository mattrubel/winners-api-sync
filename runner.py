import os

from endpoints.game_odds import GameOdds

API_KEY = os.environ['API_KEY']
BASE_URL = os.environ['BASE_URL']
LOGGING_TABLE_NAME = os.environ['LOGGING_TABLE_NAME']
S3_BUCKET = os.environ['S3_BUCKET']
SPORTS_DYNAMODB_TABLE = os.environ['SPORTS_DYNAMODB_TABLE']
GAME_DYNAMODB_TABLE = os.environ['GAME_DYNAMODB_TABLE']
ODDS_DYNAMODB_TABLE = os.environ['ODDS_DYNAMODB_TABLE']


def main():
    # sports = Sports(
    #     API_KEY,
    #     BASE_URL,
    #     LOGGING_TABLE_NAME,
    #     S3_BUCKET,
    #     SPORTS_DYNAMODB_TABLE
    # )
    # sports_payload = sports.call_endpoint()
    # sports.export_to_s3(sports_payload)
    # sports.write_to_dynamo(sports_payload)

    odds = GameOdds(
        API_KEY,
        BASE_URL,
        LOGGING_TABLE_NAME,
        S3_BUCKET,
        GAME_DYNAMODB_TABLE,
        ODDS_DYNAMODB_TABLE,
        'baseball_mlb'
    )

    odds_payload = odds.call_endpoint()
    odds.export_to_s3(odds_payload)


if __name__ == '__main__':
    main()
