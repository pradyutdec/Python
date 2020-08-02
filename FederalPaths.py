from pathlib import Path
import os
 
 
class FederalPaths:
    def __init__(self):
        # Make sure start path is  properly set
        self.set_starting_dir()
        self.homepath = Path('.')
        self.rootpath = self.homepath / '..'
        self.datapath = self.rootpath / 'data'
        self.datapath.mkdir(exist_ok=True)
        self.outpath = self.datapath / 'json'
        self.outpath.mkdir(exist_ok=True)
 
        self.gov_urlbase = 'https://www.usa.gov/'
        self.baseurl = 'https://www.usa.gov/federal-agencies/'
        self.valid_pages = 'abcdefghijlmnoprstuvw'
        self.fed_index_file = self.outpath / 'FedIndex.json'
 
    def set_starting_dir(self):
        path = Path(__file__).resolve()
        path, file = os.path.split(path)
        path = os.path.abspath(path)
        os.chdir(path)
 
def testit():
    FederalPaths()
 
if __name__ == '__main__':
    testit()