import os

class KyotoIPToCSV(object):

    @classmethod
    def convert(cls, directory, outfile):
        features = "duration,service,source_bytes,destination_bytes,count,same_srv_rate,serror_rate," +\
        "srv_serror_rate,dst_host_count,dst_host_srv_count,dst_host_same_src_port_rate,dst_host_serror_rate," +\
        "dst_host_srv_serror_rate,flag,ids_detection,malware_detection,ashula_detection,label,source_ip_address," +\
        "source_port_number,destination_ip_address,destination_port_number,start_time,duration_session"
        with open(outfile, 'w') as ofile:
            ofile.write(features)
            ofile.write("\n")
            for root, dirs, files in os.walk(directory, topdown=False):
                for d in dirs:
                    for filename in os.listdir(os.path.join(root,d)):
                        with open(os.path.join(root,d,filename)) as ifile:
                            for record in ifile:
                                ofile.write(",".join(record.split()) + "\n")
