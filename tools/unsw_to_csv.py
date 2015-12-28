import os

class UnswToCSV(object):

    @classmethod
    def convert(cls, directory, feature_file, out):
        features = ""
        with open(feature_file) as f:
            for feature in f:
                if len(features) > 0:
                    features += ","
                features += feature.split(",")[1]
        with open(out, "w") as ofile:
            ofile.write(features)
            ofile.write("\n")
            for root, dirs, files in os.walk(directory, topdown=False):
                for filename in files:
                    if filename.find("features") >= 0:
                        continue
                    with open(os.path.join(root, filename)) as ifile:
                        for record in ifile:
                            ofile.write(record)
