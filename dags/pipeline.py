import subprocess

# Run Extract process
subprocess.run(["python", "/home/vignesh-nadar/Desktop/sixtyDays/sprint1/project1/src/etl/extract.py"], check=True)

# Run Transform process
subprocess.run(["python", "/home/vignesh-nadar/Desktop/sixtyDays/sprint1/project1/src/etl/transform.py"], check=True)

# Run Load process
subprocess.run(["python", "/home/vignesh-nadar/Desktop/sixtyDays/sprint1/project1/src/etl/load.py"], check=True)

# Run Visualization process
subprocess.run(["python", "/home/vignesh-nadar/Desktop/sixtyDays/sprint1/project1/visualization/viz.py"], check=True)
