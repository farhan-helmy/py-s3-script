from tokenize import String
import boto3
import time

dev = boto3.session.Session(profile_name='nih-python')
s3 = dev.resource('s3')
s3object = dev.client('s3')

def list_bucket():
    for bucket in s3.buckets.all():
        print(bucket.name)

def get_bucket_object(bucket_name: String):
    bucket =  s3.Bucket(bucket_name)

    for bucket_object in bucket.objects.all():
        print(bucket_object.key)

def bucket_copy_object(bucket_destination_name: String, source_bucket: String, object_name: String):
    copy_source = {
      'Bucket': source_bucket,
      'Key': object_name
    }

    s3object.copy_object(CopySource = copy_source, Bucket = bucket_destination_name, Key = object_name)

def bucket_copy_change_name(bucket_destination_name: String, source_bucket: String, object_name: String):
    copy_source = {
      'Bucket': source_bucket,
      'Key': object_name
    }

    date_now = get_time()

    updated_object = object_name+date_now
    
    s3object.copy_object(CopySource = copy_source, Bucket = bucket_destination_name, Key = updated_object)

def get_time():
    current_time = time.localtime()
    final_time = time.strftime("%m-%d-%Y", current_time)
    print(final_time)
    return final_time