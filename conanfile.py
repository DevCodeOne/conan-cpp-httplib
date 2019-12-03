#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os

class CppHttpLibConan(ConanFile):
    name = "cpp-httplib"
    version = "0.3.1"
    url = "https://github.com/zinnion/conan-cpp-httplib"
    description = "A single file C++11 header-only HTTP/HTTPS server and client library"
    license = "MIT"
    no_copy_source = True
    build_policy = "always"
    requires = "OpenSSL/1.1.1c@conan/stable", "zlib/1.2.11@conan/stable"
    exports_source = "sources/*"

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="sources")
        return cmake

    def source(self):
        source_url = "https://github.com/yhirose/cpp-httplib"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, "sources")

    def package_id(self):
        self.info.header_only()

    def package(self):
        self.copy(pattern="LICENSE")
        cmake = self._configure_cmake()
        cmake.install()
