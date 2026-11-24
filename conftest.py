import pytest
import uiautomator2 as u2


@pytest.fixture(scope="session")
def device():
    """Conecta ao dispositivo Android via ADB (usa o primeiro disponível)."""
    d = u2.connect()
    yield d
