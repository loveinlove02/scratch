import psutil


def list_running_processes():

    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'status']):
        if proc.info['status'] == psutil.STATUS_RUNNING:
            processes.append(proc.info)

    return processes 

def terminate_process(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"프로세스 {pid}가 종료되었습니다.")
    except psutil.NoSuchProcess:
        print(f"프로세스 {pid}를 찾을 수 없습니다.")
    except psutil.AccessDenied:
        print(f"프로세스 {pid}를 종료할 권한이 없습니다.")


processes = list_running_processes()

for i, proc in enumerate(processes, 1):
    if proc['name']=='chrome.exe':
        print(f"{i}. PID: {proc['pid']}, 이름: {proc['name']}")
        terminate_process(proc['pid'])

