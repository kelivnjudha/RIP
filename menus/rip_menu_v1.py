import os
import sys
sys.path.append('.')
import rip

def menu():
    pass


def disclaimer():
    print('''
            [ RIP_MENU_V1.0 ]       .
    --------------------------------
       This script is intended for 
    educational and testing purposes 
     only. Do not use this script on 
    any system or network without the
      explicit consent of the owner.  
    --------------------------------
    is not responsible for any damages
    or losses resulting from the use 
            of this script.
            
    *********************************
    *  By running this script, you  *
    *acknowledge that you understand* 
    *   the risks and accept full   *
    *     responsibility for any    *
    *   consequences that may occur.*
    *********************************
    ''')
    sec_c = input('Do you want to continue? (y/n) > ').lower()
    if sec_c.startswith('y'):
        menu()
    else:
        print('Exiting script...')
        rip.rip_menu()

disclaimer()