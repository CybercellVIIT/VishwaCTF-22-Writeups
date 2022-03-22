1. The name of the challenge is a hint intself saying CVE(common vulnerabilities and exposures). 
Also the flag format given (EDBID_Date) is saying that we have to find the ExploitDB id of some attack.

2. Seeing the question again now also tells us that "JAILBREAK" is an important keyword.
Reasearching on internet tells us that it is a type of malware to gain access to mobile devices.

3. Carefully searching for "Ahmed Masoor's" on internet with "Jailbrake" we understand that this is a true story which lead to the discovery of "Pegasus" spyware.

4. Now we understand that we have to find the EDBID and date of the vulnerabilities that were used by the Pegasus spyware.
In ExploitDB we can find vulnerabilities to use in softwares like metasploit. To search ExploitDB we have to know what vulnerabilities pegasus used.

5. We search internet for the details of pegasus and find Vulnerabilities used were:
CVE-2016-4655: Information leak in kernel – A kernel base mapping vulnerability that leaks information to the attacker allowing them to calculate the kernel's location in memory.
CVE-2016-4656: Kernel memory corruption leads to jailbreak – 32 and 64 bit iOS kernel-level vulnerabilities that allow the attacker to secretly jailbreak the device and install surveillance software – details in reference.[66]
CVE-2016-4657: Memory corruption in the webkit – A vulnerability in the Safari WebKit that allows the attacker to compromise the device when the user clicks on a link.

6. We find one entry in ExploitDB for the search "2016-4655"/"2016-4656"/"2016-4657" and on clicking we find 
EDB-ID : 44836
Date : 2018-06-05
