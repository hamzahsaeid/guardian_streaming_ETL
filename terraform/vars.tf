variable "stream_name" {
    type = string
    default = "Guardian_content"
    description = "The name of the Kinesis stream"
}

variable "lambda_name" {
    type = string
    default = "lambda_handler"
}

variable "python_runtime" {
    type = string
    default = "python3.12"
}