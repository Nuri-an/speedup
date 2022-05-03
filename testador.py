import subprocess
from datetime import datetime


def exeSequentialProgram():
    args = ["python", "sequencial.py"]

    subprocess.Popen(
        args,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def exeSixThreadProgram():
    args = ["python", "thread.py"]

    subprocess.Popen(
        args,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def exeThreeThreadProgram():
    args = ["python", "thread-3.py"]

    subprocess.Popen(
        args,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def measureSequential():
    i = 0
    totalTime = 0

    while i < 50:
        startTime = datetime.now()
        exeSequentialProgram()
        endTime = datetime.now()
        totalTime += endTime.timestamp() - startTime.timestamp()
        i += 1

    return totalTime


def measureThreeThread():
    i = 0
    totalTime = 0

    while i < 50:
        startTime = datetime.now()
        exeThreeThreadProgram()
        endTime = datetime.now()
        totalTime += endTime.timestamp() - startTime.timestamp()
        i += 1

    return totalTime


def measureSixThread():
    i = 0
    totalTime = 0

    while i < 50:
        startTime = datetime.now()
        exeSixThreadProgram()
        endTime = datetime.now()
        totalTime += endTime.timestamp() - startTime.timestamp()
        i += 1

    return totalTime


sequentialTime = measureSequential()
threeThreadTime = measureThreeThread()
sixThreadTime = measureSixThread()

print(
    "\n\t Tempo médio de execução para programa sequencial testado 50 vezes: "
    + str(sequentialTime / 50)
    + " segundos. \n"
    + "\t Tempo total: "
    + str(sequentialTime)
)


print(
    "\n\t Tempo médio de execução para programa c/ 3 threads testado 50 vezes: "
    + str(threeThreadTime / 50)
    + " segundos. \n"
    + "\t Tempo total: "
    + str(threeThreadTime)
)

print(
    "\n\t Tempo médio de execução para programa c/ 6 threads testado 50 vezes: "
    + str(sixThreadTime / 50)
    + " segundos. \n"
    + "\t Tempo total: "
    + str(sixThreadTime)
)

speedup_a = (sequentialTime / 50) / (threeThreadTime / 50)
speedup_b = (sequentialTime / 50) / (sixThreadTime / 50)

print(
    "\n\t - SpeedUp Programa sequencial / 3 threads: "
    + str(speedup_a)
    + "\n\t\t ~"
    + str(round(speedup_a * 100, 3))
    + "%"
)
print(
    "\n\t - SpeedUp Programa sequencial / 6 threads: "
    + str(speedup_b)
    + "\n\t\t ~"
    + str(round(speedup_b * 100, 3))
    + "%"
)

print("\n\t Programa Testador finalizado! \n")
