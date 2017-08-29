# import records
# import datetime
from flask import Flask
from flask import render_template
from flask import request
import os
import records
import datetime
import pymysql
import resource
import threading
import subprocess
import time
import sys

#db = records.Database('mysql://student:6s08student@localhost/iesc')

"""
user = "root"
key = ""
host = "localhost"
db_name = "karkhanaiot"

db = pymysql.connect(host, user, key, db_name)
cursor = db.cursor();

data = cursor.execute("SELECT * FROM iot")
print(data)
"""



# _resource_mapper = {
#     'CPUTIME': (resource.RLIMIT_CPU, lambda x: (x, x + 1)),
#     'MEMORY': (resource.RLIMIT_AS, lambda x: (x, x)),
#     'FILESIZE': (resource.RLIMIT_FSIZE, lambda x: (x, x)),
# }

# os.environ['MKL_NUM_THREADS']='1'
# os.environ['NUMEXPR_NUM_THREADS']='1'
# os.environ['OMP_NUM_THREADS']='1'


# kill_time = 4.0

# class PKiller(threading.Thread):
#     def __init__(self, proc, timeout):
#         threading.Thread.__init__(self)
#         self.proc = proc
#         self.timeout = timeout

#     def run(self):
#         end = time.time() + self.timeout
#         while (time.time() < end):
#             print(time.time(), self.proc.poll())
#             time.sleep(0.1)
#             if self.proc.poll() is not None:
#                 return
#         print(self.proc.poll())
#         if self.proc.poll() is None:
#             os.kill(self.proc.pid,signal.SIGKILL)
#             #os.killpg(os.getpgid(self.proc.pid), signal.SIGKILL)


# #os.killpg(os.getpgid(self.proc.pid), signal.SIGKILL)
# def run_code(code):
#     rlimits = [(resource.RLIMIT_NPROC, (0, 0)),(resource.RLIMIT_CPU,(kill_time,kill_time)), (resource.RLIMIT_AS,(500e6,500e6)),(resource.RLIMIT_FSIZE,(1e9,1e9))]
#     def limiter():
#         os.setsid()
#         for i in rlimits:
#             resource.setrlimit(*i)

#     interp = '/usr/bin/python3'

#     p = subprocess.Popen([interp, code],
#                          preexec_fn=limiter,
#                          stdin=subprocess.PIPE,
#                          stdout=subprocess.PIPE,
#                          stderr=subprocess.PIPE)
#     killer = PKiller(p, kill_time)
#     killer.start()

#     out, err = p.communicate(sys.stdin.read().encode())
#     if p.returncode is not None and p.returncode != 0:
#         final_string = "<h1>ERROR in your CODE :( !</h1>"
#         final_string+="<pre>"
#         final_string += err.decode()
#         final_string += out.decode()
#         final_string += "</pre>"
#     else:
#         final_string = out.rstrip().decode()
#     os.remove(code)
#     return final_string




def web_handler(request):
    method = request["REQUEST_METHOD"]

    if method == "GET":
        print("Using GET METHOD")
        return "GOT GET"
    else:
        print("Using something else")
        return "Something else"


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    print(request)
    params = request.args.to_dict()
    params["REQUEST_METHOD"] = request.method
    print(params.keys())

    web_handler(request)

    return render_template('index.html')


# @app.route('/uploads', methods=["GET", "POST"])
# def runcode():
#     #try:
#     if request.method == "GET":
#         data = """
#             x = 10
#             y = 20
#             z = 30
#             def data(request):
#                 return request
#         """
#         output = run_code(data)
#         return output
#     #except:
#         #return("Error! Sorry!")

port = int(os.environ.get('PORT', 8081))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, threaded=True)
