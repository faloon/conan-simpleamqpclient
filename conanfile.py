from conans import ConanFile, CMake, tools 
import platform 
class SimpleAmqpClientConan(ConanFile):
    name = "simpleamqpclient" # lowercase is what conan seems to like
    case_name = "SimpleAmqpClient" #todo deduct name from repo
    version = "v2.5.1"
    license = "https://github.com/alanxz/SimpleAmqpClient/blob/master/LICENSE-MIT"
    url = "https://github.com/alanxz/SimpleAmqpClient"
    description = "RabbitMQ SimpleAmqpClient"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False], # Build rabbitmq-c as a shared library
        "ssl": [True, False], # Enable SSL support
    }
    default_options = (
        "shared=True",
        "ssl=True",
    )
    requires = ("rabbitmq-c/0.11.0"),("boost/1.76.0"),("zlib/1.2.11")	
    exports = ["CMakeLists.txt.patch"]
    generators = "cmake"
	
	
        
    def configure(self):
        self.options['boost'].shared = False
        self.options["rabbitmq-c"].ssl = self.options.ssl

    def source(self):
        self.run("git clone https://github.com/alanxz/SimpleAmqpClient.git")
        self.run("cd %s && git checkout %s" % (self.case_name, self.version))
        tools.patch(self.case_name, "CMakeLists.txt.patch")

    def build(self):
        cmake = CMake(self)
        command_line = [
            cmake.command_line,
            self.cmake_option_bool("ssl", "ENABLE_SSL_SUPPORT"),
            self.cmake_option_bool("shared", "BUILD_SHARED_LIBS"),
            "-DCMAKE_INSTALL_PREFIX:PATH=%s/_" % self.install_folder			
        ]        
        self.run("cmake %s %s" % (self.case_name, " ".join(command_line)))
        cmake.build()
        self.run("cmake --build . --target install")

    def package(self):
        self.copy("config.h", dst="include", src="librabbitmq")
        self.copy("*.h", dst="include", src="_/include")
        self.copy("*.lib", dst="lib", src="_/lib")
        self.copy("*.a", dst="lib", src="_/lib")
        self.copy("*.so*", dst="lib", src="_/lib")
        if platform.system() == "Windows":
            self.copy("*.dll", dst="bin", src="_/bin")

    def package_info(self):
        if platform.system() == "Windows":
            self.cpp_info.libs = [f"{self.name}.7"] #sac should be dynamic
        else:
            self.cpp_info.libs = [self.case_name]

    def cmake_option_bool(self, name, cmake_name):
        return "-D%s=%s" % (cmake_name, ("ON" if getattr(self.options, name) else "OFF"))
