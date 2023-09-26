import ctypes

# Load the shared library
hello_lib = ctypes.CDLL('./build/hello.dylib')  # Use the appropriate extension for your OS (.so for Linux, .dll for Windows)

# Call the function from the shared library
hello_lib.say_hello()
