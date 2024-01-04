import hashlib

"""
    Genrate a user id from ip adress.

    Parameters:
    ip (str): The IP address of the user.

    Returns:
    int: The user id.
    """


def user_id_from_ip(ip):
    # Use a cryptographic hash function (SHA-256 in this example)
    hash_object = hashlib.sha256(ip.encode()).hexdigest()[:5]
    # Convert the hash to a hexadecimal string and take the first 5 characters
    user_id_str = int(hash_object, 16)
    return user_id_str
