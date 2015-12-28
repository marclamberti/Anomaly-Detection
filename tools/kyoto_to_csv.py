import os

class KyotoToCSV(object):

    @classmethod
    def convert(cls, directory, kyoto_with_ip_directory, outfile):
        features = "duration,service,source_bytes,destination_bytes,count,same_srv_rate,serror_rate," +\
        "srv_serror_rate,dst_host_count,dst_host_srv_count,dst_host_same_src_port_rate,dst_host_serror_rate," +\
        "dst_host_srv_serror_rate,flag,ids_detection,malware_detection,ashula_detection,label"
        with open(outfile, 'w') as ofile:
            ofile.write(features)
            ofile.write("\n")
            for root, dirs, files in os.walk(directory, topdown=False):
                for d in dirs:
                    for filename in os.listdir(os.path.join(root,d)):
                        file_path = os.path.join(root, d, filename)
                        kyoto_with_ip_path = os.path.join(kyoto_with_ip_directory, d, filename)
                        if not os.path.isfile(kyoto_with_ip_path):
                            continue
                        with open(file_path) as ifile, open(kyoto_with_ip_path) as kfile:
                            for record, krecord in zip(ifile, kfile):
                                label = krecord.split()[17]
                                ofile.write(",".join(record.split()) + "," + label + " \n")
