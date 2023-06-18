class Secret:
    def __init__(self, data, secret_data):
        self.data=data
        # Prefixing with two underscores to make it private
        self._secret_data = secret_data


# Creating an object
my_secret = Secret("Public Data","Private Data")

print(my_secret.data)

# Trying to access the private variable directly
# This will cause AttributeError because the variable is intended to be private.

print(my_secret._secret_data)
