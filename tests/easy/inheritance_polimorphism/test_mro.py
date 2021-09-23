import pytest

from tasks.easy.inheritance_polimorphism.mro import (
    Device,
    Copier,
    Scanner,
    MFU
)


def test_device():
    with pytest.raises(TypeError):
        Device()

    assert hasattr(Device, "process_doc")


def test_copier():
    copier = Copier()
    assert copier.process_doc("Doc") == "Делаю копию: Doc"


def test_scanner():
    scanner = Scanner()
    assert scanner.process_doc("Doc") == "Сканирую документ: Doc"


def test_mfu():
    mfu = MFU()
    assert mfu.process_doc("Doc") == "Сканирую, отправляю факс: Doc"
