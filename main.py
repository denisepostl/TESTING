class CSVToXML():
    def __init__(self, in_file, out_file):
        self.in_file = in_file
        self.out_file = out_file
        self.headers = []
        self.data = []

    def import_file(self):
        with open(self.in_file, 'r') as f:
            cont = f.readlines()
            self.headers = cont[0].strip().split(',')
            self.data = [line.strip().split(',') for line in cont[1:]]
        return cont

    def transform(self):
        self.import_file()
        cont = '<DATA>\n'  
        for row in self.data:
            cont += ' <ROW>\n'
            for i in range(len(self.headers)):
                cont += f'    <{self.headers[i]}>{row[i]}</{self.headers[i]}>\n'  
            cont += ' </ROW>\n'
        cont += '</DATA>\n'
        return cont

    def export(self):
        data = self.transform()
        with open(self.out_file, 'w') as f:
            f.write(data)

def main():
    xml = CSVToXML('in.csv', 'out.xml')
    xml.export()

if __name__ == '__main__':
    main()
