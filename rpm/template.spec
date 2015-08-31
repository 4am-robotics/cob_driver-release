Name:           ros-indigo-cob-undercarriage-ctrl
Version:        0.6.5
Release:        0%{?dist}
Summary:        ROS cob_undercarriage_ctrl package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_undercarriage_ctrl
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cob-msgs
Requires:       ros-indigo-cob-utilities
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-diagnostic-updater
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cob-msgs
BuildRequires:  ros-indigo-cob-utilities
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-diagnostic-updater
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf

%description
cob_undercarriage_ctrl implements a controller for the omnidirectional base of
Care-O-bot 3 on joint level. For a given Pltf-Twist the according wheel steering
angles and linear wheel velocities are calculated based on the principle of
rigid body motion. Each joint is than controlled individually to achieve the
computed position and velocity

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
* Mon Aug 31 2015 Matthias Gruhler <mig@ipa.fhg.de> - 0.6.5-0
- Autogenerated by Bloom

* Tue Aug 25 2015 Matthias Gruhler <mig@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Matthias Gruhler <mig@ipa.fhg.de> - 0.6.3-0
- Autogenerated by Bloom

* Mon Dec 15 2014 Matthias Gruhler <mig@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

* Wed Sep 17 2014 Matthias Gruhler <mig@ipa.fhg.de> - 0.6.1-0
- Autogenerated by Bloom

* Tue Sep 09 2014 Matthias Gruhler <mig@ipa.fhg.de> - 0.6.0-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Matthias Gruhler <mig@ipa.fhg.de> - 0.5.7-0
- Autogenerated by Bloom

