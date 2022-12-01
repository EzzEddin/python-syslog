import syslog

syslog.syslog('Sending a log message through syslog_module_v1!')
def divide(dividend, divisor):
    try:
        syslog.syslog(syslog.LOG_INFO, f"Dividing {dividend} by {divisor}")
        return dividend / divisor
    except ZeroDivisionError:
        syslog.syslog(syslog.LOG_ERR, "Zero Division error.")

print(divide(6, 2))
print(divide(6, 0))
