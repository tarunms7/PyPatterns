# Target Interface (What the Client expects)
class EuropeanSocketInterface:
    def voltage(self):
        pass

    def plug_type(self):
        pass

    def is_compatible(self):
        pass


# Adaptee (Incompatible interface, for example, an American socket)
class AmericanSocket:
    def voltage(self):
        return 120

    def plug_type(self):
        return "Type A"

    def is_compatible(self):
        return False


# Adapter (Makes the AmericanSocket compatible with the EuropeanSocketInterface)
class SocketAdapter(EuropeanSocketInterface):
    def __init__(self, american_socket):
        self.american_socket = american_socket

    def voltage(self):
        # Adapting voltage from 120V (American) to 230V (European)
        return 230

    def plug_type(self):
        # Adapting plug type from "Type A" (American) to "Type C" (European)
        return "Type C"

    def is_compatible(self):
        return True  # Now it's compatible!


# Client code
class PhoneCharger:
    def __init__(self, socket: EuropeanSocketInterface):
        self.socket = socket

    def charge(self):
        if self.socket.is_compatible():
            print(f"Charging with {self.socket.voltage()}V using {self.socket.plug_type()} plug.")
        else:
            print("Incompatible socket, cannot charge.")


# Client interaction
if __name__ == "__main__":
    american_socket = AmericanSocket()  # Incompatible socket
    adapter = SocketAdapter(american_socket)  # Adapt it!

    charger = PhoneCharger(adapter)
    charger.charge()


# OUTPUT : Charging with 230V using Type C plug.
