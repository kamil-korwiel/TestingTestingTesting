import pytest

@pytest.fixture(scope="session")
def setupsession(request):
    # print("Starting Session")

    yield "session_obj"
    # print("Ending Session")


@pytest.fixture(scope="module")
def setupmodule(request, setupsession):
    # print("starting module")
    yield setupsession, "module_obj"
    # print("Ending Module")


@pytest.fixture(scope="class")
def setupclass(request, setupmodule):
    # print("starting class")
    yield (*setupmodule, "class_obj")
    # print("Ending class")


@pytest.fixture(scope="function")
def setupmethod(request, setupclass):
    # print("starting method")
    yield (*setupclass, "class_obj")
    # print("Ending method")