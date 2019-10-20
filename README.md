# security

Since i started root-me, i decided to write some helpers to audit servers.
Not much of a work, of course, but useful nonetheless, and publishing them here makes no harm. 

   - Web

     * urlextact.py      : extract link of interest from an url, in order to build web site analyser/mirrorer/hacker scripts
     * htmlentities.py   : a simple html entities decoder, for rewriting purposes in shell script
     * httproxy.py       : probe for 80,443,8080  and 8443 port on target ip/name and fetch the title if possible
     * getcookies.py     : like html entities, a one simple purpose script, connect to a page, and print retrieved cookies, useful for session continuity when hacking
     * test-methods.py   : a script to test methods supported by a web server
     * xssfilter.py      : rudimentary xss injector sending the content of vector_XSS.txt file to the "message" field of the url
     * ha-brute-detector : script who parse /var/log/haproxy.log and count 404 errors to identify possible dirbuster

   - Wifi

     * get-ssid.py : extract the sid from a capture of a wifi session 

