import subprocess
def runcmd(command):
    subprocess.Popen(command, shell = True)

if __name__ == "__main__":
    runcmd("python test1.py")