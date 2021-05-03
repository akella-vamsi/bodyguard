import re
import base64
dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
ImageData = request.POST.get('hidden_image_field')
ImageData = dataUrlPattern.match(ImageData).group(2)

# If none or len 0, means illegal image data
if (ImageData == None) or len(ImageData) == 0 :
    pass

# Decode the 64 bit string into 32 bit
ImageData = base64.b64decode(ImageData)