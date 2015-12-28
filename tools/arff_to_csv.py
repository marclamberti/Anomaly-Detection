class ArffToCSV(object):

    @classmethod
    def convert(cls, infile, outfile):
        attribute_field = "@attribute"
        data_field = "@data"
        with open(infile) as ifile, open(outfile, 'w') as ofile:
            header = ""
            header_written = False
            data_written = False
            for line in ifile:
                if header_written == False and line.find(attribute_field) >= 0:
                    first_quote = line.find("'")
                    if len(header) > 0:
                        header += ","
                    header += line[first_quote + 1: first_quote + 1 + line[first_quote + 1:].find("'")]
                if data_written or line.find(data_field) >= 0:
                    if header_written == False:
                        ofile.write(header)
                        ofile.write("\n")
                        header_written = True
                        data_written = True
                    else:
                        ofile.write(line)
