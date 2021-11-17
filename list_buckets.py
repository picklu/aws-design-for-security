import boto3


s3 = boto3.resource('s3')

def list_bucket_objects():
    """ list all the objects in all the buckets 
    """
    items = {}

    for bucket in s3.buckets.all():
        items[bucket.name] = []
        for object in bucket.objects.all():
            items[bucket.name].append(object.key)
    
    return items


if __name__ == "__main__":
    items = list_bucket_objects()
    for bucket_name in items.keys():
        print("==>", bucket_name)
        for object_key in items[bucket_name]:
            print("   *", object_key)
        
    print("done!")