"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self,
                 fname,
                 lname,
                 email,
                 password):
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about Customer in console."""

        return "<Customer: {}, {}, {}>".format(self.first_name, 
                                               self.last_name, 
                                               self.email)


def read_melon_types_from_file(filepath):
    """Read customer data and populate.
    Dictionary will be {email: Customer object}
    """
    customers = {}

    with open(filepath) as file:
        for line in file:
            (fname,
             lname,
             email,
             password) = line.strip().split("|")

            customers[email] = Customer(fname,
                                        lname,
                                        email,
                                        password)

    return customers


def get_all():
    """Return list of customers."""
    # This relies on access to the global dictionary

    return list(customers.values())


def get_by_email(email):
    """Return a customer, given a email."""
    # This relies on access to the global dictionary `melon_types`

    return customers[email]


# Dictionary to hold types of melons.
#
# Format is {id: Melon object, ... }

customers = read_melon_types_from_file("customers.txt")