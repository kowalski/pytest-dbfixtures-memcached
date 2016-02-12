import pytest

from pytest_dbfixtures.port import get_port
from pytest_dbfixtures.executors import TCPExecutor


def memcached_proc(port='?', memcached='/usr/bin/memcached', host='localhost'):
    '''
        Starts Memcached as a subprocess.

        :param int|str port: exact server port (e.g. '8000')
            or randomly selected port:
                '?' - any random available port
                '2000-3000' - random available port from a given range
                '4002,4003' - random of 4002 or 4003 ports
        :returns pytest fixture with Memcached process executor
    '''

    port = get_port(port)

    @pytest.fixture(scope='session')
    def memcached_proc_fixture(request):
        command = "%s -p %s" % (memcached, port)
        memcached_executor = TCPExecutor(
            command,
            host,
            port,
        )

        request.addfinalizer(memcached_executor.stop)

        memcached_executor.start()

        return memcached_executor

    return memcached_proc_fixture
