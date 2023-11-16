import subprocess
import paramiko
from sshcheckers import ssh_getout
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)

def upload_files(host, user, passwd, local_path, remote_path, port=22):
    print(f"Загружаем файл {local_path} в каталог {remote_path}")
    transport = paramiko.Transport((host, port))
    transport.connect(None, username=user, password=passwd)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(local_path, remote_path)
    if sftp:
        sftp.close()
    if transport:
        transport.close()

def save_log(start_time, name):
    if "noop" in subprocess.run(f'[ -d "{data["folder_log"]}" ] && echo "yes" || echo "noop"', shell=True,
                                stdout=subprocess.PIPE, encoding='utf-8').stdout:
        subprocess.run(f"mkdir {data['folder_log']}", shell=True)
    with open(f"{data['folder_log']}/{name}", "w") as f:
        f.write(ssh_getout(data["ip"], data["user"], data["passwd"], "journalctl --since '{}'".format(start_time)))


