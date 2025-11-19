# List of approved dog breeds
APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        # These will trigger the setter methods below
        self.name = name
        self.breed = breed

    # ------------------ NAME PROPERTY ------------------

    @property
    def name(self):
        """
        Getter method for name.
        Called when you access dog.name
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Setter for name.
        Validates that the name is a string between 1–25 characters.
        """
        if isinstance(value, str) and 1 <= len(value) <= 25:
            # Store the validated name in a "protected" variable _name
            self._name = value.title()
        else:
            raise ValueError("Name must be string between 1 and 25 characters.")

    # ------------------ BREED PROPERTY ------------------

    @property
    def breed(self):
        """
        Getter for breed.
        Called when you access dog.breed
        """
        return self._breed

    @breed.setter
    def breed(self, value):
        """
        Setter for breed.
        Ensures the breed is in the APPROVED_BREEDS list.
        """
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            raise ValueError("Breed must be in list of approved breeds.")
