
# factor: del(dc)/delOmega_lambda/m
def dOm(z, Omega):
    dc_list = []
    for i in range(lenz):
        
        H0, Omega_m0, Omega_l0  = theta[0], theta[1], theta[2]
        
        if Omega == 1:        #Omega_Lambda case
            int_arg = lambda z: -(0.5) * ((Omega_l0 + (Omega_m0 * ((1 + z) ** 3)))) ** (3/2)
            d = quad(int_arg, 0, z[i])
        
        else:                #Omega_m case
            
            int_arg = lambda z: -((1 + z) ** 3) * (0.5) * ((Omega_l0 + (Omega_m0 * ((1 + z) ** 3)))) ** (3/2)
            d = quad(int_arg, 0, z[i])
        
               
        dc_list.append(d[0])

    return np.array(dc_list)


#delmu/delH0
delmuH0 =  []

#delmu/delOmegalambda
delmuOL = []

#delmu/delOmegam
delmuOM = []

for k in range(lenz):
    delmuH0i =(- 5) / (H0 * ln(10))
    delmuOLi = (5 / (Dl(z, theta)[k] * ln(10)) * dOm(zobs, 1)[k])
    delmuOMi = (5 / (Dl(z, theta)[k] * ln(10)) * dOm(zobs, 2)[k])
    delmuOL.append(delmuOLi)
    delmuOM.append(delmuOMi)
    delmuH0.append(delmuH0i)


der = [delmuH0, delmuOL, delmuOM] #list of derivatives from mu

#Fisher Matrix
list_mn = []
for n in der:
    list_m = []
    for m in der:
        list_d = []
        for i in range(lenz):
            di = (1 / (sigma[i]) ** 2) * ( n[i] * m[i])
            list_d.append(di)
        list_m.append(sum(list_d))
    list_mn.append(list_m)
    
#Parameters and data
theta = fit.x
H0 = theta[0]
z = zobs

# factor: del(dc)/delOmega_lambda/m
def dOm(z, Omega):
    dc_list = []
    for i in range(lenz):
        
        H0, Omega_m0, Omega_l0  = theta[0], theta[1], theta[2]
        
        if Omega == 1:        #Omega_Lambda case
            int_arg = lambda z: -(0.5) * ((Omega_l0 + (Omega_m0 * ((1 + z) ** 3)))) ** (3/2)
            d = quad(int_arg, 0, z[i])
        
        else:                #Omega_m case
            
            int_arg = lambda z: -((1 + z) ** 3) * (0.5) * ((Omega_l0 + (Omega_m0 * ((1 + z) ** 3)))) ** (3/2)
            d = quad(int_arg, 0, z[i])
        
               
        dc_list.append(d[0])

    return np.array(dc_list)


#delmu/delH0
delmuH0 =  []

#delmu/delOmegalambda
delmuOL = []

#delmu/delOmegam
delmuOM = []

for k in range(lenz):
    delmuH0i =(- 5) / (H0 * ln(10))
    delmuOLi = (5 / (Dl(z, theta)[k] * ln(10)) * dOm(zobs, 1)[k])
    delmuOMi = (5 / (Dl(z, theta)[k] * ln(10)) * dOm(zobs, 2)[k])
    delmuOL.append(delmuOLi)
    delmuOM.append(delmuOMi)
    delmuH0.append(delmuH0i)


der = [delmuH0, delmuOL, delmuOM] #list of derivatives from mu

#Fisher Matrix
list_mn = []
for n in der:
    list_m = []
    for m in der:
        list_d = []
        for i in range(lenz):
            di = (1 / (sigma[i]) ** 2) * ( n[i] * m[i])
            list_d.append(di)
        list_m.append(sum(list_d))
    list_mn.append(list_m)
    
fisher_matrix = np.array(list_mn)                
              

