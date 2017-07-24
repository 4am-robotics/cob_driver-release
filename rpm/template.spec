Name:           ros-kinetic-cob-driver
Version:        0.6.10
Release:        0%{?dist}
Summary:        ROS cob_driver package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_driver
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-cob-base-drive-chain
Requires:       ros-kinetic-cob-bms-driver
Requires:       ros-kinetic-cob-camera-sensors
Requires:       ros-kinetic-cob-canopen-motor
Requires:       ros-kinetic-cob-elmo-homing
Requires:       ros-kinetic-cob-generic-can
Requires:       ros-kinetic-cob-head-axis
Requires:       ros-kinetic-cob-light
Requires:       ros-kinetic-cob-mimic
Requires:       ros-kinetic-cob-phidgets
Requires:       ros-kinetic-cob-relayboard
Requires:       ros-kinetic-cob-scan-unifier
Requires:       ros-kinetic-cob-sick-lms1xx
Requires:       ros-kinetic-cob-sick-s300
Requires:       ros-kinetic-cob-sound
Requires:       ros-kinetic-cob-undercarriage-ctrl
Requires:       ros-kinetic-cob-utilities
Requires:       ros-kinetic-cob-voltage-control
BuildRequires:  ros-kinetic-catkin

%description
The cob_driver stack includes packages that provide access to the Care-O-bot
hardware through ROS messages, services and actions. E.g. for mobile base, arm,
camera sensors, laser scanners, etc...

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Jul 24 2017 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.10-0
- Autogenerated by Bloom

