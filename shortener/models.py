from django.db import models
import base64
import random
import string



# Create your models here.



class Link(models.Model):
    target_url = models.CharField(max_length=50000)
    encoded = models.CharField(blank=True, null=True, max_length=1000)
    


    def url_encode(self):
        target_url = self.target_url
        #key = Fernet.generate_key()
        #fernet = Fernet(key)
        enc_url = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
        
        #target_url_bytes = target_url.encode("ascii")
        #base64_bytes = base64.b64encode(target_url_bytes)
        #base64_string = base64_bytes.decode("ascii")

        sliced_string = enc_url[slice(8)]

        return sliced_string

    



    def save(self, *args, **kwargs):
        self.encoded = self.url_encode()


        super().save(*args, **kwargs)



