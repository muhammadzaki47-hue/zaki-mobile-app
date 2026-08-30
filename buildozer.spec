[app]

# (str) Title of your application
title = Zaki Mobile App

# (str) Package name
package.name = zakimobileapp

# (str) Package domain (needed for android packaging)
package.domain = org.zaki

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source directory where the application files are located
source.dir = .

# (str) Application versioning
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) List of permissions
#android.permissions = INTERNET

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (list) Supported architectures
android.archs = arm64-v8a, armeabi-v7a

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minAPI = 21

# (bool) Use the Android X support library
android.androidx = True
