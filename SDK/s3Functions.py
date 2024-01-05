import boto3
import io

# Open a session to be able to utilize the SDK
session = boto3.Session(profile_name='bvanek')

# Create a reference to the S3 bucket
s3 = session.client('s3')

# Displays all the names of our S3 buckets
def display_names():
    for bucket in s3.list_buckets()['Buckets']:
        print(bucket['Name'])
    print("------------------------------------------------------------")

# Creates an S3 bucket
def create_S3(name, region):
    if (region != "us-east-1"):
        s3.create_bucket(
            Bucket=name,
            CreateBucketConfiguration={
                'LocationConstraint': region,
            },
        )
    else:
        s3.create_bucket(
            Bucket=name,
        )

# Puts an item in our S3 bucket
def put_item(filename, bucketname):
    with open(filename, 'r') as file:
        response = s3.put_object(
            Body=file.read(),
            Bucket=bucketname,
            Key=filename,
        )
    # print(response)

# Gets an item from our S3 bucket
def get_item(filename, bucketname):
    response = s3.get_object(
        Bucket=bucketname,
        Key=filename
    )
    print("------------------------------------------------------------")
    print("File " + filename)
    print(response['Body'].read().decode('utf-8'))

# Lists all items inside an S3 bucket
def list_items(bucketname): 
    response = s3.list_objects(
        Bucket=bucketname,
    )
    # print(response)
    i = 1
    for o in response['Contents']:
        print("------------------------------------------------------------")
        filename = o.get('Key')
        data = s3.get_object(Bucket=bucketname, Key=filename)
        print("File " + filename)
        print(data['Body'].read().decode('utf-8'))
        i+=1
    print("------------------------------------------------------------")

# Deletes an item from our S3 bucket
def delete_item(filename, bucketname):
    s3.delete_object(
        Bucket=bucketname,
        Key=filename,
    )
    print("Deleted file " + filename)

# Deletes all items from an S3 bucket
def empty_bucket(bucketname): 
    item_list = s3.list_objects(
        Bucket=bucketname,
    )
    for item in item_list['Contents']:
        s3.delete_object(
            Bucket=bucketname,
            Key=item['Key'],
        )

# Deletes an S3 bucket
def delete_bucket(bucketname):
    response = s3.delete_bucket(
        Bucket=bucketname,
    )
    # print(response)
    

# Display names of all our S3 buckets
display_names()

# Creates an S3 bucket in us-east-1
create_S3("bvanek-demo", "us-east-1")

# Display names of all our S3 buckets to ensure bucket was created
display_names()

# Puts two text files inside of the S3 bucket
put_item('test.txt', 'bvanek-demo')
put_item('NewFile.txt', 'bvanek-demo')

# Display a particular item in our S3 bucket
get_item("NewFile.txt", "bvanek-demo")

# # Display all the items in our S3 bucket
list_items("bvanek-demo")

# # Delete a particular item in our S3 bucket
delete_item("NewFile.txt", "bvanek-demo")
delete_item("test.txt", "bvanek-demo")

# # Puts two text files inside of the S3 bucket
put_item('test.txt', 'bvanek-demo')
put_item('NewFile.txt', 'bvanek-demo')

# # Empties a bucket of all the files inside of the S3 bucket
empty_bucket('bvanek-demo')

# # Deletes our S3 bucket
delete_bucket("bvanek-demo")

# # Ensures that our S3 bucket was deleted
display_names()