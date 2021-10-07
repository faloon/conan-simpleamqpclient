# conan-simpleamqpclient
Conan recipe for SimpleAmqpClient by alanxz

## Please note 

* only shared lib
* no tests
* slightly boilerplatey

## build

### Linux

```docker build . ```

### Windows

```conan create . simpleamqpclient/v2.5.1@conan/stable```

Tested with
```
arch=x86_64
arch_build=x86_64
build_type=Release
compiler=Visual Studio
compiler.runtime=MD
compiler.version=15
os=Windows
os_build=Windows
```
* cmake 3.15.1
* conan 1.40.3
