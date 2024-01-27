#!/bin/bash

while true; do
    python3 /home/katana/Desktop/blockpost.py

    if [ $? -ne 0 ]; then
        echo "РЎРєСЂРёРїС‚ Р·Р°РІРµСЂС€РёР»СЃСЏ СЃ РѕС€РёР±РєРѕР№. РџРµСЂРµР·Р°РїСѓСЃРє С‡РµСЂРµР· 5 СЃРµРєСѓРЅРґ..."
        sleep 5
    else
        break
    fi
done
