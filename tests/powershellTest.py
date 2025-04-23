import subprocess
import threading as th

class PSSession():
    def __init__(self):
        x = subprocess.Popen(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"], 
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        print("init powershell!")

    def runPowershellCommand(self, cmd):
        x = subprocess.Popen(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", "-Command", cmd],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, err = x.communicate()
        print("cmd ran!")
        print(f"{out} === {err}")

class executer(th.Thread):
    def __init__(self):
        th.Thread.__init__(self)
        self.initiate()

    def initiate(self):
        self.session = PSSession()

    def runCmd(self, cmd):
        self.session.runPowershellCommand(cmd)

x = executer()
x.runCmd("$x = 'Out Test'")
x.runCmd("write-output $x")
x.runCmd("$x = Get-Content -Raw 'SECRET.json' | ConvertFrom-Json")
x.runCmd("$y = ConvertTo-SecureString -AsPlainText -Force ($x.SECRET)")
x.runCmd("$cred = New-Object System.Management.Automation.PSCredential -ArgumentList ($x.CLIENT, $y)")
x.runCmd("Connect-MgGraph -TenantId $x.TENANT -ClientSecretCredential $cred -NoWelcome -ErrorAction SilentlyContinue")
x.runCmd("if ($?) { Write-Output 'CONNECTED TO TENANT!' } else { Write-Output 'CONNECT FAILED!' }")
print(x)