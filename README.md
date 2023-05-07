# IP Subnet Calculator


This script is a simple IP subnet calculator that takes an IP address, subnet mask in CIDR notation, and the number of networks and number of hosts per network as input, and calculates the network ID and the number of available hosts for each network.

The script starts by taking the IP address as input from the user and validating whether the input is valid or not. Next, the subnet mask is taken as input and validated. Finally, the number of networks and hosts per network are taken as input, and the script calculates the available hosts for each network.


How to Use

- Enter the IP address when prompted.
- Enter the subnet mask in CIDR notation when prompted.
- Enter the number of networks needed when prompted.
- Enter the number of hosts for each network when prompted.

## Output
The script will output the network ID and the number of available hosts for each network. If the number of hosts needed for each network cannot be assigned to the given subnet, the script will print a message indicating that the subnets will not fit into the network.