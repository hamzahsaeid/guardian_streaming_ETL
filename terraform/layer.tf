resource "null_resource" "create_dependencies" {
  provisioner "local-exec" {
    command = "mkdir -p ${path.module}/../layer_dependencies/python ${path.module}/../deployment_files && pip install -r ${path.module}/../requirements.txt -t ${path.module}/../layer_dependencies/python" 
  }
  triggers = {
    always_run = timestamp()
  }
}

data "archive_file" "layer_code" {
    type = "zip"
    source_dir = "${path.module}/../layer_dependencies"
    output_path = "${path.module}/../deployment_files/lambda_handler_layer.zip"
    depends_on = [null_resource.create_dependencies]
}

resource "aws_lambda_layer_version" "dependencies" {
  layer_name = "HandlerDependency"
  filename = data.archive_file.layer_code.output_path
  source_code_hash = data.archive_file.layer_code.output_base64sha256
}