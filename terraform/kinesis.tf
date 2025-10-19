# The infrastructure that terraform creates & configures


# Kinesis stream is created using the variable name
resource "aws_kinesis_stream" "my_stream" {
    name = var.stream_name
    shard_count = 1
    retention_period = 72 # Length of time the records will in accessible (hours)
    region = "eu-north-1"

    stream_mode_details {
        stream_mode = "PROVISIONED"
    }
}

# Create a SSM parameter to store the stream name, single source of truth
resource "aws_ssm_parameter" "stream_name" {
  name = "/temp/kinesis/stream_name"
  type = "String"
  value = aws_kinesis_stream.my_stream.name
}