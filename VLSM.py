import math

# A loop that takes the IP address as input from the user and only broken if the IP is valid
while True:    
    valid = True
    print('Enter the IP address: ', end = '')
    
    #split the octets and store the values in an array
    ip = input().split('.')
    
    #check if the ip consists of 4 octets
    if len(ip) != 4:                             
        #if they are not 4 octets start from the begining
        print('Invalid IP address')
        continue
    
    #loop over each octet and check whether its numeric and the value is between 0 and 255
    #Start from the begining if the condition is not satisfied
    for i in range( len(ip) ):
        try:
            ip[i] = int(ip[i])
            if ip[i] > 255 or ip[i] < 0:
                valid = False
                break
        except:
            valid = False
            print('Invalid IP address')
            break
    
    if valid:
        #if the input is True break the while loop and start the next step
        break

# A loop that takes the Subnet Mask address as input from the user and only broken if the Mask is valid
while True:
    print('Enter Subnet Mask in CIDR notation: ', end = '')
    mask = input()
    try :
        # check whether the input is valid
        mask = int(mask)
        if int(mask) > 32 or int(mask) < 0 :
            print('Subnet Mask is a number between 0 - 32')
        else: break
    except:
        print('Subnet Mask is a number between 0 - 32')


# A loop that takes the number of networks as input and broken when the input is a number
while True:
    try:
        print('Enter number of networks needed: ',end ='')
        number_networks = int(input())
        break
    except:
        print('Invalid input. Input must be a number')

number_hosts = []

# a loop to take the number of hosts for each network
for i in range(number_networks):
    
    # a loop that check the input is always a number
    while True:
        print(f'Enter number of hosts for network {i+1}: ',end = '')
        try:
            host = int(input())
            number_hosts.append(host)
            break
        except:
            print('Invalid input. Input must be a number')

# Sort the number of hosts as we assign the network with the highes number of hosts first
number_hosts.sort()

# calculate the total number of available IP given the subnet mask
total_number_host = 2 ** (32 - mask) 



#Subtract the number of hosts of each network from the total number of available IP
for i in number_hosts[::-1]:
    total_number_host -= 2 ** math.ceil( math.log2(i + 2)) 

#check whether the number of hosts need to assigned can fit into the network
if total_number_host < 0 :
    print('Looks like those subnets will not fit into that network' )

else:
    
    #calculate the network IP in binary
    ip_binary = "{0:08b}{1:08b}{2:08b}{3:08b}".format(*ip)
    #calculate the subnet mask in binary
    mask_binary = '1' * mask + '0' *(32 - mask)
    
    # Anding the network IP and the subnet mask to get the network ID  
    network_binary = int(ip_binary,2) & int(mask_binary,2)
    network_binary = bin(network_binary)[2:]
    
    #convert the network ID from binary to decimal
    network = str(int(network_binary[:8],2))+'.'+str(int(network_binary[8:16],2))+'.'+str(int(network_binary[16:24],2))+'.'+str(int(network_binary[24:],2))
    
    #print newtork ID and number of available hosts for the subnet mask
    print( f'Network {network} has {2 ** (32 - mask) -2} hosts'  )

    print('------------------------------------------------------')
    

    counter = 1
    
    #Loop over each network to assign hosts from the network of the large number of hosts to the smaller one
    for i in number_hosts[::-1]:
        
        print(f'subnet {counter}' )
        print(f'Network ID: {network}')
        
        #calculate the available number of hosts for the subnet 
        number_hosts_available = 2 ** math.ceil(math.log2(i + 2) ) - 2 
        #calculate the number of unused IP
        number_hosts_unused = number_hosts_available - i
        
        #print the subnet mask of the network
        print(f'/{ 32 - math.ceil(math.log2(number_hosts_available))}') 
        
        #print the total avaialable IP, number of hosts needed, and number of hosts unused
        print(f'Number of hosts available: {number_hosts_available}')
        print(f'Number of host needed: {i}, Number of hosts unused {number_hosts_unused}')
        
        #Calculate the first usable IP in the network in binary then convert it to decimal
        network_binary = bin(int(network_binary,2) + 1)[2:]
        network = str(int(network_binary[:8],2))+'.'+str(int(network_binary[8:16],2))+'.'+str(int(network_binary[16:24],2))+'.'+str(int(network_binary[24:],2))
        print(f'Network range: {network} - ',end='')

        #calculate the last usable IP in the network in binary then convert it to decimal
        #Print the available range of IPs      
        network_binary = network_binary = bin(int(network_binary,2) + number_hosts_available - 1 )[2:]
        network = str(int(network_binary[:8],2))+'.'+str(int(network_binary[8:16],2))+'.'+str(int(network_binary[16:24],2))+'.'+str(int(network_binary[24:],2))
        print(network)

        #print the broadcast IP of the network in binary then convert it to Decimal
        network_binary =  bin(int(network_binary,2) + 1)[2:]
        network = str(int(network_binary[:8],2))+'.'+str(int(network_binary[8:16],2))+'.'+str(int(network_binary[16:24],2))+'.'+str(int(network_binary[24:],2))
        print(f'Network broadcast: {network} ')
        
        #calculate the network ID of the next subnet
        network_binary =  bin(int(network_binary,2) + 1)[2:]
        network = str(int(network_binary[:8],2))+'.'+str(int(network_binary[8:16],2))+'.'+str(int(network_binary[16:24],2))+'.'+str(int(network_binary[24:],2))
        counter += 1
        print('------------------------------------------------------')