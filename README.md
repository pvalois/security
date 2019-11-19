# security

Since i started root-me, i decided to write some helpers to audit servers.
Not much of a work, of course, but useful nonetheless, and publishing them here makes no harm. 

   - Web

     * urlextact.py          : extract link of interest from an url, in order to build web site analyser/mirrorer/hacker scripts
     * htmlentities.py       : a simple html entities decoder, for rewriting purposes in shell script
     * httpprobe.py          : probe for 80,443,8080  and 8443 port on target ip/name and fetch the title if possible
     * getcookies.py         : like html entities, a one simple purpose script, connect to a page, and print retrieved cookies, useful for session continuity when hacking
     * test-methods.py       : a script to test methods supported by a web server
     * xssfilter.py          : rudimentary xss injector sending the content of vector_XSS.txt file to the "message" field of the url
     * ha-brute-detector.py  : script who parse /var/log/haproxy.log and count 404 errors to identify possible dirbuster
     * forgotten-treasure.py : dirbustting over links in a web page to find .old .bak .back and ~ backup versions as a possible security faw

   - Wifi

     * get-ssid.py : extract the sid from a capture of a wifi session 

   - Reverse Engineering
	
     * r2graphasm.py : script using radare2 to generate a flowchart of disassembled binary

   - Pentesting

     * Metasploit : scripts using pymetasploit3 to remotely control metasploit with python 

