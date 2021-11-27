from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import random
import os
import h5py

##load the dataset
d = h5py.File('porositydataset.hdf5','a')
#load original images
og_images = np.zeros(d['Original Images'].shape)
og_images[:,:,:] = d['Original Images']
#load deformed images
deformed_images = np.zeros(d['Deformed Images'].shape)
deformed_images[:,:,:] = d['Deformed Images']
#load stress-strain data
data = np.zeros(d['Data'].shape)
data[:,:,:] = d['Data']
#separate stresses/strains, stresses in MPa, strain is unitless
SMises = data[:,0,:] #von Mises stress
S11 = data[:,1,:] #stress in 11 direction
S22 = data[:,2,:] #stress in 22 direction
SP = data[:,3,:] #pressure stress
strain = data[:,4,:]*0.006 #strain (have to multiply by 0.006 to get value)
#load youngs moduli, units are GPa
E = np.zeros(d['Youngs Modulus'].shape)
E[:] = d['Youngs Modulus']

#choose which run you want to look at
run = 0

#print youngs modulus
print('Youngs Modulus:',E[run],'GPa')

#plot images and stress response
fig = plt.figure()
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)
ax1.imshow(og_images[run,:,:,:])
ax1.title.set_text('Original Configuration')
ax1.set_xticks([])
ax1.set_yticks([])
ax2.imshow(deformed_images[run,:,:,:])
ax2.title.set_text('Deformed Configuration')
ax2.set_xticks([])
ax2.set_yticks([])
ax3.plot(strain[run,:],SMises[run,:],label='von Mises')
ax3.plot(strain[run,:],S11[run,:],label='S11')
ax3.plot(strain[run,:],S22[run,:],label='S22')
ax3.plot(strain[run,:],SP[run,:],label='Pressure')
ax3.title.set_text('Stress-Strain Response')
ax3.set_xlabel('Strain')
ax3.set_ylabel('Stress (MPa)')
ax3.legend()
plt.show()