Name:           ros-hydro-cob-footprint-observer
Version:        0.5.4
Release:        0%{?dist}
Summary:        ROS cob_footprint_observer package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_footprint_observer
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-tf
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-tf

%description
The cob_footprint_observer package adjusts the footprint of the robot based on
the setup (e.g. arm and/or tray).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Aug 25 2014 Matthias Gruhler <mig@ipa.fhg.de> - 0.5.4-0
- Autogenerated by Bloom

