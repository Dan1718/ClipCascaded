from core.constants import *
from core.config import Config

if PLATFORM == WINDOWS:
    # WINDOWS: When creating the executable with pyinstaller, add --hidden-import plyer.platforms.win.notification
    from plyer import notification
elif PLATFORM.startswith(LINUX):
    from cli.info import CustomDialog
elif PLATFORM == MACOS:
    import subprocess


class NotificationManager:
    def __init__(self, config: Config):
        self.config = config

    def notify(self, title: str, message: str, app_name: str = APP_NAME, timeout=10):
        if self.config.data["notification"]:  # Check if notifications are enabled
            try:
                if PLATFORM == WINDOWS:
                    notification.notify(
                        title=title,
                        message=message,
                        app_name=app_name,
                        timeout=timeout,  # seconds
                    )
                elif PLATFORM.startswith(LINUX):
                    CustomDialog(f"{title} : {message}").mainloop()
                elif PLATFORM == MACOS:
                    subprocess.run(
                        [
                            "osascript",
                            "-e",
                            f'display notification "{message}" with title "{title}"',
                        ]
                    )
            except Exception as e:
                logging.error(f"Failed to handle notification: {e}")
