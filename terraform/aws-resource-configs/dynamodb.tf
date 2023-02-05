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
