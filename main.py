import wmi
from pefile import long
import time
import psutil

c = wmi.WMI ()

# 1 список запущених процесів
def runningProcesses():
    for process in c.Win32_Process():
        yield process.ProcessId, process.Name, int(process.VirtualSize) / (1024*1024)

# 11 список всіх процесів із даним іменем
def runningProcess(name = "notepad.exe"):
    for process in c.Win32_Process(name=name):
        print(process.ProcessId, process.Name, process.VirtualSize / ())
        print(process)

# 2 відсоток вільного простору на дисках
def FreeSpace():
    for disk in c.Win32_LogicalDisk (DriveType=3):
      yield (disk.Caption + "%0.2f%% free" % (100.0 * long(disk.FreeSpace) / long(disk.Size)))


# 3 відкриває текстовий файл, після виводить його вміст
def RunTXT(path = r"C:\temp\temp.txt"):
    filename = path
    process = c.Win32_Process
    process_id, result = process.Create (CommandLine="notepad.exe " + filename)
    watcher = c.watch_for (
      notification_type="Deletion",
      wmi_class="Win32_Process",
      delay_secs=1,
      ProcessId=process_id
    )

    watcher ()
    print("This is what you wrote:")
    print(open (filename).read ())


# 4 Показати IP та MAC-адреси для мережевих інтерфейсів із підтримкою IP
def showNetwork():
    for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
      yield  interface.Description, interface.MACAddress, interface.IPAddress[0]

