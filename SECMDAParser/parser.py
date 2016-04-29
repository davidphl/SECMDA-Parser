# This script will parse the Management Discussion and Analysis
# section from SEC Forms 10-k and 10-q
import re
import html2text

class MDAParser():
    def __init__(self):
        self.hello = "Running MD&A Parser"

    def parse_10k(self, file_path):
        print("Parsing form 10-K" + file_path)

        #compile regular expressions
        expr_re_filing_date = re.compile(r'FILED AS OF DATE:\s{1,}[0-9]{1,}', re.IGNORECASE)
        expr_re_item7 = re.compile(r'item\s+?7[^,][^Aa]*?.{0,25}management.*?\s+?discussion.?\s+?and\s+?analysis\s+?',\
                                    re.IGNORECASE)
        expr_re_item8 = re.compile(r'item\s+?8[^,][^\s+?of this].*?financial\s+?statements', re.IGNORECASE)

        #set up mda variables
        filing_dt = None
        mda = None
        item7_end_pos = None
        item8_beg_pos = None

        #configure html 2 text object
        h = html2text.HTML2Text()
        h.ignore_links = True

        #read in file
        f = self.openfile(file_path)
        raw_text = f.read()
        text = html2text.html2text(raw_text)

        #Get filing date
        filing_date = re.search(expr_re_filing_date, text)
        if(filing_date):
            filing_dt = filing_date.string[filing_date.start():filing_date.end()][-8:]

        #find instances of item 7 and item 8 ans substring to get mda
        for match in re.finditer(expr_re_item7, text):
            item7_end_pos = match.end()
        for match in re.finditer(expr_re_item8, text):
            item8_beg_pos = match.start()

        if(item7_end_pos and item8_beg_pos):
            mda = text.encode('ascii','ignore')[item7_end_pos:item8_beg_pos]
        #print(mda)

        # close file
        f.close()
        dict = {'filing_date': filing_dt, 'MDA': mda}
        return(dict)

    def parse_10q(self, file_path):
        print("Parsing form 10-Q: " + file_path)

        # setup regex
        expr_re_filing_date = re.compile(r'FILED AS OF DATE:\s{1,}[0-9]{1,}', re.IGNORECASE)
        expr_re_item2 = re.compile(r'item\s+?2[^,][^Aa]*?.{0,25}management.*?\s+?discussion.?\s+?and\s+?analysis\s+?', \
                                   re.IGNORECASE)
        expr_re_item4 = re.compile(r'item\s+?4.*?controls\s+?and\s+?procedures', re.IGNORECASE)

        # set up mda variables
        filing_dt = None
        mda = None
        item2_end_pos = None
        item4_beg_pos = None

        h = html2text.HTML2Text()
        h.ignore_links = True

        # read in file
        f = self.openfile(file_path)
        raw_text = f.read()

        # text = re.sub('<[^>]*>', '', raw_text)
        text = html2text.html2text(raw_text)

        #Get filing date
        filing_date = re.search(expr_re_filing_date, text)
        if(filing_date):
            filing_dt = filing_date.string[filing_date.start():filing_date.end()][-8:]

        for match in re.finditer(expr_re_item2, text):
            item2_end_pos = match.end()
        for match in re.finditer(expr_re_item4, text):
            item4_beg_pos = match.start()

        if (item2_end_pos and item4_beg_pos):
            mda = text.encode('ascii', 'ignore')[item2_end_pos:item4_beg_pos]
        #print(mda)

        # close file
        f.close()
        dict = {'filing_date': filing_dt, 'MDA': mda}
        return (dict)

    def openfile(self, file_path):
        try:
            return (open(file_path, "r"))
        except:
            print("No input file found")