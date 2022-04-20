To investigate version differences between dashjs v4.3.0, v4.2.1 and v3.1.3.

Quickstart

1. Run logging server:
    - `python http_log_server.py <run_key>` (server runs at port 3003)
    - <run_key> eg. `dashjs4.1.2_some_comment`, to be appended to results folder name
    - IMPT: Re-run command for each new test run to create separate log files

1. Run HTTP server w dash.js media files:
    - `cd server`
    - `vi config/nginx.conf` and update this line `root /<PATH_TO_MAIN_FOLDER>/server/nginx;` with the correct system directory (use absolute path)
    - Start nginx: `sudo nginx -c /<PATH_TO_MAIN_FOLDER>/server/nginx/config/nginx.conf`

1. Run dash.js of desired version:
    - v4.3.0
        - `cd dash.js-4.3.0`
        - `npm install` (if not done before)
        - `npm run start`
    - v4.2.1
        - `cd dash.js-4.2.1`
        - `npm install` (if not done before)
        - `npm run start`
    - v3.1.3
        - `cd dash.js-3.1.3`
        - `npm install` (if not done before)
        - `grunt dev`
    - IMPT: All dash.js above have been edited with:
        - Additional logging/debugging commands 
        - ABR rule: abrThroughput
        - Min/Max buffer: 4s/20s

1. Run tc throttling:
    - `sudo bash tc-network-profiles/2c_Cascade.sh` (2c refers to 2 client test case)
    - To kill the throttling, Ctrl-C and run `sudo bash tc-network-profiles/kill.sh`

1. Run the test:
    - Open n (eg. n=2 for `2c_Cascade.sh`) instances of desired browser (eg. Chrome/Firefox)
    - Navigate to: `http://localhost:3000/samples/cmsd-dash/index.html` on each browser
    - Wait for the video to complete (video/test duration: approx. 10mins)
    - Stop the logging server
    - Review the results in `results` folder
