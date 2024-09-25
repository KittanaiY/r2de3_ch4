from google.cloud import storage


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client() #สร้างstorage
    bucket = storage_client.bucket(bucket_name) #get bucket
    blob = bucket.blob(destination_blob_name) #สร้าง ไฟล์ที่จะถูกอัพโหลดไว้ขึ้นมาก่อน

    # Optional: set a generation-match precondition to avoid potential race conditions
    # and data corruptions. The request to upload is aborted if the object's
    # generation number does not match your precondition. For a destination
    # object that does not yet exist, set the if_generation_match precondition to 0.
    # If the destination object already exists in your bucket, set instead a
    # generation-match precondition using its generation number.
    generation_match_precondition = 0

    blob.upload_from_filename(source_file_name, if_generation_match=generation_match_precondition)
    #อัพไฟล์นั้นลง blob ที่เพิ่งสร้างไป
    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )


def download_byte_range(
    bucket_name, source_blob_name, start_byte, end_byte, destination_file_name
):
    """Downloads a blob from the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your GCS object
    # source_blob_name = "storage-object-name"

    # The starting byte at which to begin the download
    # start_byte = 0

    # The ending byte at which to end the download
    # end_byte = 20

    # The path to which the file should be downloaded
    # destination_file_name = "local/path/to/file"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name, start=start_byte, end=end_byte)

    print(
        "Downloaded bytes {} to {} of object {} from bucket {} to local file {}.".format(
            start_byte, end_byte, source_blob_name, bucket_name, destination_file_name
        )
    )


if __name__ =='__main__':
    command = input("Upload (u) or Download (d): ")
    bucket_name = input("Bucket name: ")
    file_name = input("File name: ")
    saved_name = input("Save into which name ? >> ")
    if saved_name is None or saved_name=="":
        saved_name = file_name.split("/")[-1]

    if command.strip().lower() == "upload" or command.strip.lower() == 'u':
        upload_blob(bucket_name,file_name,saved_name)
        # upload_blob("r2de3-workshop-gritta", "../README-cloudshell.txt", "hello_cloudshell")
    if command.strip().lower() == "download" or command.strip.lower() == 'd':
        download_byte_range(bucket_name, file_name,)
    else:
        print("Invalid Command")