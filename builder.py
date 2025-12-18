class DeviceService():
    def __init__(self):
        self.queue=None
        self.storage=None
        self.db=None
        self.metrics = None
    def with_priority_queue(self,queue=None):
        self.queue=queue
        print("added queue to device service object")
        return self
    def with_storage(self,storage):
        self.storage=storage
        return self
    def with_metrices(self,metrices):
        self.metrics=metrices
        print("added metrices obj to deviceservice")
        return self

from abc import abstractmethod,ABC
class storage(ABC):
    @abstractmethod
    def upload():
        pass
class S3Storage(storage):
    def upload(self):
        print("s3 upload")


class AzureStorage(storage):
    def upload(self):
        print("blob upload")
    
ds=DeviceService().with_metrices(None).with_priority_queue(None).with_storage(AzureStorage())
#bridge
ds.storage.upload()
