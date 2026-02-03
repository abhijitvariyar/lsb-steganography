class Log:

    # Define ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    WARNING = '\033[93m'
    ENDC = '\033[0m' # Reset to default color and style

    @staticmethod
    def log_success(msg):
        print(f"\n{Log.GREEN}{msg}{Log.ENDC}\n")

    @staticmethod
    def log_info(msg):
        print(f"[INFO] {msg}")

    @staticmethod
    def log_warning(msg):
        print(f"\n{Log.WARNING}!!!! WARNING !!!! : {msg}{Log.ENDC}\n")

    @staticmethod
    def log_error(msg):
        print(f"\n{Log.RED} !!!! FATAL ERROR !!!! : {msg}{Log.ENDC}\n")

# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
