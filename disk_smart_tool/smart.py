import os

ATTR_TABLE_HEADER = [
    "ID#",
    "ATTRIBUTE_NAME",
    "FLAG",
    "VALUE",
    "WORST",
    "THRESH",
    "TYPE",
    "UPDATED",
    "WHEN_FAILED",
    "RAW_VALUE",
]


class SMART:

    def run(self, str_args):
        cmd_str = "smartctl " + str_args
        output = os.popen(cmd_str).read()
        lines = str.splitlines(output)

        return lines

    def get_device_health(self, device_path):
        device_info_lines = self.run("-H " + device_path)
        return device_info_lines[-2]

    def get_device_attributes(self, device_path):
        device_info_lines = self.run("-A " + device_path)

        index = len(device_info_lines)
        for i in range(len(device_info_lines)):
            if device_info_lines[i].startswith('ID#'):
                index = i + 1
                break

        info_dict = dict()
        for i in range(index, len(device_info_lines) - 1):
            x = device_info_lines[i].strip().split()
            raw = " ".join(x[9:])
            x = x[:9]
            x.append(raw)
            info_dict[x[0]] = {ATTR_TABLE_HEADER[nx]: x[nx] for nx in range(len(x))}

        return info_dict

    def get_nvme_device_attributes(self, device_path):
        device_info_lines = self.run("-A " + device_path)

        index = len(device_info_lines)
        for i in range(len(device_info_lines)):
            if device_info_lines[i].startswith('Critical Warning:'):
                index = i
                break

        info_dict = dict()
        for i in range(index, index + 15):
            (r_k, r_v) = device_info_lines[i].split(":")
            key = r_k.strip()
            val = r_v.strip()
            info_dict[i - index] = {
                "name": key,
                "value": val
            }

        return info_dict


if __name__ == '__main__':
    smart_features = SMART()

    print("++++++++++++++++ sdd ++++++++++++++++")
    device_attributes_dict = smart_features.get_device_attributes("/dev/sdd")
    for k, v in device_attributes_dict.items():
        print(v)
    print("-------------------------------------")

    nvme_device_attributes_dict = smart_features.get_nvme_device_attributes("/dev/nvme0n1")
    print("++++++++++++++ nvme0n1 ++++++++++++++")
    for k, v in nvme_device_attributes_dict.items():
        print(v)
    print("-------------------------------------")
