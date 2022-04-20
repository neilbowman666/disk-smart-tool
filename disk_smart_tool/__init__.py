from disk_smart_tool.smart import SMART
from disk_smart_tool.smart_tool import check_disk, check_nvme_disk, check_sata_disk

name = 'disk-smart-tool'

__version__ = '0.0.1'
VERSION = __version__

__all__ = [
    'SMART',
    'check_disk',
    'check_nvme_disk',
    'check_sata_disk',
]
