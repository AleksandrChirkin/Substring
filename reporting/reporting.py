class Reporting:
    def __init__(self, for_test=False):
        self.is_testing = for_test

    def run(self, args=None):
        try:
            with open('reporting/report.txt', 'r', encoding='utf-8') as report:
                report_content = report.readlines()
            content = self.get_content(report_content)
            if self.is_testing:
                if args == '0':
                    return content
                elif args == '10':
                    return self.time_analysis(content, self.is_testing, '0')
                elif args == '11':
                    return self.time_analysis(content, self.is_testing, '1')
            else:
                print('Select mode:\n0 - Print whole report\n'
                      '1 - Analyze by time elapsed')
                mode = input()
                if mode == '0':
                    for item in content:
                        print(item)
                elif mode == '1':
                    self.time_analysis(content)
                else:
                    print("Incorrect input!")
        except OSError:
            print('Report file not found!')

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

    def time_analysis(self, report_content, for_test=False, code=None):
        if for_test:
            return self.process_report(code, report_content)
        else:
            print('Enter 0 to sort all units by time\n'
                  'Enter 1 to get average time of algorithm')
            mode = input()
            result = self.process_report(mode, report_content)
            for item in result:
                print(item)

    @staticmethod
    def process_report(mode, report_content):
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
