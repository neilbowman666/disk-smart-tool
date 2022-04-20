# Disk S.M.A.R.T. tool

read disk S.M.A.R.T. of SATA disks and NVME disks

## Dependency

```bash
# Debian / Ubuntu
apt-get install -y smartmontools
# RHEL / CentOS / Fedora
yum install -y smartmontools
```

## Usage

```python
from smart_tool import check_disk

result = check_disk("/dev/sda")
```