import os
from tempfile import gettempdir


def main():
    check_permission()


def check_permission():
    error = os.system("NET session >nul 2>&1")
    if error == 0:
        activate()
    else:
        uac_bypass()


def uac_bypass():
    with open("{}\\getadmin1.vbs".format(gettempdir())) as f:
        f.write('Set UAC = CreateObject("Shell.Application")\n')
        f.write('UAC.ShellExecute "cmd","/c ""%~s0"" %*", "", "runas", 1\n')

    os.system("{}\\getadmin1.vbs".format(gettempdir()))
    os.remove("{}\\getadmin1.vbs".format(gettempdir()))


def activate():
    os.system('SLMGR /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX')
    # using the activation server
    os.system('SLMGR /skms kms.digiboy.ir')
    print("Please wait this might take sometime. Hold on tight!")
    # activating windows 10 pro
    os.system('SLMGR /ato')

    input("Successfully activated your Windows 10 Pro. Press enter key to exit....")


if __name__ == "__main__":
    main()
