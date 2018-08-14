# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools

class UtfcppConan(ConanFile):
    name = 'utfcpp'
    version = '2.3.5'
    description = 'UTF-8 with C++ in a Portable Way.'
    url = 'https://github.com/birsoyo/conan-utfcpp'
    homepage = 'https://github.com/nemtrif/utfcpp'
    author = 'Orhun Birsoy <orhunbirsoy@gmail.com>'

    license = '<Indicates License type of the packaged library>'

    no_copy_source = True

    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"

    def source(self):
        source_url = 'https://github.com/nemtrif/utfcpp'
        tools.get(f'{source_url}/archive/v{self.version}.tar.gz')
        extracted_dir = self.name + '-' + self.version

        #Rename to "source_folder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)

    def package(self):
        include_folder = os.path.join(self.source_subfolder, 'source')
        self.copy(pattern='LICENSE', dst='license', src=self.source_subfolder)
        self.copy(pattern='*', dst='include', src=include_folder)

    def package_id(self):
        self.info.header_only()
