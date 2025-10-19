data "archive_file" "lambda" {
  type        = "zip"
  source_dir  = "${path.module}/../src"
  output_path = "${path.module}/../deployment_files/lambda_function.zip"
}

resource "aws_lambda_function" "guardian_lambda_resource" {
  filename         = data.archive_file.lambda.output_path
  function_name    = var.lambda_name
  runtime          = var.python_runtime
  role             = aws_iam_role.lambda_role.arn
  handler          = "lambda_handler.lambda_handler" 
  timeout          = 200
  source_code_hash = data.archive_file.lambda.output_base64sha256
  layers           = [aws_lambda_layer_version.dependencies.arn]
}
