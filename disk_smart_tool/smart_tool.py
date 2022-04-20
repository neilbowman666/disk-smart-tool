from .smart import SMART

smart_features = SMART()


def check_disk(device_path):
    """
    根据磁盘路径检查磁盘健康
    WARNING 硬编码警告⚠
    :param device_path: 磁盘路径
    :return:
    """
    return check_nvme_disk(device_path) if "nvme" in device_path else check_sata_disk(device_path)


def check_nvme_disk(device_path):
    """
    检查 NVME 盘的 Percentage Used 值
    :param device_path:
    :return:
    """
    device_attributes = smart_features.get_nvme_device_attributes(device_path)
    percentage_used_dict = device_attributes[0x04]
    if percentage_used_dict and percentage_used_dict['name'] == 'Percentage Used':
        percentage_used_str: str = percentage_used_dict['value']
        percentage_used = int(percentage_used_str.replace("%", ""))
        return 1, "life percentage less than 50%" if percentage_used > 50 else 0, "ok"
    return 0, "metric missing: r-5(Percentage Used)"


def check_sata_disk(device_path, realloc_sector_thresh_ct_val=0, pending_sector_thresh_ct_val=0):
    """
    检查 SATA 磁盘的 05 C5 状态
    :param device_path: 磁盘路径，如 /dev/sdc
    :param realloc_sector_thresh_ct_val: 重分配扇区阈值计数，输入上次计数可用于判断有无增长
    :param pending_sector_thresh_ct_val: 损坏的扇区阈值计数，输入上次计数可用于判断有无增长
    :return: 是否有告警，错误 2，警告 1，正常 0；信息
    """
    device_attributes = smart_features.get_device_attributes(device_path)
    # disk_exists = bool(device.model)
    pending_sector_ct = device_attributes[0xC5]
    realloc_sector_ct = device_attributes[0x05]

    if pending_sector_ct:
        if int(pending_sector_ct['RAW']) > pending_sector_thresh_ct_val:
            return 2, "found bad sectors"
    else:
        return 0, "metric missing: 0xC5(pending_sector_ct)"

    if realloc_sector_ct:
        if int(realloc_sector_ct['RAW']) > realloc_sector_thresh_ct_val:
            return 1, "found reallocated sectors"
    else:
        return 0, "metric missing: 0x05(realloc_sector_ct)"

    return 0, "ok"


if __name__ == '__main__':
    result = check_nvme_disk("/dev/nvme0n1")
    print(result)
