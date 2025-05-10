[app]
title = Ultra Local Comic Reader
package.name = ultralocalcomic
package.domain = org.kivy
version = 1.0.0

source.dir = .
source.main = main.py

requirements = 
    python3==3.10.5,
    kivy==2.3.0,
    pillow==10.1.0,
    pyjnius==1.5.0,
    android

android.api = 34
android.minapi = 21
android.ndk_version = 25b
android.archs = arm64-v8a

# 更新后的权限配置（Android 11+兼容）
android.permissions = 
    INTERNET,
    READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2