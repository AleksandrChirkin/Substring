class Reporting:
    """
        Analyzes a report created after running algorithms

        Keys:
        0 - Shows whole report
        10 - Sorts each run by elapsed time
        11 - Sorts algorithms by average time
    """
    def __init__(self):
        pass

    def run(self, arg):
        try:
            with open('reporting/report.txt', 'r', encoding='utf-8') as report:
                report_content = report.readlines()
            content = self.get_content(report_content)
            if arg == '0':
                return content
            elif arg == '10':
                return self.time_analysis(content, '0')
            elif arg == '11':
                return self.time_analysis(content, '1')
            raise NameError()
        except OSError:
            print('Report file not found!')
        except NameError:
            print('Invalid reporting key!')

    @staticmethod
    def get_content(report_content):
        result = []
        item = {}
        for string in report_content:
            if string[:-1] == 120*'-':
                result.append(item)
                item = {}
            elif string[:10] == 'Algorithm:':
                item['Algorithm:'] = string[11:-1]
            elif string[:13] == 'Time elapsed:':
                item['Time elapsed:'] = float(string[14:-1])
            elif string[:16] == 'Fragments found:':
                item['Fragments found:'] = int(string[17:-1])
            elif string[:17] == 'Current template:':
                item['Template:'] = string[18:-1]
            elif string[:20] == 'Collisions occurred:':
                item['Collisions occurred:'] = int(string[21:-1])
        return result

    @staticmethod
    def time_analysis(report_content, mode):
        if mode == '0':
            return sorted(report_content,
                          key=lambda element:
                          float(element['Time elapsed:']))
        elif mode == '1':
            sorted_content = sorted(report_content,
                                    key=lambda element:
                                    element['Algorithm:'])
            times = {}
            current_algorithm = sorted_content[0]['Algorithm:']
            current_number = 0
            current_time = 0.0
            for item in sorted_content:
                if item['Algorithm:'] != current_algorithm:
                    times[current_algorithm] = current_time / current_number
                    current_algorithm = item['Algorithm:']
                    current_number = 0
                    current_time = 0.0
                current_time += float(item['Time elapsed:'])
                current_number += 1
            else:
                times[current_algorithm] = current_time / current_number
            return sorted(times.items(), key=lambda element: element[1])
