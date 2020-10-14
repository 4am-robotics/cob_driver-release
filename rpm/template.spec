%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-cob-generic-can
Version:        0.7.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS cob_generic_can package

License:        Apache 2.0
URL:            http://ros.org/wiki/cob_generic_can
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-cob-utilities
Requires:       ros-noetic-libntcan
Requires:       ros-noetic-libpcan
Requires:       ros-noetic-socketcan-interface
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-cob-utilities
BuildRequires:  ros-noetic-libntcan
BuildRequires:  ros-noetic-libpcan
BuildRequires:  ros-noetic-socketcan-interface
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The package cob_generic_can provides an interface for nodes on a can-bus and
examplary wrappers for two PeakSys-can-libs. When a can-bus-device is generated
(for an example see base_dirve_chain) you can use generic_can to create as many
itfs as there will be components communicating via this can-bus. Assign type of
the can communication device (e.g. usb-to-can or can-card of a specific vendor)
and can-address of the target device. This package comes with wrappers for
PeakSys and PeakSysUSB adapters.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Wed Oct 14 2020 Matthias Gruhler <mig@ipa.fhg.de> - 0.7.4-1
- Autogenerated by Bloom

