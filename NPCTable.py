

class NPCTable():
    values = None

    def __init__(self, table_path):
        self.values = {}
        table_file = open(table_path, 'r')
        header = table_file.readline().split(',')
        header = [x.replace("\n", "") for x in header]

        for col_name in header:
            self.values[col_name] = []

        line = table_file.readline()
        while line:
            cols = [x.replace("\n", "") for x in line.split(',')]
            for ii,col_name in enumerate(header):
                self.values[col_name].append(cols[ii])
            line = table_file.readline()

    def getValueAtLevel(self, category, level):
        if category == "":
            return""

        if type(level) is int:
            level = str(level)

        level_index = self.values['Level'].index(level)
        return self.values[category][level_index]
        
