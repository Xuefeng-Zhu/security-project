import dpkt
import socket
import sys


def process_packet(buf, ip_dict):
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data

    if type(ip) is not dpkt.ip.IP:
        return

    tcp = ip.data
    if type(tcp) is not dpkt.tcp.TCP:
        return

    src_ip = socket.inet_ntop(socket.AF_INET, ip.src)
    dst_ip = socket.inet_ntop(socket.AF_INET, ip.dst)
    if tcp.flags == 0x02:
        ip_info = ip_dict.setdefault(src_ip, (0, 0))
        ip_dict[src_ip] = (ip_info[0] + 1, ip_info[1])
    elif tcp.flags == 0x12:
        ip_info = ip_dict.setdefault(dst_ip, (0, 0))
        ip_dict[dst_ip] = (ip_info[0], ip_info[1] + 1)


def get_anomaly_ip(ip_dict):
    for (ip, count) in ip_dict.items():
        if count[1] is 0 or count[0] > 3 * count[1]:
            print ip, count[0], count[1]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Please provide the name of PCAP file to be analyzed"
        sys.exit(1)

    f = open(sys.argv[1])
    pcap = dpkt.pcap.Reader(f)
    ip_dict = dict()
    for _, buf in pcap:
        try:
            process_packet(buf, ip_dict)
        except dpkt.dpkt.UnpackError:
            pass

    get_anomaly_ip(ip_dict)
    f.close()
