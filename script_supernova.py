# NumCosmo:
try:
  import gi
  gi.require_version('NumCosmo', '1.0')
  gi.require_version('NumCosmoMath', '1.0')
except:
  pass

from gi.repository import GObject
from gi.repository import NumCosmo as Nc
from gi.repository import NumCosmoMath as Ncm

import matplotlib.pyplot as plt
import scipy
import numpy as np
from sympy import *
import scipy.stats as scs

from numpy import sqrt, log10, sinh, exp
from numpy import log as ln

from scipy.integrate import quad #Integrate
from sympy import diff, Symbol, symbols #Derivative
from scipy.optimize import minimize

c = 3*(10**5)

Ncm.cfg_init ()
cosmo = Nc.HICosmoDEXcdm() #Cosmology object

ser = Ncm.Serialize.new(0)
data = ser.from_file("/home/cinthia/NumCosmo/data/nc_data_snia_diag_legacy.obj")
lenz = data.y.len()

muobs = []
sigma = []
zobs = []
for i in range(lenz):
    mi = data.y.get(i)
    si = data.sigma.get(i)
    zi = data.x.get(i)
    
    muobs.append(mi)
    sigma.append(si)
    zobs.append(zi)

muobs = np.array(muobs)
zobs = np.array(zobs)
sigmaobs = np.array(sigma)
