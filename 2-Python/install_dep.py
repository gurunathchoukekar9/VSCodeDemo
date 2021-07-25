
import boto3
import botostubs

#......
#pip uninstall boto3 botostubs
#pip install boto3 botostubs
#......


client = boto3.client('s3',region_name='us-east-1')


print("Bucket List....")
print("...")


#....
#intelliscense
#....
result = client.list_buckets()


for itm in result["Buckets"]:
    print(itm["Name"])

print("...")
print("script completed..")

