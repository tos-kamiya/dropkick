# dropkick
Repeat a command line for each file dropped (as a practice of AppImage)

## requirement

* Python3, PyQt5 and venv.

```
sudo apt install python3-pyqt5
sudo apt install pytohn3-venv
```

* AppImageTool

Download AppImageTool and put it some directory.

## build

```
cd dropkick
python3 -m venv venv
rsync -av /usr/lib/python3/dist-packages/PyQt5/ venv/lib/python3.6/site-packages/PyQt5/
cp /usr/lib/python3/dist-packages/sip.cpython-*.so venv/lib/python3.6/site-packages/
chmod +x AppRun
cd ..
env ARCH=x86_64 /path/to/appimagetool-x86_64.AppImage dropkick/
```

## usage

Run dropkick with a target command line:

```
dropkick-x86_64.AppImage the-command-line
```

When a window appears, drag-and-drop a file to the window.
The above command line will be executed with the file name of the dropped file, like:

```
the-command-line a-dropped-file
```



