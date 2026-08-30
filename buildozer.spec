[app]

# (str) Title of your application
title = Zaki Mobile App

# (str) Package name
package.name = zakimobileapp

# (str) Package domain (needed for android packaging)
package.domain = org.zaki

# (str) Source files where the let of data is (relative to directory of spec)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minAPI = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Enable Android auto backup
android.autopm = True
