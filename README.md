# Guardian Streaming Data Pipeline

Python ETL pipeline that retrieves articles from the Guardian Open API and publishes them to an AWS Kinesis Data Stream. Supports both local CLI execution and AWS Lambda deployment.

---

## Functionality

 - Accepts a search term and optional date_from (YYYY-MM-DD)

 - Retrieves up to 10 recent Guardian articles

 - Secure API key retrieval via AWS Secrets Manager

 - Transforms to return only:

    - webPublicationDate

    - webTitle

    - webUrl

    - content_preview (first 1000 characters of article body)

 - Publishes each record to AWS Kinesis in JSON format

 ---

## Run Locally (CLI)

```bash
python -m src.cli "machine learning" Guardian_content 2025-01-01
```
---
## Example Lambda Event
```json
{
  "search_term": "machine learning",
  "date_from": "2025-01-01",
  "kinesis_stream": "Guardian_content"
}
```
---
## Testing
```bash
pytest -v
```

Covers:

 - Input validation

 - Secrets retrieval via AWS

 - Output structure verification

 - Kinesis publish success and failure scenarios

---

## Notes

 - No credentials are stored in the code

 - PEP 8 compliant and tested for security vulnerabilities. 
 
 - AWS Lambda-ready

 - Designed to operate within AWS Free Tier limits

---

 ## Future Improvements

 - Optional S3 or DynamoDB storage for long-term storage
 - Integrate automated CI/CD Deployment