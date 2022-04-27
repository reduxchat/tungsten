import time
import os
import threading

class SnowflakeFactory:
    def __init__(self) -> None:
        self._epoch: int = 1649325271415
        self._incrementation = 0

    def formulate(self) -> int:
        current_ms = time.time_ns() // 1000000
        epoch = current_ms - self._epoch << 22

        epoch |= threading.current_thread().ident << 17
        epoch |= os.getpid() << 12

        epoch |= self._incrementation % 0xFFF

        self._incrementation += 1

        return epoch

if __name__ == '__main__':
    f = SnowflakeFactory()
    print(f.formulate())