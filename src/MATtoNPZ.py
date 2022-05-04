import scipy.io 
import numpy


mat = scipy.io.loadmat('MOGA142i_os.mat')

TR_SET=mat['TR_SET']
print(TR_SET.shape)
VA_SET=mat['VA_SET']
print(VA_SET.shape)
TE_SET=mat['TE_SET']
print(TE_SET.shape)

# print(TR_SET)

numpy.savez('MOGA_DATA_142i_os.npz',TR_SET=TR_SET,VA_SET=VA_SET,TE_SET=TE_SET)

print('OK')
