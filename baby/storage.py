from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
import vercel_blob
import os

@deconstructible
class VercelBlobStorage(Storage):
    def __init__(self, **kwargs):
        self.options = kwargs
        if 'token' not in self.options:
            self.options['token'] = os.environ.get('BLOB_READ_WRITE_TOKEN')

    def _open(self, name, mode='rb'):
        raise NotImplementedError("VercelBlobStorage does not support opening files directly.")

    def _save(self, name, content):
        if hasattr(content, 'read'):
            data = content.read()
        else:
            data = content
            
        # Ensure we are passing bytes
        if isinstance(data, str):
            data = data.encode('utf-8')
            
        # Vercel put returns a dict with 'url'
        # We enable random suffix to handle name collisions automatically
        put_options = self.options.copy()
        put_options['addRandomSuffix'] = 'true'
        
        resp = vercel_blob.put(name, data, options=put_options)
        return resp.get('url')

    def url(self, name):
        # The 'name' stored in the DB will be the full URL returned by _save
        return name

    def exists(self, name):
        if not name or not name.startswith('http'):
            return False
        try:
            vercel_blob.head(name, options=self.options)
            return True
        except:
            return False

    def delete(self, name):
        if name and name.startswith('http'):
            try:
                vercel_blob.delete(name, options=self.options)
            except:
                pass

    def size(self, name):
        if not name or not name.startswith('http'):
            return 0
        try:
            resp = vercel_blob.head(name, options=self.options)
            return resp.get('size', 0)
        except:
            return 0
