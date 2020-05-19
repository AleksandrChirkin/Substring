class Algorithm:
    def __init__(self, text, template, for_test=False):
        self.text = text
        self.template = template
        self.is_testing = for_test

    def run(self):
        pass

    def output(self, algorithm, counter, time):
        fragments = ["Algorithm: "+algorithm,
                     "Current template: "+self.template,
                     "Fragments found: "+str(counter),
                     "Time elapsed: "+str(time), 120*'-']
        result = '\n'.join(fragments)+'\n'
        if self.is_testing is False:
            print(result)
        with open('reporting/report.txt', 'a+', encoding='utf-8') as report:
            report.write(result)
