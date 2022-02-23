import os
import timeit

compile_python = "morloc make networkPYTest.loc"
compile_cpp = "morloc make networkCPPTest.loc"
run_nexus = "./nexus.pl sigmoid 12"
setup ='''import os
run_nexus = "./nexus.pl sigmoid 12"'''

trials = 0

code = '''
def run():
    os.system(run_nexus)
'''

os.system(compile_python)
python_time = timeit.timeit(setup=setup, stmt=code, number=trials)
os.system(compile_cpp)
os.system("clear")
cpp_time = timeit.timeit(setup=setup, stmt=code, number=trials)

print("Time to run sigmoid", trials, "times from python source: ", python_time)
print("Time to run sigmoid", trials, "times from cpp source: ", cpp_time)
