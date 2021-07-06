#/bin/bash
pwd
cd build/Seeeduino.samd.zero/
mkdir ../../build_signed
python ../../ci/sign.py ../../ci/private.pem firmware.ino.bin 1 --out ../../build_signed/firmware.signed 
python ../../ci/verify.py ../../ci/public.pem ../../build_signed/firmware.signed
