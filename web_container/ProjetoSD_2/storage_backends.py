from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    bucket_name = 'projetosd-static'
    location = 'media'
    file_overwrite = True


class StaticStorage(S3Boto3Storage):
    bucket_name = 'projetosd-static'
    location = 'static'
