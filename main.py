import string
from functions import *

def main():
    print("1. List all S3 buckets\n")
    print("2. Get object list in bucket\n")
    print("3. Copy object into another bucket\n")

if __name__ == "__main__":
    main()

option = int(input("Enter your option:"))

while option != 0:
    if option == 1:
        list_bucket()
    elif option == 2:
        bucket_name = input("Enter bucket name:")
        get_bucket_object(bucket_name)
    elif option == 3:
        source_bucket: String = input("Enter source bucket:")
        object_name: String = input("Enter object name:")
        destination_bucket: String = input("Enter bucket destination:")
        bucket_copy_object(destination_bucket, source_bucket, object_name)
    else:
        print("Invalid option")
    
    print()
    main()
    option = int(input("Enter your option:"))

print("Thank you")

