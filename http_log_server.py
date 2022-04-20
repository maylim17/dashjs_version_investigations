from http.server import BaseHTTPRequestHandler, HTTPServer
from time import time
import os
import sys

hostName = "localhost"
serverPort = 3003

run_timestamp = str(int(time()))
# run_comment = "_dashjs4.1.2_testbed_chrome_v313_4s20s"
run_comment = ""
if sys.argv[1]:
    run_comment = "_" + sys.argv[1]

results_folder = "results/" + run_timestamp + run_comment
os.mkdir(results_folder)
csv_filepath_tputpushed = results_folder + "/tputpushed.csv"
csv_filepath_allmetrics = results_folder + "/allmetrics.csv"   # Extracts all params provided by client in req url

with open(csv_filepath_tputpushed,"a") as csv_f:
    csv_f.write('timestamp, tc_value, dash_value, dash_client_id\n')  ## headers

last_tc_value = 0

class LogServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("", "utf-8"))

        # print(self.path)

        global last_tc_value
        timestamp = str(int(time()))

        if "tc_value" in self.path:
            last_tc_value = self.path.split("/")[-1]

        elif "dash_value" in self.path:
            dash_client_id = self.path.split("/")[-2]
            dash_value = self.path.split("/")[-1]

            with open(csv_filepath_tputpushed,"a") as csv_f:
                csv_f.write(timestamp + ", " + last_tc_value + ", " + dash_value + ", " + dash_client_id + "\n")

        elif "dash_metrics" in self.path:
            headers_str = "timestamp, last_tc_value, "
            values_str = timestamp + ", " + last_tc_value + ", "

            query_str = self.path.split("?")[-1]
            params_arr = query_str.split(",")
            for kv_pair_str in params_arr:
                kv_pair = kv_pair_str.split("=")
                headers_str += (kv_pair[0] + ", ")
                values_str += (kv_pair[1] + ", ")

            headers_str += "\n"
            values_str += "\n"

            if not os.path.isfile(csv_filepath_allmetrics):    ## file not created yet
                with open(csv_filepath_allmetrics,"a") as csv_f:
                    csv_f.write(headers_str)        ## add headers

            with open(csv_filepath_allmetrics,"a") as csv_f:
                csv_f.write(values_str)
            


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), LogServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")