import os

from endpoints.game_odds import GameOdds
from endpoints.sports import Sports

API_KEY = os.environ['API_KEY']
BASE_URL = os.environ['BASE_URL']
LOGGING_TABLE_NAME = os.environ['LOGGING_TABLE_NAME']
S3_BUCKET = os.environ['S3_BUCKET']
SPORTS_DYNAMODB_TABLE = os.environ['SPORTS_DYNAMODB_TABLE']
GAME_DYNAMODB_TABLE = os.environ['GAME_DYNAMODB_TABLE']
ODDS_DYNAMODB_TABLE = os.environ['ODDS_DYNAMODB_TABLE']


def handle_sports():
    sports = Sports(
        API_KEY,
        BASE_URL,
        LOGGING_TABLE_NAME,
        S3_BUCKET,
        SPORTS_DYNAMODB_TABLE
    )
    sports_payload = sports.call_endpoint()
    sports.export_to_s3(sports_payload)
    sports.write_to_dynamo(sports_payload)


def handle_game_odds(sport):
    odds = GameOdds(
        API_KEY,
        BASE_URL,
        LOGGING_TABLE_NAME,
        S3_BUCKET,
        GAME_DYNAMODB_TABLE,
        ODDS_DYNAMODB_TABLE,
        sport
    )

    odds_payload = odds.call_endpoint()
    odds.export_to_s3(odds_payload)
    odds.write_to_dynamo(odds_payload)


def handler(event, _):
    event_type = event["type"]

    if event_type == "sports":
        handle_sports()
    elif event_type == "game_odds":
        handle_game_odds(event["sport"])
    else:
        raise RuntimeError(f"Event type {event_type} not yet implemented")
