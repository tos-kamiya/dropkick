python3 -m venv venv
rsync -av /usr/lib/python3/dist-packages/PyQt5/ venv/lib/python3.6/site-packages/PyQt5/
cp /usr/lib/python3/dist-packages/sip.cpython-*.so venv/lib/python3.6/site-packages/
chmod +x AppRun

cd ..
env ARCH=x86_64 appimagetool dropkick/
