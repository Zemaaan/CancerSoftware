import os
from PIL import Image

# Rotate Image By 180 Degree

# This is Alternative Syntax To Rotate
# The Image
SeznamDatotek = os.listdir(r'C:\Users\Hrvoje\OneDrive - Univerza v Mariboru\Namizje\Cancer\Skin_Data\Cancer\Testing')
for Slika in SeznamDatotek:
	KompletnaPot = os.path.join(
		r"C:\Users\Hrvoje\OneDrive - Univerza v Mariboru\Namizje\Cancer\Skin_Data\Cancer\Testing", Slika)
	Original_Image = Image.open(KompletnaPot)
	rotated_image2 = Original_Image.transpose(Image.ROTATE_90)
	rotated_image1 = Original_Image.rotate(270)
	rotated_image3 = Original_Image.rotate(180)
	rotated_image1.save('C:\\Users\\Hrvoje\\OneDrive - Univerza v Mariboru\\Namizje\\Cancer\\Skin_Data\\Cancer\\AugmentiraniPodatki\\{0}'.format(Slika))
	rotated_image2.save('C:\\Users\\Hrvoje\\OneDrive - Univerza v Mariboru\\Namizje\\Cancer\\Skin_Data\\Cancer\\AugmentiraniPodatki270\\{0}'.format(Slika))
	rotated_image3.save('C:\\Users\\Hrvoje\\OneDrive - Univerza v Mariboru\\Namizje\\Cancer\\Skin_Data\\Cancer\\AugmentiraniPodatki180\\{0}'.format(Slika))

print(SeznamDatotek)
