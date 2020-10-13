from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.files.storage import default_storage
from io import BytesIO

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete= models.CASCADE)
	profile_pic = models.ImageField(default="default-avatar.png", upload_to='media/', null=True, blank=True)

	def __str__(self):
		return self.user.username.capitalize() + " profile"

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		if self.profile_pic != "default-avatar.png":

			memfile = BytesIO()
			
			img = Image.open(self.profile_pic)

			if img.mode in ("RGBA", "P"):
				img = img.convert("RGB")

			if img.height > 300 or img.width > 300:
				output_size = (300, 300)
				img.thumbnail(output_size, Image.ANTIALIAS)
				img.save(memfile, 'JPEG', quality=95)
				default_storage.save(self.profile_pic.name, memfile)
				memfile.close()
				img.close()

				# img_size = (300, 300)
				# img.thumbnail(img_size)
				# img.save(self.profile_pic)