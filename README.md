# What

Package [socklog](http://smarden.org/socklog/index.html) for deployment.

# How

```
yum -q -y install rpmdevtools git glibc-static
yum -q -y groupinstall "Development Tools"
git clone https://github.com/shore/socklog-rpm socklog-rpm
cd ./socklog-rpm
./build.sh
sudo rpm -i ~/rpmbuild/RPMS/*/socklog-*.rpm
```

