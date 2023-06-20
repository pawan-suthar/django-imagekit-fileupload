
from imagekitio import ImageKit
from django.conf import settings

imagekit = ImageKit(
    private_key=settings.IMAGEKIT_PVT_KEY,
    public_key=settings.IMAGEKIT_PUBLIC_KEY,
    url_endpoint =settings.IMAGE_KIT_URLENDPOINT
)