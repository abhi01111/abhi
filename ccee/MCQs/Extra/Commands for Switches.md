### **Configuration for VLAN1 (Step-wise)**
- **`switch> on`**: 
- **`switch# conf t`**: Enters global configuration mode.
- **`switch(config)# int vlan1`**: Enters configuration mode for VLAN 1.
- **`switch(config-if)# no shutdown`**: Activates the VLAN interface.
- **`switch(config-if)# ip address 172.16.100.10 255.255.255.0`**: Assigns an IP address to VLAN 1.
- **`switch(config-if)# exit`**: Exits the VLAN configuration mode. Correct.
- **`switch(config)# ip default-gateway 172.16.10.1`**: Sets the default gateway for the switch.
- **`switch(config)# int fa1/0`**: Enters configuration mode for FastEthernet interface 1/0.
- **`switch(config-if)# switchport port-security mac-address <MAC address>`**: Here, instead of the actual MAC address, we can also use `sticky`. This states that the PC's MAC address will be made permanent here. `sticky` is a keyword.
- **`switch(config-if)# switchport port-security violation shutdown`**: Configures the switch to shut down the port if a violation occurs.

---

### **Configuration of Multiple Ports at Once**

**`switch(config)# int range f0/1 - n`**: Enters configuration mode for a range of FastEthernet interfaces (from fa0/1 to fa0/n) to apply settings simultaneously.

---

### **Configuration for VLANs**

- **`switch# conf t`**: Enters global configuration mode.
- **`switch(config)# vlan [vlan-id]`**: Creates a new VLAN with the specified VLAN ID.
- **`switch(config-vlan)# name [vlan-name]`**: Assigns a name to the newly created VLAN for identification.
- **`switch(config)# interface vlan [vlan-id]`**: Enters configuration mode for the VLAN interface.
- **`switch(config-if)# ip address [ip-address] [subnet-mask]`**: Assigns an IP address and subnet mask to the VLAN interface.
- **`switch(config-if)# no shutdown`**: Activates the VLAN interface.
- **`switch(config-if)# exit`**: Exits VLAN interface configuration mode back to global configuration mode.
- **`switch(config)# interface [interface-type] [interface-number]`**: Enters configuration mode for a switch port to assign it to the new VLAN.
  or
  **`switch(config)# interface range f0/1 - n`**
- **`switch(config-if)# switchport access vlan [vlan-id]`**: Assigns the switch port to the newly created VLAN.

---

### **Declaring Trunks**

- **`switch(config)# int g0/0`**: Enters configuration mode for GigabitEthernet interface 0/0.
- **`switch(config)# switchport mode trunk`**: Configures the interface as a trunk port.
- **`switch(config)# switchport trunk encapsulation dot1q`**: Configures the trunk port to use 802.1Q for VLAN tagging.

---

### **VTP (VLAN Trunking Protocol)**

- **`A# conf t`**: Enters global configuration mode.
- **`A(config)# vtp domain [domain-name]`**: Configures the VTP domain name for VLAN information sharing.
- **`A(config)# vtp mode [server|client|transparent]`**: Sets the VTP mode for the switch (server, client, or transparent).
- **`A(config)# vtp password [password]`**: Sets the VTP password for authentication between switches.
- **`A(config)# interface [interface-type] [interface-number]`**: Enters interface configuration mode for trunk settings.
- **`A(config-if)# switchport mode trunk`**: Configures the interface as a trunk to carry VLAN information.
- **`A# show vtp status`**: Displays the current VTP status, including the VTP mode and revision number.

---

### **Sub Interfaces**

- **`A# conf t`**: Enters global configuration mode.
- **`A(config)# interface [interface-type] [interface-number].[subinterface-number]`**: Creates a sub-interface for the specified physical interface.
- **`A(config-subif)# encapsulation dot1q [vlan-id]`**: Configures 802.1Q encapsulation for the sub-interface, specifying the VLAN ID.
- **`A(config-subif)# ip address [ip-address] [subnet-mask]`**: Assigns an IP address and subnet mask to the sub-interface.
- **`A(config-subif)# no shutdown`**: Activates the sub-interface.

---

### **Monitoring Commands**

- **`show vlan`**: Displays detailed information about all configured VLANs on the switch.
- **`show vlan brief`**: Provides a summary of VLANs, including their IDs and names.
- **`show int trunk`**: Shows trunk interfaces and their VLAN membership and status.
- **`show mac-address table`**: Displays MAC addresses learned on the switch ports along with their corresponding VLANs.
- **`show vtp status`**: Displays the VTP status, including mode, domain name, and revision number of the switch.