#Here you can see some regular expression samples to extract data from files using Python.

#1. Get a list of names from the sentences below.

import re
def names():   
    x = []
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""
    for name in re.findall("[A-Z]{1}\w*", simple_string):
        x.append(re.split("\s|,", name)[0])
    return x


#2. Get a list of the full names of the students who have received a 'B'.

import re
def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()
    return re.findall("[a-zA-Z ]{1,100}(?=:\sB)", grades)
	

#3. 
"""Parse the web log file, converting it into a list of dictionaries, where each dictionary looks like the following:
example_dict = {"host":"146.204.224.152", 
                "user_name":"feest6811", 
                "time":"21/Jun/2019:15:45:24 -0700",
                "request":"POST /incentivize HTTP/1.1"} """

import re
def logs():
    with open("assets/logdata.txt", "r") as file:
        logdata = file.read()
        x = []
        pattern="""        
        (?P<host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?=\s-\s))
        (.*)
        (?P<user_name>(?<=\s-\s).+(?=\s\[))
        (.*)
        (?P<time>(?<=\[).+(?=\]))
        (.*)
        (?P<request>(?<=").+(?="))
        (.*\n)
        """
        for item in re.finditer(pattern,logdata,re.VERBOSE):
            x.append(item.groupdict())
    return x

""" #2. grades = """'Ronald Mayr: A\nBell Kassulke: B\nJacqueline Rupp: A \nAlexander Zeller: C\nValentina Denk: C \nSimon Loidl: B \nElias Jovanovic: B \nStefanie Weninger: A \nFabian Peer: C \nHakim Botros: B\nEmilie Lorentsen: B\nHerman Karlsen: C\nNathalie Delacruz: C\nCasey Hartman: C\nLily Walker : A\nGerard Wang: C\nTony Mcdowell: C\nJake Wood: B\nFatemeh Akhtar: B\nKim Weston: B\nNicholas Beatty: A\nKirsten Williams: C\nVaishali Surana: C\nCoby Mccormack: C\nYasmin Dar: B\nRomy Donnelly: A\nViswamitra Upandhye: B\nKendrick Hilpert: A\nKillian Kaufman: B\nElwood Page: B\nMukti Patel: A\nEmily Lesch: C\nElodie Booker: B\nJedd Kim: A\nAnnabel Davies: A\nAdnan Chen: B\nJonathan Berg: C\nHank Spinka: B\nAgnes Schneider: C\nKimberly Green: A\nLola-Rose Coates: C\nRose Christiansen: C\nShirley Hintz: C\nHannah Bayer: B'
"""
#3. logdata="""'146.204.224.152 - feest6811 [21/Jun/2019:15:45:24 -0700] "POST /incentivize HTTP/1.1" 302 4622\n197.109.77.178 - kertzmann3129 [21/Jun/2019:15:45:25 -0700] "DELETE /virtual/solutions/target/web+services HTTP/2.0" 203 26554\n156.127.178.177 - okuneva5222 [21/Jun/2019:15:45:27 -0700] "DELETE /interactive/transparent/niches/revolutionize HTTP/1.1" 416 14701\n100.32.205.59 - ortiz8891 [21/Jun/2019:15:45:28 -0700] "PATCH /architectures HTTP/1.0" 204 6048\n168.95.156.240 - stark2413 [21/Jun/2019:15:45:31 -0700] "GET /engage HTTP/2.0" 201 9645\n71.172.239.195 - dooley1853 [21/Jun/2019:15:45:32 -0700] "PUT /cutting-edge HTTP/2.0" 406 24498\n180.95.121.94 - mohr6893 [21/Jun/2019:15:45:34 -0700] "PATCH /extensible/reinvent HTTP/1.1" 201 27330\n144.23.247.108 - auer7552 [21/Jun/2019:15:45:35 -0700] "POST /extensible/infrastructures/one-to-one/enterprise HTTP/1.1" 100 22921\n2.179.103.97 - lind8584 [21/Jun/2019:15:45:36 -0700] "POST /grow/front-end/e-commerce/robust HTTP/2.0" 304 14641\n241.114.184.133 - tromp8355 [21/Jun/2019:15:45:37 -0700] "GET /redefine/orchestrate HTTP/1.0" 204 29059\n224.188.38.4 - keebler1423 [21/Jun/2019:15:45:40 -0700] "PUT /orchestrate/out-of-the-box/unleash/syndicate HTTP/1.1" 404 28211\n94.11.36.112 - klein8508 [21/Jun/2019:15:45:41 -0700] "POST /enhance/solutions/bricks-and-clicks HTTP/1.1" 404 24768\n126.196.238.197 - gusikowski9864 [21/Jun/2019:15:45:45 -0700] "DELETE /rich/reinvent HTTP/2.0" 405 7894\n103.247.168.212 - medhurst2732 [21/Jun/2019:15:45:49 -0700] "HEAD /scale/global/leverage HTTP/1.0" 203 15844\n57.86.153.68 - dubuque8645 [21/Jun/2019:15:45:50 -0700] "POST /innovative/roi/robust/systems HTTP/1.1" 406 29046\n231.220.8.214 - luettgen1860 [21/Jun/2019:15:45:52 -0700] "HEAD /systems/sexy HTTP/1.1" 201 2578\n
"""

