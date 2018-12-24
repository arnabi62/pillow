
# coding: utf-8

# In[11]:


from PIL import Image

image = Image.open('C:\\Users\\Amit Kumar Mitra\\Desktop\\IMG-20180304-WA0002.jpg')


# In[12]:


image.show()


# In[14]:



print(image.format) # Output: JPEG


# In[15]:


# The pixel format used by the image. Typical values are “1”, “L”, “RGB”, or “CMYK.”
print(image.mode) # Output: RGB


# In[16]:


# Image size, in pixels. The size is given as a 2-tuple (width, height).
print(image.size) # Output: (1200, 776)


# In[17]:


image = Image.open('C:\\Users\\Amit Kumar Mitra\\Desktop\\IMG-20180304-WA0002.jpg')
image.save('C:\\Users\\Amit Kumar Mitra\\Desktop\\IMG-20180304-WA0002.jpg')


# In[18]:


#Resizing an Image
image = Image.open('C:\\Users\\Amit Kumar Mitra\\Desktop\\IMG-20180304-WA0002.jpg')
new_image = image.resize((400, 400))
new_image.save('C:\\Users\\Amit Kumar Mitra\\Desktop\\IMG-20180304-WA0002.jpg')

print(image.size) # Output: (1200, 776)
print(new_image.size) # Output: (400, 400)


# In[19]:


#Creating Thumbnail of an image
image = Image.open('C:\\Users\\Amit Kumar Mitra\\Desktop\\IMG-20180304-WA0002.jpg')
image.thumbnail((400, 400))
image.save('C:\\Users\\Amit Kumar Mitra\\Desktop\\IMG-20180304-WA0002.jpg')

print(image.size) # Output: (400, 258)


# In[20]:


#Cropping of image
image = Image.open('C:\\Users\\Amit Kumar Mitra\\Desktop\\IMG-20180304-WA0002.jpg')
#box = (150, 200, 600, 600)
#cropped_image = image.crop(box)
#cropped_image.save('C:\\Users\\Amit Kumar Mitra\\Desktop\\IMG-20180304-WA0002.jpg')


# In[21]:


#Pasting an Image
image = Image.open('C:\\Users\\Amit Kumar Mitra\\Desktop\\IMG-20180304-WA0002.jpg')
logo = Image.open('C:\\Users\\Amit Kumar Mitra\\Desktop\\IMG-20180304-WA0002.jpg')
image_copy = image.copy()
position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
image_copy.paste(logo, position)
image_copy.save('C:\\Users\\Amit Kumar Mitra\\Desktop\\IMG-20180304-WA0002.jpg')

