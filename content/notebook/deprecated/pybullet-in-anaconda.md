---
title: getting pyBullet working in Anaconda
tags:
- pybullet
- anaconda
- bash
- ubuntu
- simulation
- python
summary: " "
---


search keywords:

- python
- anaconda
- conda
- pybullet
- Mesa
- OpenGL
- radeonsi
- swrast


Trying to run a pyBullet script, I kept getting this kind of error:

```bash
pybullet build time: Dec  1 2021 18:34:28
startThreads creating 1 threads.
starting thread 0
started thread 0 
argc=2
argv[0] = --unused
argv[1] = --start_demo_name=Physics Server
ExampleBrowserThreadFunc started
X11 functions dynamically loaded using dlopen/dlsym OK!
X11 functions dynamically loaded using dlopen/dlsym OK!
libGL error: MESA-LOADER: failed to open radeonsi: /usr/lib/dri/radeonsi_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri)
libGL error: failed to load driver: radeonsi
libGL error: MESA-LOADER: failed to open radeonsi: /usr/lib/dri/radeonsi_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri)
libGL error: failed to load driver: radeonsi
libGL error: MESA-LOADER: failed to open swrast: /usr/lib/dri/swrast_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri)
libGL error: failed to load driver: swrast
Creating context
Failed to create GL 3.3 context ... using old-style GLX context
Failed to create an OpenGL context
```

I looked up this error, and there were lots of suggestions that didn't work, like exporting the right environment variable, installing the amdgpu-pro drivers, etc.  It turned out to be conflicts between the libstdc++ library expected by pyBullet and the version installed in my base anaconda environment.

After searching my anaconda directory for installations of libstdc++.so, I found multiple conflicting results:

Search:

```bash
sudo find / -wholename "*conda*/**/libstdc++.so*"
```

Result:

```
/home/danaukes/miniconda3/lib/libstdc++.so.6.0.28
/home/danaukes/miniconda3/lib/libstdc++.so
/home/danaukes/miniconda3/lib/libstdc++.so.6
/home/danaukes/miniconda3/pkgs/libstdcxx-ng-9.3.0-hd4cf53a_17/lib/libstdc++.so.6.0.28
/home/danaukes/miniconda3/pkgs/libstdcxx-ng-9.3.0-hd4cf53a_17/lib/libstdc++.so
/home/danaukes/miniconda3/pkgs/libstdcxx-ng-9.3.0-hd4cf53a_17/lib/libstdc++.so.6
/home/danaukes/miniconda3/pkgs/gcc_impl_linux-64-11.2.0-h82a94d6_13/x86_64-conda-linux-gnu/lib/libstdc++.so
/home/danaukes/miniconda3/pkgs/gcc_impl_linux-64-11.2.0-h82a94d6_13/x86_64-conda-linux-gnu/lib/libstdc++.so.6
/home/danaukes/miniconda3/pkgs/gcc_impl_linux-64-11.2.0-h82a94d6_13/x86_64-conda-linux-gnu/lib/libstdc++.so.6.0.29
/home/danaukes/miniconda3/pkgs/libstdcxx-ng-11.2.0-he4da1e4_13/lib/libstdc++.so
/home/danaukes/miniconda3/pkgs/libstdcxx-ng-11.2.0-he4da1e4_13/lib/libstdc++.so.6
/home/danaukes/miniconda3/pkgs/libstdcxx-ng-11.2.0-he4da1e4_13/lib/libstdc++.so.6.0.29
```

So I created a new environment, just for pybullet.

```bash
conda create -n pybullet
conda activate pybullet
conda install python
conda install pip
conda install -c conda-forge gcc
pip install pybullet
```

Spyder conflicts with this environment so I instead installed the ide-python package for atom.  See the instructions [here](/notebook/atom-for-python/)

## External Resources

* <https://askubuntu.com/questions/1352158/libgl-error-failed-to-load-drivers-iris-and-swrast-in-ubuntu-20-04>

