class KddToCSV(object):

    @classmethod
    def convert(cls, feature_file, data_file, outfile):
        with open(feature_file) as ffile, open(outfile, 'w') as ofile:
            features = ""
            for i, line in enumerate(ffile):
                if i > 0:
                    if len(features) > 0:
                        features += ","
                    features += line[:line.find(":")]
            ofile.write(features)
            ofile.write("\n")
        with open(data_file) as data, open(outfile, 'a') as ofile:
            for record in data:
                ofile.write(record[:-2] + "\n")
