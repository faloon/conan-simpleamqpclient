# conan-simpleamqpclient
Conan recipe for [SimpleAmqpClient by alanxz](https://github.com/alanxz/SimpleAmqpClient)

## Notes 

* probably forked from [here](https://github.com/db4/conan-SimpleAmqpClient) some years ago
* only shared lib
* no tests
* slightly boilerplatey
* plenty of room for improvement

## Build

### Linux

```docker build . ```

### Windows

```conan create . simpleamqpclient/v2.5.1@conan/stable --build missing```

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
