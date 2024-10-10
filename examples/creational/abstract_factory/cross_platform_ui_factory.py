from abc import ABC, abstractmethod

# Abstract Product: Button
class Button(ABC):
    @abstractmethod
    def click(self):
        pass

# Abstract Product: Checkbox
class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass

# Concrete Product: Windows Button
class WindowsButton(Button):
    def click(self):
        return "Windows Button clicked"

# Concrete Product: Windows Checkbox
class WindowsCheckbox(Checkbox):
    def check(self):
        return "Windows Checkbox checked"

# Concrete Product: MacOS Button
class MacOSButton(Button):
    def click(self):
        return "MacOS Button clicked"

# Concrete Product: MacOS Checkbox
class MacOSCheckbox(Checkbox):
    def check(self):
        return "MacOS Checkbox checked"

# Abstract Factory: UIFactory
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factory: Windows UI Factory
class WindowsUIFactory(UIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

# Concrete Factory: MacOS UI Factory
class MacOSUIFactory(UIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()

# Example usage
def client_code(factory: UIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(button.click())
    print(checkbox.check())

if __name__ == "__main__":
    print("Windows UI:")
    windows_factory = WindowsUIFactory()
    client_code(windows_factory)

    print("\nMacOS UI:")
    macos_factory = MacOSUIFactory()
    client_code(macos_factory)



"""
OUTPUT 

Windows UI:
Windows Button clicked
Windows Checkbox checked

MacOS UI:
MacOS Button clicked
MacOS Checkbox checked
"""