import numpy as n
import matplotlib.pyplot as plt
import h5py


h=h5py.File("heimdall_lowel.h5","r")
print(h.keys())
plt.figure(figsize=(8,10))
plt.subplot(411)
plt.ylabel("Latitude")

plt.pcolormesh(h["t_unix"][()].astype('datetime64[s]'),h["lat"][()],n.log10(h["ne"]),cmap="turbo",vmin=10,vmax=12.5)
cb=plt.colorbar()
cb.set_label(r"$n_e$ ($m^{-3}$)")

plt.subplot(412)
plt.ylabel("Latitude")

plt.pcolormesh(h["t_unix"][()].astype('datetime64[s]'),h["lat"][()],h["Te"],cmap="turbo",vmin=0,vmax=4000)
cb=plt.colorbar()
cb.set_label(r"$T_e$ (K)")

plt.subplot(413)
plt.ylabel("Latitude")

plt.pcolormesh(h["t_unix"][()].astype('datetime64[s]'),h["lat"][()],h["Ti"],cmap="turbo",vmin=0,vmax=3000)
cb=plt.colorbar()
cb.set_label(r"$T_i$ (K)")

plt.subplot(414)
plt.ylabel("Latitude")
plt.pcolormesh(h["t_unix"][()].astype('datetime64[s]'),h["lat"][()],h["vi"],cmap="seismic",vmin=-800,vmax=800)
cb=plt.colorbar()
cb.set_label(r"$v_i$ (m/s negative away from radar)")
plt.xlabel("Date")
plt.tight_layout()
plt.show()
h.close()

