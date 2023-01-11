from prefect.filesystems import S3

s3 = S3(
    bucket_path="rend-prefect-s3/prod",
    aws_access_key_id="xxx",  # when creating a block, you can pass this value from CI/CD Secrets
    aws_secret_access_key="xxx",  # or retrieve those from environment variables
)
s3.save("rend-prefect-s3", overwrite=True)
