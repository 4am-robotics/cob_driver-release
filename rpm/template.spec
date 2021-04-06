%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-cob-light
Version:        0.7.5
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS cob_light package

License:        Apache 2.0
URL:            http://ros.org/wiki/cob_light
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python3-devel
Requires:       ros-noetic-actionlib
Requires:       ros-noetic-actionlib-msgs
Requires:       ros-noetic-diagnostic-msgs
Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-rospy
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-visualization-msgs
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  ros-noetic-actionlib
BuildRequires:  ros-noetic-actionlib-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-diagnostic-msgs
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-visualization-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
This package contains scripts to operate the LED lights on Care-O-bot.

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
* Tue Apr 06 2021 Felix Messmer <felixmessmer@gmail.com> - 0.7.5-1
- Autogenerated by Bloom

* Wed Oct 14 2020 Felix Messmer <felixmessmer@gmail.com> - 0.7.4-1
- Autogenerated by Bloom

