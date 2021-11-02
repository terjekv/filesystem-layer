# Creating the package.

````
mkdir -p ~/rpmbuild/RPMS
mkdir -p ~/rpmbuild/SOURCES
mkdir -p ~/rpmbuild/SPECS

cp eessi-release.spec ~/rpmbuild/SPECS
cp eessi.rep ~/rpmbuild/SOURCES

cd ~/rpmbuild/SPECS/
rpmbuild -ba eessi-release.spec
````

The package should be under `~/rpmbuild/RPMS/noarch/`.