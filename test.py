import subprocess
def runcmd(command):
    subprocess.Popen(command, shell = True)

if __name__ == "__main__":
    runcmd("ssh -i /path/to/your/.pem/file/ ec2-user@IPv4-PUBLIC-DNS-ADDRESS.compute-1.amazonaws.com")
    runcmd("python scanner.py")