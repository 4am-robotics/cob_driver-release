Name:           ros-indigo-cob-head-axis
Version:        0.6.3
Release:        0%{?dist}
Summary:        ROS cob_head_axis package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_head_axis
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-cob-canopen-motor
Requires:       ros-indigo-cob-generic-can
Requires:       ros-indigo-cob-srvs
Requires:       ros-indigo-cob-utilities
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-libntcan
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rostest
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-urdf
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cob-canopen-motor
BuildRequires:  ros-indigo-cob-generic-can
BuildRequires:  ros-indigo-cob-srvs
BuildRequires:  ros-indigo-cob-utilities
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-libntcan
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-urdf

%description
cob_head_axis

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
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
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Jun 17 2015 Matthias Gruhler <mig@ipa.fhg.de> - 0.6.3-0
- Autogenerated by Bloom

