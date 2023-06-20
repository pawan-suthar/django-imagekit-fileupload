from .import imagekit

import base64


class ImageKitClient():
    def __init__(self,file):
        self.file = self.convertbin(file)
        self.file_name = file.name

    # method for conver file
    def convertbin(self,file):
        self.binfile = base64.b64encode(file.read())
        return self.binfile

    @property
    def upload(self):

        result = imagekit.upload_file(
            file=self.file,
            file_name=self.file_name,
        )
        return result.response_metadata.raw