# import datetime
# import subprocess
#
#
# def collect_log():
#     now_time = datetime.datetime.now()
#     date_now = datetime.datetime.date(now_time)
#     date_before = date_now + datetime.timedelta(days=-1)
#     file_name = f"uwsgi-{date_before.year}-{date_before.month}-{date_before.day}.log"
#     log_path = "/home/ubuntu/src/logs/" + file_name
#     logdir_path = "/home/ubuntu/src/logs/logdir"
#     subprocess.run(["mv", log_path, logdir_path])
#     subprocess.run(["uwsgi", "--stop", "/tmp/uwsgi.pid"])
#     subprocess.run(["uwsgi", "uwsgi.ini", "--daemonize", "uwsgi.log", "--pidfile", "/tmp/uwsgi.pid"])
#
#
#
# if __name__ == '__main__':
#     collect_log()
