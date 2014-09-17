Name:           ros-indigo-cob-phidgets
Version:        0.6.1
Release:        0%{?dist}
Summary:        ROS cob_phidgets package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_phidgets
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-libphidgets
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-libphidgets
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs

%description
cob_phidgets

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Sep 17 2014 Benjamin Maidel <benjamin.maidel@ipa.fraunhofer.de> - 0.6.1-0
- Autogenerated by Bloom

* Tue Sep 09 2014 Benjamin Maidel <benjamin.maidel@ipa.fraunhofer.de> - 0.6.0-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Benjamin Maidel <benjamin.maidel@ipa.fraunhofer.de> - 0.5.7-0
- Autogenerated by Bloom

