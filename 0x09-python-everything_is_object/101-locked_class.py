#: /usr/bin/python3
"""Defines a Locked class """
class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes for
    anything but attributes called 'first name'
    """
    _slots_ = ["first_name" ]
