import math

while True:
    
    valid = True
    print('Enter the IP address: ', end = '')
    ip = input().split('.')
    if len(ip) != 4:
        print('Invalid IP address')
        continue
    
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
        break

while True:
    print('Enter Subnet Mask in CIDR notation: ', end = '')
    mask = input()
    try :
        mask = int(mask)
        if int(mask) > 32:
            print('Subnet Mask is a number between 0 - 32')
        else: break
    except:
        print('Subnet Mask is a number between 0 - 32')


while True:

    try:
        print('Enter number of networks needed: ',end ='')
        number_networks = eval(input())
        break
    except:
        print('Invalid input. Input must be a number')

number_hosts = []

for i in range(number_networks):
    
    while True:
        print(f'Enter number of hosts for network {i+1}: ',end = '')
        try:
            host = eval(input())
            number_hosts.append(host)
            break
        except:
            print('Invalid input. Input must be a number')


number_hosts.sort()


total_number_host = 2 ** (32 - mask) 




for i in number_hosts[::-1]:
    total_number_host -= 2 ** math.ceil( math.log2(i + 2)) 


if total_number_host < 0 :
    print('Looks like those subnets will not fit into that network' )

else:

   
    ip_binary = "{0:08b}{1:08b}{2:08b}{3:08b}".format(*ip)
    mask_binary = '1' * mask + '0' *(32 - mask)

    network_binary = int(ip_binary,2) & int(mask_binary,2)
    network_binary = bin(network_binary)[2:]
    network = str(int(network_binary[:8],2))+'.'+str(int(network_binary[8:16],2))+'.'+str(int(network_binary[16:24],2))+'.'+str(int(network_binary[24:],2))
    
    print( f'Network {network} has {2 ** (32 - mask) -2} hosts'  )

    print('------------------------------------------------------')
    

    counter = 1
    for i in number_hosts[::-1]:
        print(f'subnet {counter}' )
        print(f'Network ID: {network}')
        number_hosts_available = 2 ** math.ceil(math.log2(i + 2) ) - 2 
        number_hosts_unused = number_hosts_available - i
        print(f'/{ 32 - math.ceil(math.log2(number_hosts_available))}') 
        print(f'Number of hosts available: {number_hosts_available}')
        print(f'Number of host needed: {i}, Number of hosts unused {number_hosts_unused}')
        network_binary = bin(int(network_binary,2) + 1)[2:]
        network = str(int(network_binary[:8],2))+'.'+str(int(network_binary[8:16],2))+'.'+str(int(network_binary[16:24],2))+'.'+str(int(network_binary[24:],2))
        print(f'Network range: {network} - ',end='')
        network_binary = network_binary = bin(int(network_binary,2) + number_hosts_available - 1 )[2:]
        network = str(int(network_binary[:8],2))+'.'+str(int(network_binary[8:16],2))+'.'+str(int(network_binary[16:24],2))+'.'+str(int(network_binary[24:],2))
        print(network)
        network_binary =  bin(int(network_binary,2) + 1)[2:]
        network = str(int(network_binary[:8],2))+'.'+str(int(network_binary[8:16],2))+'.'+str(int(network_binary[16:24],2))+'.'+str(int(network_binary[24:],2))
        print(f'Network broadcast: {network} ')
        network_binary =  bin(int(network_binary,2) + 1)[2:]
        network = str(int(network_binary[:8],2))+'.'+str(int(network_binary[8:16],2))+'.'+str(int(network_binary[16:24],2))+'.'+str(int(network_binary[24:],2))
        counter += 1
        print('------------------------------------------------------')