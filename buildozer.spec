[app]
title = MC Bedrock Resizer
package.name = mcbedrockresizer
package.domain = com.mcbedrock
version = 1.0.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
source.dir = .
android.accept_sdk_license = True


[buildozer]
log_level = 2
warn_on_root = 1

[app@android]
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 23b
android.arch = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
