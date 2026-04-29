#!/usr/bin/env python3


    # now to we are going to creat a !--port scanner using python V- 27.4.25.1--!
    # now to we are going to creat a !--port scanner using python V- 28.4.25.2--!
    # now to we are going to creat a !--port scanner using python V- 29.4.25.3--!


    # what it does ? 

    #--it ask for the Target and aske for the ports need to scan 
    #-- we can scan a range of port also
    #--and scan the port using socket tools in python 

#importing socket 
import socket
# to ensure the input correct we are importing regular exprission
#import re
#in here we are mentioning what is the communication tool
#in socket we created a class call socket from the class we createded 
#AF_INET ---> it say we are searcing IPv4 
#AF_INET6 ---> it saya we are also searching IPv6 // we can add both in one eg;-cant answer 2 call in one phone
#&& .SOCK.Stream ---> connecting through TCP trnsfer protoclo

#defing a pacakge -->the below code consider a the name called --portkey--
def portkey():
     
     def banner_grab (target,port): #this banner have Time out error 
                     s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
                     s.settimeout(2)    

                     s.connect((target,port)) #connecting banner 
                     try:  
                            s.send(b"HEAD / HTTP/1.1\r\nHost: target\r\n\r\n") #conforming or waking server 
                            banner = s.recv(1024)  #only this it showing time out 

                            if banner:
                                print(f"[Banner]{banner.decode(errors='ignore').strip()}")

                            else:
                                print('Banner can not find')
                 
                     except Exception as e:
                            print(f"[Banner]error{e}")
                     s.close()

    
     target=input('IP means enter -i or Web name meant enter -w :- ').strip().lower()
     if target =='-w':
        print('--web mode activiated--')
        domaine= input('enter scanning WEB,(eg:-google.com):-').strip()
        if '.' not in domaine :
           domaine += '.com'
        try:
         target=socket.gethostbyname(domaine)
         print(f'[resolved IP]->{target}')
        except socket.gaierror:
         print('--Invadlide Web name--')
         return 
     elif target == "-i":
       print('--IP mode activated--')
       target =input("Enter your target ? ")
     try:
        socket.inet_aton(target)
     except socket.error:
        print("--invalid IP--")
        return

    #ensuring the user entering correct parrten format if it wrong output will be --plese enter valid IP--
     #pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
      #      if not re.match(pattern,target):
       #         print ('-- plese enter valid IP--')
        #        return () '''
    
        #createin a mode this make this system bit advance it can now scan ranges from above 1 to below 65535 
        #if it contidiont not occur mean it print --invalid port--#
        #in here we can select 2 mode 1,(-s) sigle mode here can scan only one port
        #                             2,(-r) range mode you can scan arange from this
     try:
        mode = input('choose mode -s or -r :-').strip().lower()
        
        #single mode (-s)
        
        if mode == '-s':
            print('--single mode activated--')
            port =int(input("enter your scanning port ?"))
            if port < 1 or port > 65535:
                print ('--invalid port--')
                return
            else:
                print('--you need to scan :- ' +target+ ' and ,this port :- ' + str(port))

                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
                s.settimeout(5)

                result = s.connect_ex((target,port))
              
                if result == 0:
                    print(" [+] port is open")
                   
                    banner_grab(target,port)
                
                else:
                    print('[-] port is closed')
            s.close()

           #Range mode (-r)
            
        elif mode == '-r':
            print ('--range mode activated--')

            start=int(input('enter your starting range:- '))
            end=int(input('enter your ending range:-'))
            if start < 1 or end > 65535 or start > end :
                print("--invalid range--")
                return()
            for port in range(start, end + 1): 
                 
                 s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
                 s.settimeout(0.1)

                 result = s.connect_ex((target,port))
                 if result == 0 :
                    print (f'[+]--port {port} is open')

                    banner_grab(target,port)#reusing the definition 
                 else:
                    print(f'[-]--port {port} is closed') 
                 s.close()
        else:
                print('--invalid mode')
    #in here we used a error handaling is any value error happen or socket error happen it show the error massage not crash
     except ValueError:
      print (' --plese enter valid integers--')
     except socket.error as e:
      print(f'!!!socket error !!!{e}')
     finally:
       try:
        s.close()
       except:
          pass
if __name__ == "__main__" :
 portkey()
 
   


