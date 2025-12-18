from abc import ABC , abstractmethod
class Storage(ABC):
    @abstractmethod
    def upload(self,file_name: str) -> None:
        pass
class AzureStorage(Storage):
    def test_upload(self):
        pass
    # def upload(self):
    #     print("uploading to blob storage")
    #     return
class AwsStorage(Storage):
    # def __init__():
    #     self.BucketName
    def upload(self,file_name):
        print("uploading to s3")
        return 
    
    
if __name__=="__main__":
    print("Hi")
    import os 
    storage=None
    storage_type=os.getenv("awdawd","aws")
    if storage_type=="aws":
        storage=AzureStorage()
    # storage.upload("awdaw")

