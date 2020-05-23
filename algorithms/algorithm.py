from abc import abstractmethod
from time import perf_counter


class Algorithm:
    def __init__(self):
        self.time = perf_counter()

    @abstractmethod
    def run(self, text, template) -> int:
        raise NotImplementedError()

    def update_report(self, algorithm, counter, template):
        self.time = perf_counter()-self.time
        fragments = ["Algorithm: "+algorithm,
                     "Current template: "+template,
                     "Fragments found: "+str(counter),
                     "Time elapsed: "+str(self.time), 120*'-']
        result = '\n'.join(fragments)+'\n'
        with open('reporting/report.txt', 'a+', encoding='utf-8') as report:
            report.write(result)
