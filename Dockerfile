from ubuntu:20.10
#dunno if all are needed..you test
RUN apt-get update && apt-get install -y \
	libgtk2.0-dev \
	python3-pip \
	software-properties-common \
        gnupg2 \
        ca-certificates \
	apt-transport-https \
	apt-utils \
	wget \
	git autoconf automake build-essential sudo apt-utils

RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | tee /etc/apt/trusted.gpg.d/kitware.gpg >/dev/null
RUN apt-add-repository 'deb https://apt.kitware.com/ubuntu/ bionic main'
RUN apt-get update && apt-get install -y cmake

RUN pip3 install conan==1.40.3
ENV CONAN_REVISIONS_ENABLED=1 

WORKDIR /simple
COPY conanfile.py .
COPY CMakeLists.txt.patch .
RUN conan create . simpleamqpclient/v2.5.1@conan/stable --build missing
