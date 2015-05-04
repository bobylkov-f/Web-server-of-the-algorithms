import configparser
import os
import shutil
import pytest
from build_bot.Languages.cpp_language import CPPLanguage
from build_bot.Languages.cs_language import CSLanguage
from build_bot.Languages.fp_language import FPLanguage


@pytest.fixture(scope="class")
def test_build_directory_fixture(request):
    request.cls.test_name = getattr(request.module, "test_name", "default_module")

    project_path = os.path.dirname(os.path.dirname(__file__))
    request.cls.build_dir = os.path.join(os.path.join(project_path, "_build"), request.cls.test_name)

    if os.path.exists(request.cls.build_dir):
        shutil.rmtree(request.cls.build_dir)

    request.cls.build_dir_bin = os.path.join(request.cls.build_dir, "bin")
    if not os.path.exists(request.cls.build_dir_bin):
        os.makedirs(request.cls.build_dir_bin)

    request.cls.src_code_dir = os.path.join(project_path, "code_to_compile")


@pytest.fixture(scope="class")
def test_config_fixture(request, test_build_directory_fixture):
    config_file_path = os.path.join(request.cls.build_dir, "test_build_bot.cfg")
    f = open(config_file_path, "w+")
    f.write("[compiler_paths]\n")
    f.write("cpp_path = " + CPPLanguage.DEFAULT_COMPILER_DIR + "\n")
    f.write("cs_path = " + CSLanguage.DEFAULT_COMPILER_DIR + "\n")
    f.write("fp_path = " + FPLanguage.DEFAULT_COMPILER_DIR + "\n")
    f.close()

    request.cls.config_parser = configparser.ConfigParser()
    request.cls.is_config_read_ok = request.cls.config_parser.read(config_file_path)
