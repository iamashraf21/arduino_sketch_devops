#/bin/bash
pwd
cd firmware/build/Moteino.samd.moteino_m0
ls -l
mkdir ../../build_signed
python ../../../ci/sign.py ../../../ci/private.pem firmware.ino.bin 1 --out ../../build_signed/firmware.signed 
python ../../../ci/verify.py ../../../ci/public.pem ../../build_signed/firmware.signed
