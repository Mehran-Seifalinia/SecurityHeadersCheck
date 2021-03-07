#!/usr/bin/env python3
# Import modules
try:
    from requests import head
    from sys import argv
    from os import name, system
    from colorama import init, Fore
except ModuleNotFoundError as error:
    name = str(error).split("\'")[1]
    install = input(f"[!] Please install {name} module manually or type \'install\' then press enter.").lower()
    if install == "install":
        try:
            system(f"pip install {name}")
        except:
            print(f"[!] Something wrong, Please install '{name}' manually.")
            exit()
    else:
        exit()

# Colors
default = Fore.RESET
lred = Fore.LIGHTRED_EX
lblue = Fore.LIGHTBLUE_EX
lgreen = Fore.LIGHTGREEN_EX

# Headers to check
security_headers = [
                "Strict-Transport-Security", "Access-Control-Allow-Origin",
                "X-XSS-Protection", "X-Frame-Options", "X-Content-Type-Options",
                "Content-Security-Policy"
                ]

# Headers and their configs
valid_values = {
            "Strict-Transport-Security": "max-age=<expire-time>",
            "Access-Control-Allow-Origin": "<origin>",
            "X-XSS-Protection": "1; mode=block",
            "X-Frame-Options": f"DENY\n\t{lgreen}[OR]->\t\t{lblue}SAMEORIGIN",
            "X-Content-Type-Options": "X-Content-Type-Options: nosniff",
            "Content-Security-Policy": "Content-Security-Policy: default-src 'self'"
            }

corrent_values = {}

# Links to fix
Strict_Transport_Security = "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security"
Access_Control_Allow_Origin = "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin"
X_XSS_Protection = "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection"
X_Frame_Options = "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options"
X_Content_Type_Options = "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options"
Content_Security_Policy = "https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP"

# Settings
exist_header = []
not_exist_header = []
origin_header = "test.com"
seperator = ""
script = ""

# Clear screen and add colors to windows cmd
def clear():
    global seperator, script
    if name == "posix":
        system("clear")
        print(default)
        seperator = "/"
    else:
        system("cls")
        init()
        print(default)
        seperator = "\\"
    
    script = argv[0].split(seperator)[-1]

# Help
def help():
    print(f"{lblue}Security Headers check v1.0  *-* created by mehran-seiflainia *-*\n\t{lgreen}[Usage]: {default}{script} # Run the script normally \
            \n\t\t {script} --cors # Run the script with an 'Origin' header in requests. \
            \n\t\t {script} --cors DOMAIN # Run the script with an custom 'Origin' header. \
            \n\t{lgreen}[Examples]:\n\t\t{default}{script}\n\t\t{script} --cors\n\t\t{script} --cors attacker.com")
    exit()

# Get headers from the site.
def get_headers(url, cors, origin_header):
    try:
        if cors == True:
            response = head(url, headers = {"Origin":origin_header})
        else:
            response = head(url)
        headers = (response.headers)
        return headers.items()
    except Exception as error:
        print(f"{lred}[!] CONNECTION ERROR:\n{error}{default}")
        exit()

# Check all security headers to exist
def is_exist(headers):
    try:
        for header in headers:
            if header[0] in security_headers:
                exist_header.append(header[0])
                corrent_values.update({f"{header[0]}": f"{header[1]}"})
        for header in security_headers:
            if header not in exist_header:
                not_exist_header.append(header)
    except Exception as error:
        print(error)

# Print headers on screen
def printer(url, headers):
    try:
        print(f"{lred}TARGET: {default}{url}\n\n")
        print(f"{lred}-- [Not implemented] --{default}")
        for header in not_exist_header:
            print(f"{lred}{header}{default}")

        print("\n")
        print(f"{lgreen}-- [Implemented] --{default}")
        for header in exist_header:
            print(f"{lgreen}{header}{default}")
            print(f"\t{lgreen}[*] {lblue}The corrent Value is " + corrent_values[header] + f"{default}")
            print(f"\t{lgreen}[*] {lblue}The best value is " + valid_values[header] + f"{default}")

    except Exception as error:
        print(error)

# Check script parameters
def check_params():
    global origin_header
    if len(argv) == 1:
        return False
    elif len(argv) == 2 and argv[1] == "--cors":
        return True
    elif len(argv) == 3 and argv[1] == "--cors":
        origin_header = argv[2]
        return True
    else:
        help()

# main
try:
    clear()
    cors = check_params()
    if cors == False:
        print(f"{lblue}[*] It's possible to sent 'Origin' header in your request check {lred}{script} -h {lblue}[*]{default}")
    url = input("Please enter the URL --> ")
    if "http" not in url:
        url = "http://" + url
    headers = get_headers(url, cors, origin_header)
    is_exist(headers)
    printer(url, headers)
except Exception as error:
    print(error)
