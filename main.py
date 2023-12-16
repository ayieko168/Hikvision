from hikvisionapi import Client

cam = Client('http://192.168.1.52', 'admin', 'globe')

response = cam.System.deviceInfo(method='get')

print(response)