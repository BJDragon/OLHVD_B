# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 20:16:59 2022

@author: pang
"""

import numpy as np
from OLHVD import olhvd
import matplotlib.pyplot as plt
import time







def setting(name):

    if name=='example1':
        def example1_1(x):
            #print(x)
            y=-(x[1]-1)**2-(x[0]-1)**2+1
            if y<0:
                return 0
            else:
                return 1
            
        lowb=np.array([0,0])
        upb=np.array([1,1])    
        return lowb,upb, [example1_1]
        
        
        
    if name=='example2': 
        def example2_1(x):
            #print(x)
            y=min([max([0.5-x[0],0.5-x[1]]),(x[0]**2+x[1]**2-0.25)])
            if y<0:
                return 0
            else:
                return 1
              
        lowb=np.array([0,0])
        upb=np.array([1,1])    
        return lowb,upb, [example2_1]

    if name == 'mine':
        def e(x):
            # print(x)
            y1 = x[0] - x[3] + x[4]
            y2 = x[2] - x[0] + x[1]
            y3 = x[5] - x[3] + x[4]
            y = min([y1, y2, y3])
            if y < 0:
                return 0
            else:
                return 1

        lowb = np.array([0, 0, 0, 0, 0, 0])
        upb = np.array([1, 1, 1, 1, 1, 1])
        return lowb, upb, [e]

if __name__ == '__main__':
    
    start_time=time.time()

    e='mine'
    lowb,upb,const=setting(e)
    n_points=200
    n_dim=6


    
    lhd=olhvd(n_points,n_dim,lowb,upb,const,Imax=800,opt=True)
    result=lhd.run()
    mm_samples=lhd.select_samples
    np.save('result.npy', result)

    end_time = time.time()
    print("Times Cost:", end_time - start_time)
    # plt.figure(2)
    # plt.scatter(mm_samples[:,0],mm_samples[:,1])
    # plt.scatter(result[:,0],result[:,1])
    # plt.show()