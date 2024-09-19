DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "awx",
        'USER': "awx",
        'PASSWORD': "awxpass",
        'HOST': "postgres",
        'PORT': "5432",
    }
}

BROADCAST_WEBSOCKET_SECRET = "eE5rTWJodEJJcDVRTzZVM2VXU1JERzJ1Mk4wdWVMVUVIa3pnQ2J1NUZxVmtvWVlkeTU5MFEtenQsVkJ1aU46T1MzLlNxbWVkbHI2NFRHX1lzajRZUXV4X0xZZWFPazdYZ3ZJeVFma0FnTHpsNVRMLnAwLDF4YnIxYWxWZjA3M1A="
