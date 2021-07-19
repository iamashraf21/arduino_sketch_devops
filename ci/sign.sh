#/bin/bash
pwd
ls ../build/
mkdir ../../build_signed
python ../../ci/sign.py ../../ci/private.pem firmware.ino.bin 1 --out ../../build_signed/firmware.signed 
python ../../ci/verify.py ../../ci/public.pem ../../build_signed/firmware.signed
