resource "aws_dynamodb_table" "winners_api_sync_endpoint_logging_table" {
  name         = "winners-api-sync-endpoint-logging"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "log_key"

  global_secondary_index {
    hash_key        = "call_type"
    range_key       = "date"
    name            = "call_type_date_idx"
    projection_type = "ALL"
  }

  attribute {
    name = "log_key"
    type = "S"
  }

  attribute {
    name = "call_type"
    type = "S"
  }

  attribute {
    name = "date"
    type = "S"
  }
}


resource "aws_dynamodb_table" "winners_sports_table" {
  name         = "winners-sports"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "sport_key"

  global_secondary_index {
    hash_key        = "collect"
    range_key       = "sport_key"
    name            = "collect_sport_key_idx"
    projection_type = "ALL"
  }

  attribute {
    name = "sport_key"
    type = "S"
  }

  attribute {
    name = "collect"
    type = "B"
  }

}

resource "aws_dynamodb_table" "winners_games_table" {
  name         = "winners-games"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "game_key"

  global_secondary_index {
    hash_key        = "sport_key"
    range_key       = "game_key"
    name            = "collect_sport_key_idx"
    projection_type = "ALL"
  }

  attribute {
    name = "game_key"
    type = "S"
  }

  attribute {
    name = "sport_key"
    type = "S"
  }
}

resource "aws_dynamodb_table" "winners_odds_table" {
  name         = "winners-odds"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "game_key"
  range_key    = "last_updated"

  attribute {
    name = "game_key"
    type = "S"
  }

  attribute {
    name = "last_updated"
    type = "S"
  }

  lifecycle {
    prevent_destroy = true
  }
}
