import datetime

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    def log(self, message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f'[{timestamp}] {message}\n'
        
        with open(self.log_file, 'a') as file:
            file.write(log_message)
        
        print(log_message.strip())

# Example usage
logger = Logger('system_log.txt')
logger.log('System started')
logger.log('File processed successfully')
logger.log('Error occurred')