Name:           ros-indigo-cob-phidget-em-state
Version:        0.6.10
Release:        0%{?dist}
Summary:        ROS cob_phidget_em_state package

Group:          Development/Libraries
License:        LGPL
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cob-msgs
Requires:       ros-indigo-cob-phidgets
Requires:       ros-indigo-rospy
BuildRequires:  ros-indigo-catkin

%description
The cob_phidget_em_state package

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Mon Jul 24 2017 Benjamin Maidel <bnm@ipa.fhg.de> - 0.6.10-0
- Autogenerated by Bloom

* Mon Oct 10 2016 Benjamin Maidel <bnm@ipa.fhg.de> - 0.6.8-0
- Autogenerated by Bloom

