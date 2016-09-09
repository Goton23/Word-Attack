try:
    #Wordlist Generator
    # -*- coding: utf-8 -*-
    import itertools
    import os
    import time
    import sys


    liste = []
    infile = "/root/A1"
    wordlist = []
    zeit = 1
    nummern = 0
    counter = 0
    zahlen = 0


    print"""
       _  _   _    _ _________________    ___ _____ _____ ___  _____ _   __  _  _
     _| || |_| |  | |  _  | ___ |  _  \  / _ |_   _|_   _/ _ \/  __ | | / /_| || |_
    |_  __  _| |  | | | | | |_/ | | | | / /_\ \| |   | |/ /_\ | /  \| |/ /|_  __  _|
     _| || |_| |/\| | | | |    /| | | | |  _  || |   | ||  _  | |   |    \ _| || |_
    |_  __  _\  /\  \ \_/ | |\ \| |/ /  | | | || |   | || | | | \__/| |\  |_  __  _|
      |_||_|  \/  \/ \___/\_| \_|___/   \_| |_/\_/   \_/\_| |_/\____\_| \_/ |_||_|


    """

    while True:
        buchstaben = raw_input("Characters which will be in list [stop] to exit: ")
        if buchstaben == "stop":
            break
        zahlen = zahlen + 1
        liste.append(buchstaben)

    pfad = raw_input("Name of Wordlist: ")

    print("[*] Word Attack will now Generate the Wordlist You have 3 Seconds to abort!!!")
    time.sleep(3)



    for L in range(0, len(liste)+1):
            for subset in itertools.permutations(liste, L):
                    wordlist.append(subset)
                    counter = counter + 1
                    if counter == 1:
                        nummern = nummern + 1
                        print("[*] Generated %s Words" %(nummern))
                        counter = 0


    print("[*] Preparing Wordlist this could take a while")


    f = open("/root/A1", "w")
    f.write("\n".join(map(lambda x: str(x), wordlist)))
    f.close()



    outfile = pfad
    delete_list = ["(", ")", "'", ",", " "]
    fin = open(infile)
    fout = open(outfile, "w+")
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)
    fin.close()
    fout.close()


    lenge = len(wordlist)
    print("\n\n[*] Succesfully written %s numbers to %s" %(lenge, pfad))
    time.sleep(2)

    os.remove("/root/A1")

except KeyboardInterrupt:
    print("[*] Exiting...")
    sys.exit()