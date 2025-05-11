import datetime

class Logger:
    """
    Simple logger with colored output for different log levels.
    """
    
    # ANSI color codes
    COLORS = {
        "RESET": "\033[0m",
        "RED": "\033[91m",
        "GREEN": "\033[92m",
        "YELLOW": "\033[93m",
        "BLUE": "\033[94m",
        "MAGENTA": "\033[95m",
        "CYAN": "\033[96m",
    }
    
    def _log(self, level, message, color):
        """
        Base log method.
        
        Args:
            level (str): Log level.
            message (str): Message to log.
            color (str): ANSI color code.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{color}[{timestamp}] [{level}] {message}{self.COLORS['RESET']}")
        
    def info(self, message):
        """
        Log an informational message.
        
        Args:
            message (str): Message to log.
        """
        self._log("INFO", message, self.COLORS["BLUE"])
        
    def success(self, message):
        """
        Log a success message.
        
        Args:
            message (str): Message to log.
        """
        self._log("SUCCESS", message, self.COLORS["GREEN"])
        
    def warning(self, message):
        """
        Log a warning message.
        
        Args:
            message (str): Message to log.
        """
        self._log("WARNING", message, self.COLORS["YELLOW"])
        
    def error(self, message):
        """
        Log an error message.
        
        Args:
            message (str): Message to log.
        """
        self._log("ERROR", message, self.COLORS["RED"])
