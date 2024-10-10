# Notification Interface
class Notification:
    def send(self, message):
        pass

# Concrete Classes
class EmailNotification(Notification):
    def send(self, message):
        return f"Sending Email with message: {message}"

class SMSNotification(Notification):
    def send(self, message):
        return f"Sending SMS with message: {message}"

class PushNotification(Notification):
    def send(self, message):
        return f"Sending Push Notification with message: {message}"

# Notification Factory
class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")

# Example usage
if __name__ == "__main__":
    notification_type = input("Enter notification type (email, sms, push): ").lower()
    notification = NotificationFactory.create_notification(notification_type)
    print(notification.send("This is a test message"))
