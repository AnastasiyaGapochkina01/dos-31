resource "aws_s3_bucket" "test-bucket" {
  bucket = "testing-1771352896"
}

resource "aws_s3_bucket" "tfstates-bucket" {
  bucket = "dos-31-tfstate-1771351893"
}

resource "aws_dynamodb_table" "state_lock_table" {
  name         = "terraform_state_lock"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"
  attribute {
    name = "LockID"
    type = "S"
  }
}
