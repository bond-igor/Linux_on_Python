from sshcheckers import ssh_checkout_negative, ssh_checkout
from conftest import start_time
from files import save_log
import yaml


with open('config.yaml') as f:
   # читаем документ YAML
   data = yaml.safe_load(f)


class Testneg:
   def test_nstep1(self, make_folders, make_bad_arx, start_time):
       # test neg 1
       save_log(start_time, "nlog1.txt")
       assert ssh_checkout_negative(data["ip"], data["user"], data["passwd"], "cd {}; 7z e {}.{} -o{} -y".format(data["folder_out"], make_bad_arx, data["type"],
                                                                       data["folder_ext"]), "ERROR:"), "test1 FAIL"


   def test_nstep2(self, make_bad_arx, start_time):
       # test neg 2
       save_log(start_time, "nlog2.txt")
       assert ssh_checkout_negative(data["ip"], data["user"], data["passwd"], "cd {}; 7z t {}.{}".format(data["folder_out"], make_bad_arx,
                                                               data["type"]), "ERROR:"), "test2 FAIL"


   def test_nstep3(self, start_time):
       res = []
       res.append(ssh_checkout(data["ip"], data["user"], data["passwd"], "echo '{}' | sudo -S dpkg -r"
                                                                         " {}".format(data["passwd"], data["pkgname"]),
                               "Удаляется"))
       res.append(ssh_checkout(data["ip"], data["user"], data["passwd"], "echo '{}' | "
                                                                         "sudo -S dpkg -s {}".format(data["passwd"],
                                                                                                     data["pkgname"]),
                               "Status: deinstall ok"))
       save_log(start_time, "nlog3.txt")
       assert all(res), "test3 FAIL"
