# IAM roles for:
#   Lambda
#   Kinesis
#   Cloudwatch - logging
#   Secrets Manager
# -----------------------------------
# Lambda IAM Role, for:
# -----------------------------------
# Define
data "aws_iam_policy_document" "trust_policy" {
    statement {
      effect = "Allow"
      principals {
        type = "Service"
        identifiers = ["lambda.amazonaws.com"]
      }
      actions = ["sts:AssumeRole"]
    }
}

# Create
resource "aws_iam_role" "lambda_role" {
  name_prefix = "role-lambda"
  assume_role_policy = data.aws_iam_policy_document.trust_policy.json
}

#-------------------------------
# Lambda IAM Policy for Kinesis Write
#-------------------------------

# Define IAM policy
data "aws_iam_policy_document" "kinesis_policy_document" {
  statement {
    actions = ["kinesis:PutRecord",
                "kinesis:PutRecords"
    ]
    resources = ["*"]
  }
}

# Create IAM policy
resource "aws_iam_policy" "kinesis_policy" {
    name_prefix = "kinesis_policy_1"
    policy = data.aws_iam_policy_document.kinesis_policy_document.json
}

# Attach IAM policy doc
resource "aws_iam_role_policy_attachment" "kinesis_policy_attachment" {
    role = aws_iam_role.lambda_role.name
    policy_arn = aws_iam_policy.kinesis_policy.arn 
}

#----------------------------------
# Lambda IAM policy for Secrets Manager
#----------------------------------

# Define the IAM policy
data "aws_iam_policy_document" "secrets_manager_document" {
  statement {
    actions = ["secretsmanager:GetSecretValue"]
    resources = ["*"]
  }
}

# Create IAM policy
resource "aws_iam_policy" "secrets_manager_policy" {
    name_prefix = "Secrets_policy"
    policy      = data.aws_iam_policy_document.secrets_manager_document.json
}

# Attach IAM policy document
resource "aws_iam_role_policy_attachment" "secrets_manager_attachment" {
    role = aws_iam_role.lambda_role.name
    policy_arn = aws_iam_policy.secrets_manager_policy.arn
}

#----------------------------------------
# Lambda IAM role for CloudWatch
#---------------------------------------

# Define the policy
data "aws_iam_policy_document" "CloudWatch_document" {
    statement {
      actions = ["logs:CreateLogStream", "logs:PutLogEvents"]
      resources = ["arn:aws:logs:*:*:*"]
    }
  
}

# Create the policy
resource "aws_iam_policy" "CloudWatch_policy" {
    name_prefix = "Cloudwatch_policy_log"
    policy = data.aws_iam_policy_document.CloudWatch_document.json
}

# Attach policy document
resource "aws_iam_role_policy_attachment" "CloudWatch_policy_attachment" {
    role = aws_iam_role.lambda_role.name
    policy_arn = aws_iam_policy.CloudWatch_policy.arn
}
