Assignment bundle - Python solutions and supporting files

Structure:

- q1/ bank.py, student.py
- q2/ string_tools.py, main.py, utils/ (math_utils.py, string_utils.py) and demo_main.py
- q3/ map_filter_reduce.py, GenericStack.cpp
- q4/ world_population.py, sample_population.csv (small sample for simulate mode)
- q5/ thread_demo.py, multithread_download.py
- q6/ github_api.py, async_github.py

Notes:
- This environment has no outbound internet access, so scripts that fetch remote data (Q4, Q5b, Q6) are provided but not executed.
- For Q4 and Q5b you can run scripts locally (Python 3.8+) and they will fetch data from the URLs. Use the --simulate flag when available to run with the bundled sample CSVs.

How to run examples locally:
- Q1: python q1/bank.py ; python q1/student.py
- Q2: python -m q2.main (or run q2/demo_main.py)
- Q3: python q3/map_filter_reduce.py
- Q4: python q4/world_population.py --simulate
- Q5: python q5/thread_demo.py ; python q5/multithread_download.py
- Q6: python q6/github_api.py (requires requests); python q6/async_github.py (requires aiohttp)

Files produced in this bundle include sample PNG screenshots for Q1, Q2, Q3 and Q5 created by this environment to demonstrate outputs.
