# API Overview

A browsable summary of the GreyScript API, generated from [ayecue/greyscript-meta](https://github.com/ayecue/greyscript-meta) (MIT licensed). It lists each type and its members with signatures and a one-line description.

!!! info "Canonical reference"
    For full descriptions, examples, and the newest additions, use the official searchable docs at [documentation.greyscript.org](https://documentation.greyscript.org). This page is a convenient offline-style summary, not a replacement.

**Signature key:** `name(arg: type, optional?: type) -> returnType`. A `?` marks an optional argument.


## Global functions

Functions available anywhere: shells, networking, I/O, math, strings, time.

| Signature | Description |
|---|---|
| `File(self: computer, path: string) -> file, null` | Returns a file located at the path provided in the arguments. |
| `abs(value?: number) -> number` | Returns the absolute value of number. |
| `acos(value?: number) -> number` | Returns the inverse cosine (in radians) of a number. |
| `active_net_card(self: computer) -> string, null` | Returns a string which contains either the keyword "WIFI" or "ETHERNET" depending on which connection type your computer is connected by. |
| `active_user() -> string` | Returns a string with the name of the user who is executing the current script. |
| `add_repo(self: aptClient, repository: string, port?: number) -> string, null` | Adds a repository address to the "/etc/apt/sources.txt" file. |
| `aircrack(self: crypto, path: string) -> string, null` | Returns a string containing the password based on the file which was generated via aireplay. |
| `aireplay(self: crypto, bssid: string, essid: string, maxAcks?: number) -> string, null` | Used to inject frames on wireless interfaces. |
| `airmon(self: crypto, option: string, device: string) -> number, string` | Enables or disables the monitor mode of a network device. |
| `allow_import(self: file) -> number, null` | Returns a number. |
| `amount_mined(self: blockchain, coinName: string) -> string, number, null` | Returns a number representing the total amount of mined coins. |
| `apply_patch(self: debugLibrary, path: string) -> string, null` | Applies a patch containing corrected code to the specified text file at the provided path. |
| `asin(value?: number) -> number` | Returns the inverse sine (in radians) of a number. |
| `atan(y?: number, x?: number) -> number` | Returns the inverse tangent (in radians) of a number. |
| `bitAnd(a?: number, b?: number) -> number` | Performs a bitwise AND for the provided values. |
| `bitOr(a?: number, b?: number) -> number` | Performs a bitwise OR for the provided values. |
| `bitXor(a?: number, b?: number) -> number` | Performs a bitwise XOR for the provided values. |
| `bitwise(operator: string, left: number, right: number) -> number, null` | Returns a number by performing bitwise operations. |
| `bssid_name(self: router) -> string, null` | Returns a string with the BSSID value of the router. |
| `build(self: shell, pathSource: string, pathBinary: string, allowImport?: number) -> string` | Compiles a plain code file provided in the arguments to a binary. |
| `buy_coin(self: wallet, coinName: string, coinAmount: number, unitPrice: number, subwalletUser: string) -> number, string` | Publishes a purchase offer indicating the number of coins you wish to buy and the price ($) per unit you are willing to pay. |
| `camera_link_system(self: trafficNet) -> number, string, null` | Accesses the traffic camera system, opening a window with controls to switch between different cameras. |
| `cancel_pending_trade(self: wallet, coinName: string) -> string, null` | Cancel any pending offer of a certain coin. |
| `cd(path?: string) -> string` | Changes the current working directory of the active shell to the specified path. |
| `ceil(value?: number) -> number` | Returns number rounded up to the integer value of the provided number. |
| `change_password(self: computer, user: string, pass: string) -> number, string, null` | Changes the password of an existing user on the computer. |
| `char(value?: number) -> string` | Returns the UTF-16 character string related to the provided unicode number. |
| `check_password(self: subWallet, password: string) -> number, string, null` | Returns a number with the value one if the credentials are correct, otherwise, the value is zero. |
| `check_upgrade(self: aptClient, filePath: string) -> string, number, null` | Verifies if there is a newer version of the program or library in the repository. |
| `chmod(self: file, perms?: string, isRecursive?: number) -> string, null` | Modifies the file permissions. |
| `clear_screen() -> null` | Removes any text existing in a Terminal prior to this point. |
| `close_program(self: computer, pid: number) -> number, string, null` | Closes a program associated with the provided PID. |
| `code(value: string) -> number` | Returns the Unicode number of the first character of the string. |
| `coin_price(self: blockchain) -> null, string, number` | Returns a number representing the current unit value of the cryptocurrency. |
| `command_info(commandName: string) -> string` | Returns a string value of a translation. |
| `connect_ethernet(self: computer, netDevice: string, localIp: string, gateway: string) -> string, null` | Sets up a new IP address on the computer through the ethernet connection. |
| `connect_service(self: shell, ip: string, port: number, user: string, password: string, service?: string) -> shell, ftpShell, string, null` | Returns a shell if the connection attempt to the provided IP was successful. |
| `connect_wifi(self: computer, netDevice: string, bssid: string, essid: string, pass: string) -> number, string, null` | Connects to the indicated Wi-Fi network. |
| `copy(self: file, path?: string, name?: string) -> string, number, null` | Copies the file to the provided path. |
| `cos(value?: number) -> number` | Returns the cosine of a number in radians. |
| `create_folder(self: computer, path: string, folder?: string) -> string, number, null` | Creates a folder at the path provided in the arguments. |
| `create_group(self: computer, user: string, group: string) -> number, string, null` | Creates a new group associated with an existing user on the computer. |
| `create_subwallet(self: coin, walletID: string, pin: string, subWalletUser: string, subWalletPass: string) -> string, number, null` | Registers a new account in the coin that can be used to manage services such as stores. |
| `create_user(self: computer, user: string, pass: string) -> number, string, null` | Creates a user on the computer, with the specified name and password. |
| `create_wallet(self: blockchain, user: string, password: string) -> string, wallet, null` | Creates a wallet and returns a wallet object on success, which can be used to manage cryptocurrencies. |
| `current_date() -> string` | Returns a string containing the current date and time. |
| `current_path() -> string` | Returns a string with the current active working directory. |
| `debug_tools(self: metaLib, user: string, password: string) -> string, debugLibrary, null` | Returns a library in debug mode as a debugLibrary object. |
| `decipher(self: crypto, encPass: string) -> string, null` | Returns a decrypted password via the provided password MD5 hash. |
| `decrypt(self: crypto, filePath: string, password: string) -> number, string, null` | Decrypts the specified file using the provided key. |
| `del_repo(self: aptClient, repository: string) -> string, null` | Removes a repository address from the "/etc/apt/sources.txt" file. |
| `delete(self: file) -> string, null` | Delete the current file. |
| `delete_coin(self: blockchain, coinName: string, user: string, password: string) -> number, string, null` | Removes a cryptocurrency from the world. |
| `delete_group(self: computer, user: string, group: string) -> number, string, null` | Deletes an existing group associated with an existing user on the computer. |
| `delete_mail(self: metaMail, mailId: string) -> number, string, null` | Delete the email corresponding to the provided email ID. |
| `delete_subwallet(self: subWallet) -> string, number, null` | Deletes the account registered in the cryptocurrency. |
| `delete_user(self: computer, user: string, removeHome?: number) -> number, string, null` | Deletes the indicated user from the computer. |
| `device_ports(self: router, ip: string) -> string, list<port>, null` | Returns a list where each item is an open port related to the device of the provided LAN IP address. |
| `devices_lan_ip(self: router) -> list<string>, null` | Returns a list where each item is a string representing a LAN IP address. |
| `dump_lib(self: netSession) -> metaLib, null` | Returns the metaLib associated with the remote service. |
| `encrypt(self: crypto, filePath: string, password: string) -> number, string, null` | Encrypts the specified file using the provided key. |
| `essid_name(self: router) -> string, null` | Returns a string with the ESSID value of the router. |
| `exit(message?: string) -> null` | Stops execution of the currently running script. |
| `fetch(self: metaMail) -> list<string>, string, null` | Returns a list where each item is a string containing mail id, from, subject and a small preview of the content consisting of the first 125 characters. |
| `firewall_rules(self: router) -> list<string>, null` | Returns a list where each item is a string containing a firewall rule. |
| `flood_connection(self: netSession) -> null` | Initiates a DDoS attack targeting the computer associated with the currently active netSession object. |
| `floor(value?: number) -> number` | Returns number rounded down to the integer value of the provided number. |
| `format_columns(columns: string) -> string` | Returns a string which is the formatted version of the provided text. |
| `funcRef() -> map<string,function>` | Returns a map which enables to extend function references with custom methods. |
| `get_abs_path(path: string, basePath?: string) -> string` | Returns the absolute path of the given path string. |
| `get_address(self: coin) -> string, null` | Returns the configured address that will be shown to users who do not have the currency, indicating where they have to register. |
| `get_balance(self: wallet, coinName: string) -> number, string, null` | Returns a number of coins of a given currency. |
| `get_balance_subwallet(self: subWallet) -> number, string, null` | Returns a number of coins of a given currency. |
| `get_coin(self: blockchain, coinName: string, user: string, password: string) -> string, coin, null` | Returns a coin object used to manage the currency. |
| `get_coin_name(self: blockchain, user: string, password: string) -> string, null` | Returns a string with the name of the coin owned by the player. |
| `get_content(self: file) -> string, null` | Returns a string representing the content of the file. |
| `get_creator_name(self: ctfEvent) -> string, null` | Returns a string with the name of the CTF event creator. |
| `get_credentials_info(self: trafficNet) -> string, null` | Returns string which contains job and name of a NPC. |
| `get_ctf(user: string, password: string, eventName: string) -> ctfEvent, string` | Returns ctfEvent object if there is one available. |
| `get_custom_object() -> map` | Returns map which is shared throughout script execution. |
| `get_cycle_mining(self: coin) -> string, number, null` | Returns a number representing the defined interval in which each user receives a coin reward when mining. |
| `get_description(self: ctfEvent) -> string, null` | Returns a string with the CTF event description. |
| `get_files(self: file) -> list<file>, null` | Returns a list of files. |
| `get_folders(self: file) -> list<file>, null` | Returns a list of folders. |
| `get_global_offers(self: wallet, coinName: string) -> string, map<string,list>, null` | Returns a map with all the offers made by any player of a given currency. |
| `get_info(self: subWallet) -> string, null` | Returns a string with the information stored by the coin creator. |
| `get_lan_ip(self: port) -> string, null` | Returns a string containing the local IP address of the computer to which the port is pointing. |
| `get_mail_content(self: ctfEvent) -> string, null` | Returns a string with the mail content of the CTF event. |
| `get_mined_coins(self: coin) -> string, number, null` | Returns a number representing the amount of coins that have been mined so far. |
| `get_name(self: computer) -> string` | Returns the hostname of the machine. |
| `get_num_conn_gateway(self: netSession) -> number, null` | Returns the number of devices using this router as a gateway. |
| `get_num_portforward(self: netSession) -> number, null` | Returns the number of ports forwarded by this router. |
| `get_num_users(self: netSession) -> number, null` | Returns the number of user accounts on the system. |
| `get_pending_trade(self: wallet, coinName: string) -> string, list, null` | Returns a list with the pending sale or purchase offer of this wallet for a certain currency. |
| `get_pin(self: wallet) -> string, null` | Returns a string with a PIN that refreshes every few minutes. |
| `get_ports(self: computer) -> list<port>, null` | Returns a list of ports on the computer which are active. |
| `get_reward(self: coin) -> string, number, null` | Returns a number representing the amount of coins that will be received as a reward after each mining cycle. |
| `get_router(ipAddress?: string) -> router, null` | Returns by default the router to which the executing computer is connected to. |
| `get_shell(user?: string, pass?: string) -> shell, null` | Returns the shell that is executing the current script. |
| `get_subwallet(self: coin, subWalletUser: string) -> string, subWallet, null` | Returns a subWallet object on success. |
| `get_subwallets(self: coin) -> string, list<subWallet>, null` | Returns a list where each item is a subWallet object, including all the accounts registered in the cryptocurrency. |
| `get_switch(ipAddress: string) -> router, null` | Returns the switch on the local network whose IP address matches, otherwise it returns null. |
| `get_template(self: ctfEvent) -> string, null` | Returns a string with the CTF event template. |
| `get_user(self: subWallet) -> string, null` | Returns a string with the username associated with this subwallet. |
| `group(self: file) -> string, null` | Returns a string with the name of the group to which this file belongs. |
| `groups(self: computer, user: string) -> string, null` | Returns a string containing groups associated with an existing user on the computer. |
| `hasIndex(value: any, index: any) -> number, null` | Verifies if an index is available within an object. |
| `has_permission(self: file, perms?: string) -> number, null` | Returns a number indicating if the user who launched the script has the requested permissions. |
| `hash(value: any) -> number` | Returns numeric hash for the provided data. |
| `home_dir() -> string` | Returns a string with the home folder path of the user who is executing the current script. |
| `host_computer(self: shell) -> computer, null` | Returns a computer related to the shell. |
| `import_code(path: string) -> null` | Enables to import code from different sources into one file. |
| `include_lib(path: string) -> crypto, metaxploit, service, blockchain, aptClient, smartAppliance, trafficNet, null` | Enables the inclusion of library binaries, which can be used inside your script. |
| `indexOf(self: any, value: any, after: any) -> any` | Lookups index of value within maps, lists, or strings. |
| `indexes(self: any) -> list, null` | Returns a list containing all indexes or keys of the passed object. |
| `insert(object: any, index: number, value: any) -> list, string` | Inserts a value into either a list or a string. |
| `install(self: aptClient, package: string, customPath?: string) -> string, number, null` | Installs a program or library from a remote repository listed in "/etc/apt/sources.txt". |
| `install_service(self: service) -> number, string, null` | Installs the necessary files for the correct functioning of the service and starts it. |
| `is_any_active_user(self: netSession) -> number, null` | Returns a number. |
| `is_binary(self: file) -> number, null` | Returns a number. |
| `is_closed(self: port) -> number, null` | Returns a number, where one indicates that the specified port is closed and zero indicates that the port is open. |
| `is_encrypted(self: crypto, filePath: string) -> number, string, null` | Checks whether the specified file is encrypted. |
| `is_folder(self: file) -> number, null` | Returns a number. |
| `is_lan_ip(ip: string) -> number` | Returns a number. |
| `is_match(value: string, pattern: string, regexOptions?: string) -> number` | Uses regular expression to check if a string matches a certain pattern. |
| `is_network_active(self: computer) -> number, null` | Returns a number with either the value one or zero. |
| `is_patched(self: metaLib, getdate: number) -> number, string, null` | Returns by default a number indicating whether the library has been patched. |
| `is_root_active_user(self: netSession) -> number, null` | Returns a number. |
| `is_symlink(self: file) -> number, null` | Returns a number. |
| `is_valid_ip(ip: string) -> number` | Returns a number. |
| `join(value: list, delimiter?: string) -> string` | Returns a concatenated string containing all stringified values inside the list. |
| `kernel_version(self: router) -> string, null` | Returns a string with the version of the kernel_router.so library. |
| `lan_ip(self: computer) -> string, null` | Returns a string with the local IP address of the computer. |
| `lastIndexOf(self: string, searchStr: string) -> number, null` | Returns a number indicating the last matching index of the provided value inside the string. |
| `last_transaction(self: subWallet) -> list<list>, number, string, null` | Returns a list with the information of the last transaction. |
| `launch(self: shell, program: string, params?: string) -> string, number` | Launches the binary located at the provided path. |
| `launch_path() -> string` | Returns a string containing the path of the script that was initially executed, meaning that even when using launch, it will still return the path of the initially executed script. |
| `len(self: any) -> number, null` | Returns number indicating what size the passed object is. |
| `lib_name(self: metaLib) -> string, null` | Returns a string containing the name of the library. |
| `list() -> map<string,function>` | Returns a map which enables to extend list types with custom methods. |
| `list_coins(self: wallet) -> list<string>, string, null` | Returns a list where each item is a string with the names of the coins available in the wallet. |
| `list_global_coins(self: wallet) -> string, list<string>, null` | Returns a list where each item is a string containing the names of all the currencies that exist. |
| `load(self: metaxploit, path: string) -> metaLib, null` | Returns a metaLib object for the provided path to the library binary. |
| `local_ip(self: router) -> string, null` | Returns a string with the local IP address of the router. |
| `locate_vehicle(self: trafficNet, licensePlate: string, password: string) -> number, string, null` | Performs a search for the specified license plate to locate the vehicle. |
| `log(value?: number, base?: number) -> number` | Returns the natural logarithm of a number. |
| `login_wallet(self: blockchain, user: string, password: string) -> string, wallet, null` | Returns a wallet object on success. |
| `lower(self: string) -> string` | Returns a string which is the lowercase transformed version of the provided string. |
| `mail_login(user: string, pass: string) -> metaMail, string, null` | Returns a MetaMail entity if the login was successful. |
| `map() -> map<string,function>` | Returns a map which enables to extend map types with custom methods. |
| `matches(value: string, pattern: string, regexOptions?: string) -> map<number,string>` | Returns a map with all search results for the provided regular expression. |
| `md5(value: string) -> string` | Returns the MD5 hash string of the provided string. |
| `mining(self: subWallet) -> number, string, null` | Starts the process of mining the cryptocurrency. |
| `model(self: smartAppliance) -> string, null` | Returns a string with the appliance model ID. |
| `move(self: file, path?: string, fileName?: string) -> string, number, null` | Moves the file to the provided path. |
| `name(self: file) -> string, null` | Returns a string with the name of the file. |
| `net_use(self: metaxploit, ip: string, port?: number) -> netSession, null` | Returns a netSession object for the provided IP address and port. |
| `network_devices(self: computer) -> string, null` | Returns a string containing all network devices available on the computer, with each item providing information about the interface name, chipset, and whether monitoring support is |
| `network_gateway(self: computer) -> string` | Returns a string with the gateway IP address configured on the computer. |
| `nslookup(webAddress: string) -> string` | Returns the IP address for the provided web address. |
| `number() -> map<string,function>` | Returns a map which enables to extend number types with custom methods. |
| `overflow(self: metaLib, memoryAddress: string, unsecZone: string, optArgs?: string) -> string, number, shell, computer, file, null` | Exploits vulnerabilities in target systems by executing various attack vectors against libraries located in the "/lib" folder. |
| `override_settings(self: smartAppliance, power: number, temperature: number) -> string, number, null` | Overrides the power and temperature settings of the appliance. |
| `owner(self: file) -> string, null` | Returns a string with the name of the file owner. |
| `parent(self: file) -> file, null` | Returns the parent folder of the current file or folder. |
| `parent_path(directory: string) -> string` | Returns a string which is the parent path of the provided path. |
| `path(self: file, symlinkOrigPath?: number) -> string, null` | Returns a string containing the file path. |
| `payload(self: debugLibrary, memZone: string, pathFile?: string) -> string, list<map>, null` | Returns a list containing a single partial computer object if zero-day vulnerabilities are detected within the specified memory zone. |
| `permissions(self: file) -> string, null` | Returns a string with the current file permissions. |
| `pi() -> number` | Returns the number PI to the precision of six. |
| `ping(self: shell, ip: string) -> string, number, null` | Returns a number. |
| `ping_port(self: router, port: number) -> port, null` | Returns a port that is behind the port number provided. |
| `player_success(self: ctfEvent) -> number, null` | Returns a number with the value one if the CTF event was completed successfully. |
| `pop(self: any) -> any` | When passing a list to this method, it will return the value at the last index and remove it from the list. |
| `port_info(self: router, port: port) -> string, null` | Returns a string with information about the provided port, including details about the running service and its version. |
| `port_number(self: port) -> number, null` | Returns the number which is used for the port. |
| `print(value?: any, replaceText?: number) -> null` | Print a message on the Terminal. |
| `program_path() -> string` | Returns a string containing the path of the script that is currently executing. |
| `public_ip(self: router) -> string, null` | Returns a string with the public IP address of the router. |
| `public_ip_pc(self: computer) -> string, null` | Returns a string with the public IP address of the computer. |
| `pull(self: any) -> any` | When passing a list to this method, it will return the value at the first index and remove it from the list. |
| `push(self: any, value: any) -> list, map, null` | Allows pushing a value into an object, supporting maps and lists. |
| `range(start?: number, end?: number, inc: number) -> list<number>` | Generates a list where each item is a number. |
| `read(self: metaMail, mailId: string) -> string, null` | Returns a string containing the content of a mail related to the provided mail id. |
| `reboot(self: computer, safeMode?: number) -> number, string, null` | Reboots a computer. |
| `remove(self: any, key: any) -> number, null, string` | Depending on the data type, this function will remove a value in the provided object, potentially mutating the object. |
| `rename(self: file, name?: string) -> string, number` | Rename the file with the name provided. |
| `replace(value: any, oldVal: any, newVal: any, maxCount: number) -> any` | This function replaces a value within an object and returns the mutated object. |
| `replace_regex(self: string, pattern: string, newValue: string, regexOptions?: string) -> string` | Returns a string with the replaced content by using regular expressions. |
| `reset_ctf_password(newPassword: string) -> number, string` | Resets the password of your CTF account. |
| `reset_password(self: wallet, newPassword: string) -> number, string, null` | Change the password of the wallet. |
| `reset_password_coin(self: coin, newPassword: string) -> number, string, null` | Resets the password of the coin. |
| `reverse(value: list) -> null` | Reverses the order of all values in the list. |
| `rnd(seed: number) -> number` | Returns a random number between 0 and 1. |
| `round(value?: number, fixed?: number) -> number` | Returns number rounded to the integer value of the provided number. |
| `rshell_client(self: metaxploit, ip: string, port?: number, processName?: string) -> string, number, null` | Launches a process on the victim's computer, silently attempting to continuously connect in the background to the specified address and port. |
| `rshell_server(self: metaxploit) -> string, list<shell>, null` | This method returns a list of shell objects that have been reverse shell connected to this computer. |
| `scan(self: metaxploit, metaLib: metaLib) -> list<string>, null` | Returns a list where each item is a string representing a memory area which has vulnerabilities related to the provided library. |
| `scan_address(self: metaxploit, metaLib: metaLib, memoryAddress: string) -> string, null` | Returns a string containing information about each vulnerability in the provided library and memory area. |
| `scan_debuglib(self: debugLibrary) -> string, null` | Scans the library in debug mode to identify potential code errors that may lead to vulnerabilities. |
| `scp(self: shell, sourceFile: string, destinationFolder: string, remoteShell: shell, isUpload?: number) -> number, string, null` | Send a file to the computer related to the provided shell. |
| `search(self: aptClient, search: string) -> string, null` | The search method specifically looks for a package in any of the repositories listed in "/etc/apt/sources.txt". |
| `sell_coin(self: wallet, coinName: string, coinAmount: number, unitPrice: number, subwalletUser: string) -> number, string` | Publishes a sale offer indicating the amount of coins you want to sell and the price ($) per unit you want to assign. |
| `send(self: metaMail, emailAddress: string, subject: string, message: string) -> string, number, null` | Send a new mail to the provided email address. |
| `set_address(self: coin, address: string) -> number, string, null` | Configures a valid address that will be shown to users who do not have the currency, indicating where to register. |
| `set_alarm(self: smartAppliance, enable: number) -> string, number, null` | Activates or deactivates the sound alarm indicating any appliance malfunction. |
| `set_content(self: file, content?: string) -> string, number, null` | Saves text into a file. |
| `set_cycle_mining(self: coin, rateHours?: number) -> string, number, null` | Defines the interval (in-game hours) in which each user receives a coin reward when mining. |
| `set_group(self: file, group?: string, recursive?: number) -> string, null` | Change the group related to this file. |
| `set_info(self: subWallet, info: string) -> number, string, null` | Stores optional information in the Subwallet for any use. |
| `set_owner(self: file, owner?: string, recursive?: number) -> string, null` | Change the owner of this file. |
| `set_reward(self: coin, coinAmount?: number) -> number, string, null` | Assigns the reward that miners will receive after each mining cycle. |
| `show(self: aptClient, repository: string) -> string, null` | Displays all the packages available in a repository. |
| `show_history(self: blockchain, coinName: string) -> map<number,list>, string, null` | Returns a map with the latest changes in the value of a specific cryptocurrency. |
| `show_nodes(self: wallet, coinName: string) -> string, number, null` | Returns a number representing the count of devices mining a specific coin for the same wallet. |
| `show_procs(self: computer) -> string, null` | Returns a string providing an overview of all active processes on the computer. |
| `shuffle(self: any) -> null` | Randomizes content of an object. |
| `sign(value?: number) -> number` | Returns a one or minus one, indicating the sign of the number passed as argument. |
| `sin(value?: number) -> number` | Returns the sine of a number in radians. |
| `size(self: file) -> string, null` | Returns a string with the size of the file in bytes. |
| `slice(value: any, startIndex?: number, endIndex: number) -> list, string, null` | Returns a sliced version of the passed object. |
| `smtp_user_list(self: crypto, ip: string, port: number) -> list<string>, string, null` | Returns a list of the existing users on the computer where the SMTP service is running. |
| `sniffer(self: metaxploit, saveEncSource?: number) -> string, null` | The terminal listens to the network packets of any connection that passes through the computer. |
| `sort(self: list, byKey: any, ascending?: number) -> list` | Sorts the values of a list alphanumerically. |
| `split(self: string, pattern: string, regexOptions?: string) -> list<string>, null` | Returns a list where each item is a segment of the string, separated by the provided separator string. |
| `sqrt(value?: number) -> number` | Returns the square root of a number. |
| `start_service(self: service) -> number, string, null` | Starts the service and opens its associated port on the local machine. |
| `start_terminal(self: shell) -> null` | Launches an active terminal. |
| `stop_service(self: service) -> number, string, null` | Stops the service and closes its associated port on the local machine. |
| `str(value: any) -> string` | Returns the string value of provided data. |
| `string() -> map<string,function>` | Returns a map which enables to extend string types with custom methods. |
| `sum(self: any) -> number` | Returns a number representing the sum of all items within a map or a list. |
| `symlink(self: file, path?: string, newName?: string) -> string, number, null` | Creates a symlink to the specified path. |
| `tan(value?: number) -> number` | Returns the tangent of a number in radians. |
| `time() -> number` | Returns a number of seconds representing the elapsed time since the script started. |
| `to_int(self: string) -> string, number, null` | Returns a number which is parsed from the string as an integer. |
| `touch(self: computer, path: string, fileName: string) -> number, string, null` | Creates an empty text file at the provided path. |
| `transaction(self: coin, subWalletOrig: string, subWalletDest: string, valAmount: number) -> string, number, null` | Makes a transaction of the currency between the indicated subwallets. |
| `trim(self: string) -> string, null` | Returns a new string stripped of any spacing at the beginning and ending. |
| `typeof(value: any) -> string` | Returns a string containing the type of the entity provided. |
| `unit_testing(self: debugLibrary, errorLines: list<number>) -> string, null` | Conducts automated tests on the specified lines of code. |
| `update(self: aptClient) -> string, number` | Refreshes the list of available packages after adding a new repository in "/etc/apt/sources.txt", or if the remote repository has updated its information in "/server/conf/repod.con |
| `upper(self: string) -> string` | Returns a string which is the uppercase transformed version of the provided string. |
| `used_ports(self: router) -> list<port>, null` | Returns a list where each item is a port used inside the router. |
| `user_bank_number() -> string, null` | Returns a string containing the bank account number of the player who is executing the script. |
| `user_input(message?: string, isPassword?: number, anyKey?: number, addToHistory?: number) -> string` | Pauses script execution to receive input from the user. |
| `user_mail_address() -> string, null` | Returns a string containing the email address of the player who is executing the script. |
| `val(self?: any) -> number, null` | Casts a string to a number. |
| `values(self: any) -> list` | Returns a list containing all values of an object. |
| `version(self: metaLib) -> string, null` | Returns a string containing the version number of the library. |
| `wait(delay?: number) -> null` | Pauses the script execution. |
| `wallet_username(self: subWallet) -> string, null` | Returns a string with the name of the wallet to which this subwallet belongs. |
| `whois(ip: string) -> string` | Returns a string containing the administrator information behind an IP address provided. |
| `wifi_networks(self: computer, netDevice: string) -> list<string>, null` | Returns a list of the Wi-Fi networks that are available for the provided interface. |
| `yield() -> null` | Waits for the next tick. |


## shell

A command session. Build binaries, launch programs, scp, connect to services.

| Signature | Description |
|---|---|
| `build(pathSource: string, pathBinary: string, allowImport?: number) -> string` | Compiles a plain code file provided in the arguments to a binary. |
| `connect_service(ip: string, port: number, user: string, password: string, service?: string) -> shell, ftpShell, string, null` | Returns a shell if the connection attempt to the provided IP was successful. |
| `host_computer() -> computer` | Returns a computer related to the shell. |
| `launch(program: string, params?: string) -> string, number` | Launches the binary located at the provided path. |
| `ping(ip: string) -> string, number` | Returns a number. |
| `scp(file: string, folder: string, remoteShell: shell, isUpload?: number) -> number, string, null` | Send a file to the computer related to the provided shell. |
| `start_terminal() -> null` | Launches an active terminal. |


## computer

A machine: files, users, groups, processes, network cards, Wi-Fi.

| Signature | Description |
|---|---|
| `File(path: string) -> file, null` | Returns a file located at the path provided in the arguments. |
| `active_net_card() -> string` | Returns a string which contains either the keyword "WIFI" or "ETHERNET" depending on the connection type your computer is currently using. |
| `change_password(username: string, password: string) -> number, string, null` | Changes the password of an existing user on the computer. |
| `close_program(pid: number) -> number, string, null` | Closes a program associated with the provided PID. |
| `connect_ethernet(netDevice: string, address: string, gateway: string) -> string, null` | Sets up a new IP address on the computer through the Ethernet connection. |
| `connect_wifi(netDevice: string, bssid: string, essid: string, password: string) -> number, string, null` | Connects to the indicated Wi-Fi network. |
| `create_folder(path: string, folder?: string) -> string, number` | Creates a folder at the path provided in the arguments. |
| `create_group(username: string, group: string) -> number, string, null` | Creates a new group associated with an existing user on the computer. |
| `create_user(usename: string, password: string) -> number, string, null` | Creates a user on the computer with the specified name and password. |
| `delete_group(username: string, group: string) -> number, string, null` | Deletes an existing group associated with an existing user on the computer. |
| `delete_user(username: string, removeHome?: number) -> number, string, null` | Deletes the indicated user from the computer. |
| `get_name() -> string` | Returns the hostname of the machine. |
| `get_ports() -> list<port>` | Returns a list of ports on the computer that are active. |
| `groups(username: string) -> string, null` | Returns a string containing groups associated with an existing user on the computer. |
| `is_network_active() -> number` | Returns a number with either the value one or zero. |
| `local_ip() -> string` | Returns a string with the local IP address of the computer. |
| `network_devices() -> string` | Returns a string containing information about all network devices available on the computer. |
| `network_gateway() -> string` | Returns a string with the gateway IP address configured on the computer. |
| `public_ip() -> string` | Returns a string with the public IP address of the computer. |
| `reboot(safeMode?: number) -> number, string, null` | Reboots the computer. |
| `show_procs() -> string` | Returns a string with an overview of all active processes on the computer, including information about the user, PID, CPU, memory, and command. |
| `touch(path: string, fileName: string) -> number, string` | Creates an empty text file at the provided path. |
| `wifi_networks(netDevice: string) -> list<string>, null` | Returns a list of the Wi-Fi networks that are available for the provided interface. |


## file

Files and folders: content, permissions, ownership, copy/move/delete.

| Signature | Description |
|---|---|
| `allow_import() -> number` | Returns a number. |
| `chmod(perms?: string, isRecursive?: number) -> string` | Modifies the file permissions. |
| `copy(path?: string, name?: string) -> string, number, null` | Copies the file to the provided path. |
| `delete() -> string` | Delete the current file. |
| `get_content() -> string, null` | Returns a string representing the content of the file. |
| `get_files() -> list<file>, null` | Returns a list of files. |
| `get_folders() -> list<file>, null` | Returns a list of folders. |
| `group() -> string, null` | Returns a string with the name of the group to which this file belongs. |
| `has_permission(perms?: string) -> number, null` | Returns a number indicating if the user who launched the script has the requested permissions. |
| `is_binary() -> number, null` | Returns a number. |
| `is_folder() -> number, null` | Returns a number. |
| `is_symlink() -> number, null` | Returns a number. |
| `move(path?: string, fileName?: string) -> string, number, null` | Moves the file to the provided path. |
| `name() -> string, null` | Returns a string with the name of the file. |
| `owner() -> string, null` | Returns a string with the name of the file owner. |
| `parent() -> file, null` | Returns the parent folder of the current file or folder. |
| `path(symlinkOrigPath?: number) -> string` | Returns a string containing the file path. |
| `permissions() -> string, null` | Returns a string with the current file permissions. |
| `rename(name?: string) -> string, number` | Rename the file with the name provided. |
| `set_content(content?: string) -> string, number, null` | Saves text into a file. |
| `set_group(group?: string, recursive?: number) -> string, null` | Change the group related to this file. |
| `set_owner(owner?: string, recursive?: number) -> string, null` | Change the owner of this file. |
| `size() -> string, null` | Returns a string with the size of the file in bytes. |
| `symlink(path?: string, newName?: string) -> string, number, null` | Creates a symlink to the specified path. |


## metaxploit

The metaxploit.so toolkit: load libraries, open net sessions, scan memory.

| Signature | Description |
|---|---|
| `load(path: string) -> metaLib, null` | Returns a metaLib object for the provided path to the library binary. |
| `net_use(ip: string, port?: number) -> netSession, null` | Returns a netSession object for the provided IP address and port. |
| `rshell_client(ip: string, port?: number, processName?: string) -> string, number, null` | Launches a process on the victim's computer, silently attempting to continuously connect in the background to the specified address and port. |
| `rshell_server() -> string, list<shell>` | This method returns a list of shell objects that have been reverse shell connected to this computer. |
| `scan(metaLib: metaLib) -> list<string>, null` | Returns a list where each item is a string representing a memory area which has vulnerabilities related to the provided library. |
| `scan_address(metaLib: metaLib, memoryAddress: string) -> string, null` | Returns a string containing information about each vulnerability in the provided library and memory area. |
| `sniffer(saveEncSource?: number) -> string, null` | The terminal listens to the network packets of any connection that passes through the computer. |


## metaLib

A loaded library you can analyse for vulnerabilities.

| Signature | Description |
|---|---|
| `debug_tools(user: string, password: string) -> string, debugLibrary, null` | Returns a library in debug mode as a debugLibrary object. |
| `is_patched(getdate: number) -> number, string, null` | Returns by default a number indicating whether the library has been patched. |
| `lib_name() -> string` | Returns a string containing the name of the library. |
| `overflow(memoryAddress: string, unsecZone: string, optArgs?: string) -> string, number, shell, computer, file, null` | Exploits vulnerabilities in target systems by executing various attack vectors against libraries located in the "/lib" folder. |
| `version() -> string` | Returns a string containing the version number of the library. |


## netSession

A connection to a remote service.

| Signature | Description |
|---|---|
| `dump_lib() -> metaLib` | Returns the metaLib associated with the remote service. |
| `flood_connection() -> null` | Initiates a DDoS attack targeting the computer associated with the currently active netSession object. |
| `get_num_conn_gateway() -> number` | Returns the number of devices using this router as a gateway. |
| `get_num_portforward() -> number` | Returns the number of ports forwarded by this router. |
| `get_num_users() -> number` | Returns the number of user accounts on the system. |
| `is_any_active_user() -> number` | Returns a number. |
| `is_root_active_user() -> number` | Returns a number. |


## crypto

The crypto.so toolkit: Wi-Fi tools and hash deciphering.

| Signature | Description |
|---|---|
| `aircrack(path: string) -> string, null` | Returns a string containing the password based on the file which was generated via aireplay. |
| `aireplay(bssid: string, essid: string, maxAcks?: number) -> string, null` | Used to inject frames on wireless interfaces. |
| `airmon(option: string, device: string) -> number, string` | Enables or disables the monitor mode of a network device. |
| `decipher(encPass: string) -> string, null` | Returns a decrypted password via the provided password MD5 hash. |
| `decrypt(filePath: string, password: string) -> number, string, null` | Decrypts the specified file using the provided key. |
| `encrypt(filePath: string, password: string) -> number, string, null` | Encrypts the specified file using the provided key. |
| `is_encrypted(filePath: string) -> number, string, null` | Checks whether the specified file is encrypted. |
| `smtp_user_list(ip: string, port: number) -> list<string>, string, null` | Returns a list of the existing users on the computer where the SMTP service is running. |


## router

A router: LAN devices, forwarded ports, firewall rules.

| Signature | Description |
|---|---|
| `bssid_name() -> string` | Returns a string with the BSSID value of the router. |
| `device_ports(ip: string) -> string, list<port>, null` | Returns a list where each item is an open port related to the device of the provided LAN IP address. |
| `devices_lan_ip() -> list<string>` | Returns a list where each item is a string representing a LAN IP address. |
| `essid_name() -> string` | Returns a string with the ESSID value of the router. |
| `firewall_rules() -> list<string>` | Returns a list where each item is a string containing a firewall rule. |
| `kernel_version() -> string` | Returns a string with the version of the kernel_router.so library. |
| `local_ip() -> string` | Returns a string with the local IP address of the router. |
| `ping_port(port: number) -> port, null` | Returns a port that is behind the port number provided. |
| `port_info(port: port) -> string, null` | Returns a string with information about the provided port, including details about the running service and its version. |
| `public_ip() -> string` | Returns a string with the public IP address of the router. |
| `used_ports() -> list<port>` | Returns a list where each item is a port used inside the router. |


## port

A network port on a host.

| Signature | Description |
|---|---|
| `get_lan_ip() -> string` | Returns a string containing the local IP address of the computer to which the port is pointing. |
| `is_closed() -> number` | Returns a number, where one indicates that the specified port is closed and zero indicates that the port is open. |
| `port_number() -> number` | Returns the number which is used for the port. |


## ftpShell

An FTP session.

| Signature | Description |
|---|---|
| `host_computer() -> ftpComputer` | Returns a computer related to the shell. |
| `scp(sourceFile: string, destinationFolder: string, remoteShell: shell, isUpload?: number) -> number, string, null` | Send a file to the computer related to the provided shell. |


## string

String methods.

| Signature | Description |
|---|---|
| `code() -> number` | Returns a number representing the Unicode code of the first character of the string. |
| `hasIndex(index: number) -> number` | Returns a number. |
| `indexOf(value: string, offset: number) -> number, null` | Returns a number which indicates the first matching index of the provided value inside the list. |
| `indexes() -> list<number>` | Returns a list where each item is a number representing all available indexes in the string. |
| `insert(index: number, value: string) -> string` | Returns a string with the newly inserted string at the provided index. |
| `is_match(pattern: string, regexOptions?: string) -> number` | Uses regular expression to check if a string matches a certain pattern. |
| `lastIndexOf(searchStr: string) -> number` | Returns a number which indicates the last matching index of the provided value inside the list. |
| `len() -> number` | Returns a number representing the length of the string. |
| `lower() -> string` | Returns a new string in which all characters are transformed into lowercase. |
| `matches(pattern: string, regexOptions?: string) -> map<number,string>` | Returns a map with all search results for the provided regular expression. |
| `remove(value: string) -> string` | Returns a new string with the provided value removed. |
| `replace(pattern: string, newValue: string, regexOptions?: string) -> string` | Returns a string with the replaced content by using regular expressions. |
| `split(pattern: string, regexOptions?: string) -> list<string>, null` | Returns a list where each item is a segment of the string, separated by the provided separator string. |
| `to_int() -> string, number` | Returns a number which is parsed from the string as an integer. |
| `trim() -> string` | Returns a new string stripped of any spacing at the beginning and ending. |
| `upper() -> string` | Returns a new string in which all characters are transformed into uppercase. |
| `val() -> number` | Returns a number which is parsed from the string. |
| `values() -> list<string>` | Returns a list where each item is a string representing all available characters in the string. |


## list

List methods.

| Signature | Description |
|---|---|
| `hasIndex(index: number) -> number` | Returns a number. |
| `indexOf(value: any, offset: number) -> number, null` | Returns a number which indicates the first matching index of the provided value inside the list. |
| `indexes() -> list<number>` | Returns a list containing all available indexes. |
| `insert(index: number, value: any) -> list` | Inserts a value into the list at the index provided. |
| `join(delimiter: string) -> string` | Returns a concatenated string containing all stringified values inside the list. |
| `len() -> number` | Returns a number representing the count of values inside the list. |
| `pop() -> any` | Returns and removes the last item in the list. |
| `pull() -> any` | Returns and removes the first item in the list. |
| `push(value: any) -> list` | Appends a value to the end of the list. |
| `remove(index: number) -> null` | Removes an item from the list with the provided index. |
| `replace(oldVal: any, newVal: any, maxCount: number) -> list` | Returns updated list where each value matching with the provided replace argument gets replaced. |
| `reverse() -> null` | Reverses the order of all values in the list. |
| `shuffle() -> null` | Shuffles all values in the list. |
| `sort(key: any, ascending?: number) -> list` | Sorts the values of a list alphanumerically. |
| `sum() -> number` | Returns sum of all values inside the list. |
| `values() -> list` | Returns a list containing all available values. |


## map

Map methods.

| Signature | Description |
|---|---|
| `hasIndex(key: any) -> number` | Returns a number. |
| `indexOf(value: any) -> any` | Returns a value which can be of any type since map keys can be of any type. |
| `indexes() -> list` | Returns a list containing all available keys. |
| `len() -> number` | Returns a number representing the count of items inside the map. |
| `pop() -> any` | Returns and removes the first item in the map. |
| `pull() -> any` | Returns and removes the first item in the map. |
| `push(key: any) -> map` | Adds the value 1 to the provided key. |
| `remove(key: string) -> number` | Removes an item from the map with the provided key. |
| `replace(oldVal: any, newVal: any, maxCount: number) -> map` | Returns updated map where each value matching with the provided replace argument gets replaced. |
| `shuffle() -> null` | Shuffles all values in the map. |
| `sum() -> number` | Returns sum of all values inside the map. |
| `values() -> list` | Returns a list containing all available values within map. |


## number

Number helpers.


## blockchain

The blockchain.so toolkit for coins and wallets.

| Signature | Description |
|---|---|
| `amount_mined(coinName: string) -> string, number, null` | Returns a number representing the total amount of mined coins. |
| `coin_price(coinName: string) -> null, string, number` | Returns a number representing the current unit value of the cryptocurrency. |
| `create_wallet(user: string, password: string) -> string, wallet, null` | Creates a wallet and returns a wallet object on success, which can be used to manage cryptocurrencies. |
| `delete_coin(coinName: string, user: string, password: string) -> number, string, null` | Removes a cryptocurrency from the world. |
| `get_coin(coinName: string, user: string, password: string) -> string, coin, null` | Returns a coin object used to manage the currency. |
| `get_coin_name(user: string, password: string) -> string, null` | Returns a string with the name of the coin owned by the player. |
| `login_wallet(user: string, password: string) -> string, wallet, null` | Returns a wallet object on success. |
| `show_history(coinName: string) -> map<number,list>, string, null` | Returns a map with the latest changes in the value of a specific cryptocurrency. |


## wallet

A crypto wallet.

| Signature | Description |
|---|---|
| `buy_coin(coinName: string, coinAmount: number, unitPrice: number, subwalletUser: string) -> number, string` | Publishes a purchase offer indicating the number of coins you wish to buy and the price ($) per unit you are willing to pay. |
| `cancel_pending_trade(coinName: string) -> string, null` | Cancel any pending offer of a certain coin. |
| `get_balance(coinName: string) -> number, string, null` | Returns a number of coins of a given currency. |
| `get_global_offers(coinName: string) -> string, map<string,list>, null` | Returns a map with all the offers made by any player of a given currency. |
| `get_pending_trade(coinName: string) -> string, list, null` | Returns a list with the pending sale or purchase offer of this wallet for a certain currency. |
| `get_pin() -> string` | Returns a string with a PIN that refreshes every few minutes. |
| `list_coins() -> list<string>, string` | Returns a list where each item is a string with the names of the coins available in the wallet. |
| `list_global_coins() -> string, list<string>` | Returns a list where each item is a string containing the names of all the currencies that exist. |
| `reset_password(newPassword: string) -> number, string, null` | Change the password of the wallet. |
| `sell_coin(coinName: string, coinAmount: number, unitPrice: number, subwalletUser: string) -> number, string` | Publishes a sale offer indicating the amount of coins you want to sell and the price ($) per unit you want to assign. |
| `show_nodes(coinName: string) -> string, number, null` | Returns a number representing the count of devices mining a specific coin for the same wallet. |


## aptClient

The apt-get client object.

| Signature | Description |
|---|---|
| `add_repo(repository: string, port?: number) -> string, null` | Inserts a repository address into the "/etc/apt/sources.txt" file. |
| `check_upgrade(filepath: string) -> string, number, null` | Checks if there is a newer version of the program or library in the repository. |
| `del_repo(repository: string) -> string, null` | Deletes a repository address from the "/etc/apt/sources.txt" file. |
| `install(package: string, customPath?: string) -> string, number, null` | Installs a program or library from a remote repository listed in "/etc/apt/sources.txt". |
| `search(search: string) -> string, null` | Search specifically looks for a package in any of the repositories listed in "/etc/apt/sources.txt". |
| `show(repository: string) -> string, null` | Show displays all the packages available in a repository. |
| `update() -> string, number` | Update refreshes the list of available packages after adding a new repository in "/etc/apt/sources.txt", or if the remote repository has updated its information in "/server/conf/re |


## ctfEvent

CTF event helpers.

| Signature | Description |
|---|---|
| `get_creator_name() -> string` | Returns string with the name of the CTF event creator. |
| `get_description() -> string` | Returns string with the CTF event description. |
| `get_mail_content() -> string` | Returns string with the mail content of the CTF event. |
| `get_template() -> string` | Returns string with the CTF event template. |
| `player_success() -> number` | Returns number with the value one if the CTF event got completed successfully. |


## metaMail

The in-game mail client.

| Signature | Description |
|---|---|
| `delete(mailId: string) -> number, string, null` | Delete the email corresponding to the provided email ID. |
| `fetch() -> list<string>, string` | Returns a list where each item is a string containing mail id, from, subject and a small preview of the content consisting of the first 125 characters. |
| `read(mailId: string) -> string, null` | Returns a string containing the content of a mail related to the provided mail id. |
| `send(emailAddress: string, subject: string, message: string) -> string, number, null` | Send a new mail to the provided email address. |
